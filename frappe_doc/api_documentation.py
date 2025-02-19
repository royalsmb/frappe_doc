import frappe
import inspect
import json
import functools
from pathlib import Path
from typing import Dict, List, Optional, Callable
import os
from frappe import scrub
def bruno(method="get"):
    """
    Decorator to mark and document API endpoints for Bruno.
    Only accepts HTTP method as a parameter, defaults to POST.
    """
    def decorator(func: Callable) -> Callable:
        # Get the docstring and parameters from the function
        docstring = inspect.getdoc(func) or ""
        parameters = inspect.signature(func).parameters
        
        # Remove self and args/kwargs from parameters
        param_dict = {
            name: ""  # Default empty value for each parameter
            for name, param in parameters.items()
            if name not in ['self', 'args', 'kwargs']
        }
        
        # Get the module path for the function
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
        self.collection_path = frappe.get_site_path('public', 'files', 'bruno_collections', docname)
        self.sequence_counter = 1
        
        
    def generate_collection(self):
        """Generates Bruno collection files."""
        # Create collections directory if it doesn't exist
        os.makedirs(self.collection_path, exist_ok=True)
        
        # Create bruno.json file
        self._create_bruno_json()
        
        # Create collection.bru file
        self._create_collection_file()
        
        # Scan for API endpoints and create collection files
        for path in Path(self.app_path).rglob("*.py"):
            if not str(path.relative_to(self.app_path)).startswith((".", "_")):
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
    
    def _analyze_file(self, file_path: Path):
        """Analyzes a Python file for API endpoints."""
        module_name = str(file_path.relative_to(self.app_path)).replace('/', '.').replace('.py', '')
        
        try:
            module = frappe.get_module(f"{self.app_name}.{module_name}")
        except ImportError:
            return
            
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and hasattr(obj, '_bruno_doc'):
                self._process_documented_function(obj)
    
    def _process_documented_function(self, func: Callable):
        """Processes a function with bruno decorator and creates .bru file."""
        # Create .bru file
        filename = f"{func.__name__}.bru"
        filepath = os.path.join(self.collection_path, filename)
        
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
def generate_bruno_collection(module_name: str, docname:str):
    """Endpoint to generate Bruno collection files."""
    generator = BrunoCollectionGenerator(module_name, docname)
    generator.generate_collection()
    return {"message": "Bruno collection generated successfully"}

@frappe.whitelist()
def get_file():
    return frappe.get_site_path('public', 'files')