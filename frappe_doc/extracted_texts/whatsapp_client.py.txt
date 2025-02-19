
from frappe.utils.data import today
from pywa import WhatsApp
import frappe
from frappe import _
from pywa.types import NewTemplate
from pywa import WhatsApp, utils
from pywa.types.media import MediaUrlResponse
import json


wa_doc = frappe.get_doc("WhatsApp Settings", "WhatsApp Settings")
wa = WhatsApp(
    phone_id = wa_doc.phone_id,
    token = wa_doc.get_password('token'),
    server=None,  # Not using Flask
    callback_url='173.212.196.39:4021/api/method/royalsmb.whatsapp_integration.whatsapp_client.webhook',
    verify_token="royalsmb",
    app_id=wa_doc.app_id,
    app_secret=wa_doc.get_password('app_secret'),
    business_account_id=wa_doc.business_account_id
)


@frappe.whitelist()
def get_rul():
    id = "973922577842969"
    media_response = wa.get_media_url(media_id=id)
    
    # Extract relevant attributes
    media_data = {
        "url": media_response.url,
        "mime_type": media_response.mime_type,
        "file_size": media_response.file_size
        # Add more attributes as needed
    }
    
    # Serialize to JSON
    return json.dumps(media_data)
@frappe.whitelist()
def download_media():
    return wa.download_media(
        url='https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=973922577842969&ext=1721231119&hash=ATvCyIBzeAtLFe-qnTwxuAPNCyItEzRz_NlEVP1CbNvHqQ',
        path='',
        filename='image.jpg',)

@frappe.whitelist(allow_guest=True)
def send_message(message, phone_number):
    wa.send_message(
        to=phone_number,
        text=message,
        preview_url=True,
    )
@frappe.whitelist(allow_guest=True)
def send_image(image_url, phone_number, message=None):
    wa.send_image(
        to=phone_number,
        url=image_url,
        caption=message,
    )

@frappe.whitelist(allow_guest=True)
def send_document(document_url, phone_number, message=None):
    wa.send_document(
        to=phone_number,
        url=document_url,
        caption=message,
    )

@frappe.whitelist(allow_guest=True)
def send_audio(audio_url, phone_number, message=None):
    wa.send_audio(
        to=phone_number,
        url=audio_url,
        caption=message,
    )
@frappe.whitelist(allow_guest=True)
def send_video(video_url, phone_number, message=None):
    wa.send_video(
        to=phone_number,
        url=video_url,
        caption=message,
    )
@frappe.whitelist(allow_guest=True)
def create_template():
    wa.create_template(
        template=NewTemplate(
            name='helos',
            category=NewTemplate.Category.UTILITY,
            language=NewTemplate.Language.ENGLISH_US,
            header=NewTemplate.Text('The New iPhone {15} is here!'),
            body=NewTemplate.Body('Buy now and use the code {WA_IPHONE_15} to get {15%} off!'),
            footer=NewTemplate.Footer('Powered by khan')
        ),
    )
@frappe.whitelist(allow_guest=True)
def send_template():
    from pywa.types import Template as Temp
    wa.send_template(
        to='2203611704',
            template=Temp(
            name='hello_world',
            language=Temp.Language.ENGLISH_US,
            header=None,
            body=None
           
        ),
    )
    return "Template sent successfully"

@frappe.whitelist(allow_guest=True)
def my_challenge_handler():
    req = frappe.request
    challenge = req.args.get('hub.challenge')
    if challenge:
        return challenge
    else:
        frappe.throw(_("Missing challenge parameter"))
