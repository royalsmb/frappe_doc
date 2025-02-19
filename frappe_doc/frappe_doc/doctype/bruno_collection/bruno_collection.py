import frappe
import os
import shutil
import zipfile
import inspect
import json
import functools
from frappe.model.document import Document
from pathlib import Path
from typing import Dict, List, Optional, Callable
# import scrub
from frappe import scrub
from frappe_doc import bruno

class BrunoCollection(Document):
    def get_collection_path(self) -> str:
        """Get the path where collection files will be stored"""
        return os.path.join(
            frappe.get_site_path(),
            "public",
            "files",
            self.name,
        )
    

@frappe.whitelist(allow_guest=True)
@bruno()
def get_bruno_collections(hearder: str):
    """Get list of Bruno collections."""
    return frappe.get_all("Bruno Collection", fields=["name", "collection_name", "module", "base_url"])
# class BrunoCollectionGenerator():
#     """Bruno collection generator for Frappe Framework applications."""

#     def __init__(self, app_name: str):
#         self.app_name = app_name
#         self.app_path = frappe.get_app_path(app_name)
#         self.collection_path = os.path.join(self.app_path, "bruno_collections")
#         self.sequence_counter = 1
#         self.settings = frappe.get_single("Bruno Settings")  # Assuming a "Bruno Settings" doctype exists

#     def generate_collection(self):
#         """Generates Bruno collection files."""
#         if not self.settings.enabled:
#             frappe.throw("Bruno documentation generation is disabled. Please enable it in Bruno Settings.")

#         # Create collections directory if it doesn't exist
#         os.makedirs(self.collection_path, exist_ok=True)

#         # Create bruno.json file
#         self._create_bruno_json()

#         # Create collection.bru file
#         self._create_collection_file()

#         # Scan for API endpoints and create collection files
#         for path in Path(self.app_path).rglob("*.py"):
#             if not str(path.relative_to(self.app_path)).startswith((".", "_")):
#                 self._analyze_file(path)

#     def _create_bruno_json(self):
#         """Creates the bruno.json configuration file."""
#         bruno_config = {
#             "version": "1",
#             "name": "bruno_collections",
#             "type": "collection",
#             "ignore": [
#                 "node_modules",
#                 ".git"
#             ]
#         }

#         with open(os.path.join(self.collection_path, "bruno.json"), "w") as f:
#             json.dump(bruno_config, f, indent=2)

#     def _create_collection_file(self):
#         """Creates the collection.bru file with environment variables."""
#         collection_content = f"""meta {{
#   name: {self.app_name.capitalize()}
# }}

# auth {{
#   mode: none
# }}

# vars:pre-request {{
#   base_url: {self.settings.base_url}
# }}"""

#         with open(os.path.join(self.collection_path, "collection.bru"), "w") as f:
#             f.write(collection_content)

#     def _analyze_file(self, file_path: Path):
#         """Analyzes a Python file for API endpoints."""
#         module_name = str(file_path.relative_to(self.app_path)).replace('/', '.').replace('.py', '')

#         try:
#             module = frappe.get_module(f"{self.app_name}.{module_name}")
#         except ImportError as e:
#             frappe.log_error(f"ImportError: Could not import module {self.app_name}.{module_name}: {e}") # Add log
#             return

#         for name, obj in inspect.getmembers(module):
#             if inspect.isfunction(obj) and hasattr(obj, '_bruno_doc'):
#                 self._process_documented_function(obj)

#     def _process_documented_function(self, func: Callable):
#         """Processes a function with bruno decorator and creates .bru file."""
#         # Create .bru file
#         filename = f"{func.__name__}.bru"
#         filepath = os.path.join(self.collection_path, filename)

#         content = self._generate_bru_content(func)

#         with open(filepath, "w") as f:
#             f.write(content)

#         self.sequence_counter += 1

#     def _generate_bru_content(self, func: Callable) -> str:
#         """Generates content for .bru file."""
#         doc = func._bruno_doc
#         method = doc.get("method", "post")

#         # Generate the endpoint path based on the module path and function name
#         endpoint_path = f"{doc['module_path']}.{func.__name__}"

#         content = f"""meta {{
#   name: {func.__name__}
#   type: http
#   seq: {self.sequence_counter}
# }}

# {method} {{
#   url: {{{{base_url}}}}/api/method/{endpoint_path}
#   body: multipartForm
#   auth: none
# }}

# body:multipart-form {{"""

#         # Add body parameters
#         for param_name in doc["body"]:
#             if param_name.startswith('_'):
#                 # Parameters starting with underscore are optional
#                 content += f"\n  ~{param_name[1:]}: "
#             else:
#                 content += f"\n  {param_name}: "
#         content += "\n}"

#         # Add docs if description is present
#         if doc["description"]:
#             content += f"""

# docs {{
#   {doc["description"].replace("\n", "\n  ")}
# }}"""

#         return content

# @frappe.whitelist(allow_guest=True)
# def generate_collection(docname: str):
#     """Endpoint to generate Bruno collection files."""
#     module_name = frappe.get_value("Bruno Collection", docname, "module")
#     generator = BrunoCollectionGenerator(module_name)  # Replace 'frappe_doc' with your app's name
#     generator.generate_collection()
#     return {"message": "Bruno collection generated successfully"}
# #     def validate(self):
# #         """Validate the document before saving"""
# #         # Ensure collection name is valid for filesystem
# #         self.collection_name = "".join(
# #             c for c in self.collection_name if c.isalnum() or c in (" ", "-", "_")
# #         ).strip()

# #     def get_collection_path(self) -> str:
# #         """Get the path where collection files will be stored"""
# #         return os.path.join(
# #             frappe.get_site_path(),
# #             "public",
# #             "files",
# #             "bruno_collections",
# #             self.name,
# #         )

# #     def before_save(self):
# #         """Reset collection status if important fields are changed"""
# #         if (
# #             self.has_value_changed("module")
# #             or self.has_value_changed("base_url")
# #         ):
# #             self.collection_status = "Not Generated"


# # class BrunoCollectionGenerator:
# #     """Bruno collection generator for specific modules."""

# #     def __init__(self, app_name: str, module_name: str, base_url: str, collection_path: str):
# #         self.app_name = app_name
# #         self.module_name = module_name
# #         self.base_url = base_url
# #         self.collection_path = collection_path
# #         self.module_path = self._get_module_path()
# #         self.sequence_counter = 1

# #         print(f"BrunoCollectionGenerator initialized with:")
# #         print(f"  app_name: {self.app_name}")
# #         print(f"  module_name: {self.module_name}")
# #         print(f"  base_url: {self.base_url}")
# #         print(f"  collection_path: {self.collection_path}")
# #         print(f"  module_path: {self.module_path}")

# #     def _get_module_path(self) -> str:
# #         """Get the absolute path to the module directory"""
# #         app_path = frappe.get_app_path(self.app_name)
# #         module_dir = self.module_name.lower().replace(" ", "_")
# #         return os.path.join(app_path, module_dir)

# #     def generate_collection(self):
# #         """Generates Bruno collection files."""
# #         if not os.path.exists(self.module_path):
# #             frappe.throw(f"Module directory not found: {self.module_path}")

# #         # Create bruno.json file
# #         self._create_bruno_json()

# #         # Create collection.bru file
# #         self._create_collection_file()

# #         # Scan for API endpoints in the module
# #         for path in Path(self.module_path).rglob("*.py"):
# #             rel_path = path.relative_to(self.module_path)
# #             if not str(rel_path).startswith((".", "_")):
# #                 self._analyze_file(path)

# #     def _create_bruno_json(self):
# #         """Creates the bruno.json configuration file."""
# #         bruno_config = {
# #             "version": "1",
# #             "name": self.module_name,
# #             "type": "collection",
# #             "ignore": ["node_modules", ".git"],
# #         }

# #         with open(os.path.join(self.collection_path, "bruno.json"), "w") as f:
# #             json.dump(bruno_config, f, indent=2)

# #     def _create_collection_file(self):
# #         """Creates the collection.bru file with environment variables."""
# #         collection_content = f"""meta {{
# #   name: {self.module_name}
# # }}

# # auth {{
# #   mode: none
# # }}

# # vars:pre-request {{
# #   base_url: {self.base_url}
# # }}"""

# #         with open(os.path.join(self.collection_path, "collection.bru"), "w") as f:
# #             f.write(collection_content)

# #     def _analyze_file(self, file_path: Path):
# #         """Analyzes a Python file for API endpoints."""
# #         try:
# #             # Get relative path from module root
# #             rel_path = file_path.relative_to(self.module_path)
# #             module_parts = list(rel_path.parts[:-1])  # Get directory structure
# #             file_name = rel_path.stem  # Get filename without extension

# #             # Build the module import path
# #             module_import_path = (
# #                 f"{self.app_name}.{self.module_name.lower().replace(' ', '_')}"
# #             )
# #             if module_parts:
# #                 module_import_path += "." + ".".join(module_parts)
# #             module_import_path += f".{file_name}"

# #             print(f"Attempting to import module: {module_import_path}")  # DEBUG

# #             # Import the module
# #             module = frappe.get_module(module_import_path)

# #             # Find API endpoints in the module
# #             api_endpoints = [
# #                 obj
# #                 for name, obj in inspect.getmembers(module)
# #                 if inspect.isfunction(obj) and hasattr(obj, "_bruno_doc")
# #             ]

# #             print(f"API endpoints found: {api_endpoints}")  # DEBUG

# #             if api_endpoints:
# #                 # Create directory structure mirroring the module
# #                 if module_parts:
# #                     dir_path = os.path.join(
# #                         self.collection_path, *module_parts, file_name
# #                     )
# #                 else:
# #                     dir_path = os.path.join(self.collection_path, file_name)

# #                 os.makedirs(dir_path, exist_ok=True)

# #                 # Create bruno.json for this directory
# #                 self._create_directory_bruno_json(dir_path, file_name)

# #                 # Process each API endpoint
# #                 for func in api_endpoints:
# #                     self._process_documented_function(func, dir_path)

# #         except ImportError as e:
# #             frappe.log_error(f"Error importing module {module_import_path}: {str(e)}")
# #         except Exception as e:
# #             frappe.log_error(f"Error analyzing file {file_path}: {str(e)}")

# #     def _create_directory_bruno_json(self, dir_path: str, dir_name: str):
# #         """Creates a bruno.json file for a directory."""
# #         bruno_config = {
# #             "version": "1",
# #             "name": dir_name,
# #             "type": "collection",
# #         }

# #         with open(os.path.join(dir_path, "bruno.json"), "w") as f:
# #             json.dump(bruno_config, f, indent=2)

# #     def _process_documented_function(self, func: Callable, dir_path: str):
# #         """Processes a function with bruno decorator and creates .bru file."""
# #         filename = f"{func.__name__}.bru"
# #         filepath = os.path.join(dir_path, filename)

# #         content = self._generate_bru_content(func)

# #         with open(filepath, "w") as f:
# #             f.write(content)

# #         self.sequence_counter += 1

# #     def _generate_bru_content(self, func: Callable) -> str:
# #         """Generates content for .bru file."""
# #         doc = func._bruno_doc
# #         method = doc.get("method", "post")

# #         # Generate the endpoint path based on the module path and function name
# #         endpoint_path = f"{doc['module_path']}.{func.__name__}"

# #         content = f"""meta {{
# #   name: {func.__name__}
# #   type: http
# #   seq: {self.sequence_counter}
# # }}

# # {method} {{
# #   url: {{{{base_url}}}}/api/method/{endpoint_path}
# #   body: multipartForm
# #   auth: none
# # }}

# # body:multipart-form {{"""

# #         # Add body parameters
# #         for param_name in doc["body"]:
# #             if param_name.startswith("_"):
# #                 # Parameters starting with underscore are optional
# #                 content += f"\n  ~{param_name[1:]}: "
# #             else:
# #                 content += f"\n  {param_name}: "
# #         content += "\n}"

# #         # Add docs if description is present
# #         if doc["description"]:
# #             content += f"""

# # docs {{
# #   {doc["description"].replace("\n", "\n  ")}
# # }}"""

# #         return content


# # @frappe.whitelist()
# # def generate_collection(docname):
# #     """Generate Bruno collection files"""
# #     try:
# #         doc = frappe.get_doc("Bruno Collection", docname)
# #         collection_path = doc.get_collection_path()

# #         # Clear existing collection if any
# #         if os.path.exists(collection_path):
# #             shutil.rmtree(collection_path)

# #         # Create new collection directory
# #         os.makedirs(collection_path, exist_ok=True)

# #         # Initialize generator with the collection path
# #         generator = BrunoCollectionGenerator(
# #             app_name=scrub(doc.module),
# #             module_name=doc.module,
# #             base_url=doc.base_url,
# #             collection_path=collection_path,
# #         )

# #         # Generate collection
# #         generator.generate_collection()

# #         # Update document status
# #         doc.collection_status = "Generated"
# #         doc.save()

# #         return {"message": "Collection generated successfully", "status": "success"}

# #     except Exception as e:
# #         frappe.log_error("Bruno Collection Generation Error", str(e))
# #         return {"message": f"Error generating collection: {str(e)}", "status": "error"}


# # @frappe.whitelist()
# # def download_collection(docname):
# #     """Create and return a zip file of the collection"""
# #     try:
# #         doc = frappe.get_doc("Bruno Collection", docname)
# #         collection_path = doc.get_collection_path()

# #         if not os.path.exists(collection_path):
# #             frappe.throw(
# #                 "Collection files not found. Please generate the collection first."
# #             )

# #         # Create zip file
# #         zip_filename = f"{doc.collection_name}.zip"
# #         zip_path = os.path.join(
# #             frappe.get_site_path(), "public", "files", zip_filename
# #         )

# #         with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
# #             for root, dirs, files in os.walk(collection_path):
# #                 for file in files:
# #                     file_path = os.path.join(root, file)
# #                     arcname = os.path.relpath(file_path, collection_path)
# #                     zipf.write(file_path, arcname)

# #         # Get the URL for downloading
# #         file_url = f"/files/{zip_filename}"

# #         return {
# #             "message": "Collection zip created successfully",
# #             "status": "success",
# #             "file_url": file_url,
# #         }

# #     except Exception as e:
# #         frappe.log_error("Bruno Collection Download Error", str(e))
# #         return {"message": f"Error creating zip file: {str(e)}", "status": "error"}

