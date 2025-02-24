
  ## Bruno Collection Generator for Frappe Developers


This Frappe app streamlines the process of generating API collections in the [Bruno](https://www.usebruno.com/) format directly from your Frappe application. Bruno is a lightweight, fast, and open-source API client designed for developers. Unlike Postman, Bruno stores your collections directly in a folder on your filesystem. This Frappe app integrates with Bruno by using the `@bruno` decorator to document your API endpoints and a "Bruno Collection" doctype to define collection metadata. This allows for a simplified workflow to keep your API documentation and testing in sync and easily shareable.

### Key Features

*   **Decorator-Based Documentation:** Document API endpoints directly in your Frappe code using the `@bruno` decorator.
*   **Frappe-Integrated Collection Management:** Define and manage Bruno collections using the "Bruno Collection" doctype within your Frappe site.
*   **Automated Generation:** Automatically generates Bruno collection files based on decorated endpoints within the selected module and collection settings.
*   **Downloadable Collection:** Download the generated Bruno collection as a zip file.
*    **Easy Integration with Bruno:**  The generated collection is ready to be used directly by Bruno, without the need for importing a format like Postman's.

### Installation

1.  **Install the Frappe App:**

    ```bash
    bench get-app https://github.com/royalsmb/frappe_doc
    bench install-app frappe_doc
    bench migrate
    ```

2.  **Install Bruno:** Download and install the Bruno API client from [https://www.usebruno.com/](https://www.usebruno.com/).

### Usage: A Step-by-Step Guide

#### 1. Decorate Your API Endpoints

Use the `@bruno` decorator to mark your Frappe API endpoints.  Make sure you document the endpoint clearly using a docstring, as this will populate the description in Bruno.

**Example:**

```python
import frappe
from frappe_doc import bruno

@frappe.whitelist(allow_guest=True)
@bruno(method="post")
def create_customer(name: str, email: str, phone: str):
    """
    Creates a new customer in the system.
    Requires the customer's name, email, and phone number.
    """
    new_customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": name,
        "email_id": email,
        "phone": phone
    }).insert()
    return {"message": f"Customer {new_customer.name} created successfully"}

@frappe.whitelist()
@bruno() #defaults to GET
def get_current_time():
    """
    Returns the current server time.
    """
    return {"current_time": frappe.utils.now()}
```

#### 2. Create a Bruno Collection Document

1.  In your Frappe site, navigate to the "Bruno Collection" doctype.
2.  Click "Add New" to create a new "Bruno Collection" document.
3.  Fill in the required fields:

    *   **Collection Name:**  A descriptive name for your Bruno collection.

        *   **Example:** `My App - API v1`

    *   **Module:** Select the Frappe module containing the `@bruno` decorated endpoints you want to include in the collection. The app will scan the files within this module for endpoints. You are selecting the Module Def (e.g. My App).

        *   **Example:** If your API endpoints are in the Awesome App module, select Awesome App.
        *   **Important:** You are selecting the Module Def, not the Python module.

    *   **Base URL:** Enter the base URL of your Frappe site.

        *   **Example (Development):** `http://localhost:8000`
        *   **Example (Production):** `https://your-frappe-site.com`

4.  Save the "Bruno Collection" document.

#### 3. Generate and Download the Bruno Collection

1.  Open the "Bruno Collection" document you just created.
2.  Click the "Generate Collection" button. This action triggers the generation of the Bruno collection files. Wait for the success message. If there are any errors, check the Frappe error logs.
3.  Once the collection is generated, click the "Download Collection" button. This will download a zip file to your computer.

#### 4. Open the Collection in Bruno

1.  Open the Bruno application.
2.  Click "Open Collection."
3.  Extract the downloaded zip file and select the *folder* that it contains (the folder with your collection name).

    *   **Important:** Do *not* select the `bruno.json` file or any other individual file within the extracted folder; select the **folder** itself.

4.  Your API endpoints, complete with documentation extracted from the docstrings, will now be available in Bruno. You can test and explore them directly within the Bruno client.

### Examples

*   **Creating a Bruno Collection:**

    *   **Collection Name:** `E-commerce API`
    *   **Module:** `ECommerce`
    *   **Base URL:** `https://ecommerce.example.com`

*   **Decorated Endpoint:**

    ```python
    @frappe.whitelist(allow_guest=True)
    @bruno(method="get")
    def get_product_details(product_id: str):
        """
        Retrieves the details of a specific product.
        Requires the product's ID.
        """
        product = frappe.get_doc("Product", product_id)
        return {
            "name": product.name,
            "description": product.description,
            "price": product.price
        }
    ```

    After generating the collection, Bruno will show an endpoint `get_product_details` with documentation "Retrieves the details of a specific product. Requires the product's ID.". Bruno will also automatically create a `product_id` field in the request's body parameters.

### Troubleshooting

*   **"Generate Collection" button does nothing:** Check the Frappe error logs. Ensure the `@bruno` decorator is used in your code, and the files containing the decorator are within the selected module. Make sure that the Module selected matches the Module the whitelisted method is associated with.
*   **Downloaded zip file is empty:** Ensure the collection was generated successfully before downloading.
*   **Endpoints are missing in Bruno:** Verify the endpoints are decorated with `@bruno`, the correct module is selected in the "Bruno Collection" document, and the docstrings are correctly formatted.
*   **Getting an error when opening the collection in Bruno:** Make sure you are selecting the **folder** containing the collection files, and *not* any of the individual files.
