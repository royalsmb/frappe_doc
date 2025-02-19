import frappe
import inspect
import json
import functools
from pathlib import Path
from typing import Dict, List, Optional, Callable
import os
from frappe import scrub
import zipfile
import importlib.util
import sys

def bruno(method="get"):
    """
    Decorator to mark and document API endpoints for Bruno.
    Only accepts HTTP method as a parameter, defaults to POST.
    """
    def decorator(func: Callable) -> Callable:
        docstring = inspect.getdoc(func) or ""
        parameters = inspect.signature(func).parameters
        
        param_dict = {
            name: ""  
            for name, param in parameters.items()
            if name not in ['self', 'args', 'kwargs']
        }
        
        
        module_path = func.__module__
        
        func._bruno_doc = {
            "description": docstring,
            "method": method.lower(),
            "body": param_dict,
            "module_path": module_path
        }
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

class BrunoCollectionGenerator:
    """Bruno collection generator for Frappe Framework applications."""
    
    def __init__(self, app_name: str, docname: Optional[str] = None):
        self.settings = frappe.get_doc("Bruno Collection", docname)
        self.docname = docname
        self.app_name = scrub(self.settings.module)
        self.app_path = frappe.get_app_path(app_name)
        # Create a "bruno collections" subfolder
        self.collection_path = os.path.join(frappe.get_site_path(), "public", "files", "bruno_collections", self.docname)
        self.sequence_counter = 1
        self.file_folders = {}

    def generate_collection(self):
        """Generates Bruno collection files."""
        # Create collections directory if it doesn't exist
        os.makedirs(self.collection_path, exist_ok=True)
        
        # Create bruno.json file
        self._create_bruno_json()
        
        # Create main collection.bru file only at the root
        self._create_collection_file()
        
        # Scan for API endpoints and create collection files
        for path in Path(self.app_path).rglob("*.py"):
            relative_path = path.relative_to(self.app_path)
            if not any(part.startswith((".", "_")) for part in relative_path.parts):
                self._analyze_file(path)

    def _create_bruno_json(self):
        """Creates the bruno.json configuration file."""
        bruno_config = {
            "version": "1",
            "name": self.settings.collection_name,
            "type": "collection",
            "ignore": [
                "node_modules",
                ".git"
            ]
        }
        
        with open(os.path.join(self.collection_path, "bruno.json"), "w") as f:
            json.dump(bruno_config, f, indent=2)

    def _create_collection_file(self):
        """Creates the collection.bru file with environment variables."""
        collection_content = f"""meta {{
  name: {self.app_name.capitalize()}
}}

auth {{
  mode: none
}}

vars:pre-request {{
  base_url: {self.settings.base_url}
}}"""
        
        with open(os.path.join(self.collection_path, "collection.bru"), "w") as f:
            f.write(collection_content)

    def _import_module_from_file(self, file_path: Path) -> Optional[object]:
        """Import a module from file path."""
        try:
            # Get the module name from the file path
            relative_path = file_path.relative_to(self.app_path)
            module_parts = list(relative_path.parts)
            if module_parts[-1].endswith('.py'):
                module_parts[-1] = module_parts[-1][:-3]
            
            module_name = f"{self.app_name}.{'.'.join(module_parts)}"
            
            # Try importing using spec
            spec = importlib.util.spec_from_file_location(module_name, str(file_path))
            if spec is None or spec.loader is None:
                return None
                
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            return module
        except Exception as e:
            frappe.logger().error(f"Error importing module {file_path}: {str(e)}")
            return None

    def _analyze_file(self, file_path: Path):
        """Analyzes a Python file for API endpoints."""
        module = self._import_module_from_file(file_path)
        if not module:
            return
            
        # Find any functions with bruno decorator
        endpoints = []
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and hasattr(obj, '_bruno_doc'):
                # Update the module path in the bruno doc to reflect the actual path
                relative_path = file_path.relative_to(self.app_path)
                module_path = str(relative_path).replace('/', '.').replace('.py', '')
                if hasattr(obj, '_bruno_doc'):
                    obj._bruno_doc['module_path'] = f"{self.app_name}.{module_path}"
                endpoints.append(obj)
        
        # If file has endpoints, create a folder structure matching the module path
        if endpoints:
            relative_path = file_path.relative_to(self.app_path)
            path_parts = list(relative_path.parts)
            if path_parts[-1].endswith('.py'):
                path_parts[-1] = path_parts[-1][:-3]
            
            # Create nested folder structure
            current_path = self.collection_path
            for part in path_parts[:-1]:  # Create intermediate directories
                current_path = os.path.join(current_path, part)
                os.makedirs(current_path, exist_ok=True)
            
            # Create final folder for the module
            final_folder = os.path.join(current_path, path_parts[-1])
            os.makedirs(final_folder, exist_ok=True)
            
            # Process each endpoint
            for func in endpoints:
                self._process_documented_function(func, final_folder)

    def _process_documented_function(self, func: Callable, folder_path: str):
        """Processes a function with bruno decorator and creates .bru file."""
        # Create .bru file
        filename = f"{func.__name__}.bru"
        filepath = os.path.join(folder_path, filename)
        
        content = self._generate_bru_content(func)
        
        with open(filepath, "w") as f:
            f.write(content)
        
        self.sequence_counter += 1

    def _generate_bru_content(self, func: Callable) -> str:
        """Generates content for .bru file."""
        doc = func._bruno_doc
        method = doc.get("method", "post")
        
        # Generate the endpoint path based on the module path and function name
        endpoint_path = f"{doc['module_path']}.{func.__name__}"
        
        content = f"""meta {{
  name: {func.__name__}
  type: http
  seq: {self.sequence_counter}
}}

{method} {{
  url: {{{{base_url}}}}/api/method/{endpoint_path}
  body: multipartForm
  auth: none
}}

body:multipart-form {{"""
        
        # Add body parameters
        for param_name in doc["body"]:
            if param_name.startswith('_'):
                # Parameters starting with underscore are optional
                content += f"\n  ~{param_name[1:]}: "
            else:
                content += f"\n  {param_name}: "
        content += "\n}"
        
        # Add docs if description is present
        if doc["description"]:
            content += f"""

docs {{
  {doc["description"].replace("\n", "\n  ")}
}}"""
        
        return content

@frappe.whitelist(allow_guest=True)
def generate_bruno_collection(module_name: str, docname: str):
    """Endpoint to generate Bruno collection files."""
    generator = BrunoCollectionGenerator(module_name, docname)
    generator.generate_collection()
    return {"message": "Bruno collection generated successfully"}

@frappe.whitelist()
def download_collection(docname):
    """Create and return a zip file of the collection"""
    try:
        # Updated path to include bruno_collections folder
        collection_path = os.path.join(frappe.get_site_path(), "public", "files", "bruno_collections", docname)
        collection_path = os.path.abspath(collection_path)

        if not os.path.exists(collection_path):
            frappe.throw(
                "Collection files not found. Please generate the collection first."
            )
            
        # Create zip file
        zip_filename = f"{docname}.zip"
        zip_path = os.path.join(
            frappe.get_site_path(), "public", "files", zip_filename
        )

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(collection_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, collection_path)
                    zipf.write(file_path, arcname)

        # Get the URL for downloading
        file_url = f"/files/{zip_filename}"

        return {
            "message": "Collection zip created successfully",
            "status": "success",
            "file_url": file_url,
        }

    except Exception as e:
        frappe.log_error("Bruno Collection Download Error", str(e))
        return {"message": f"Error creating zip file: {str(e)}", "status": "error"}