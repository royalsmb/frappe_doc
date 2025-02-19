# Copyright (c) 2024, royalsmb and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from pywa import WhatsApp
import frappe

class WM(Document):
	def validate(self):
		if self.type == "Text" and not self.message:
			frappe.throw(_("Message is required for Text type"))
		if self.type == "Image" and not self.upload:
			frappe.throw(_("Image is required for Image type"))
		if self.type == "Document" and not self.upload:
			frappe.throw(_("Document is required for Document type"))
		if self.type == "Audio" and not self.upload:
			frappe.throw(_("Audio is required for Audio type"))
		if self.type == "Video" and not self.upload:
			frappe.throw(_("Video is required for Video type"))

	def after_insert(self):
		if self.type == "Text":
			self.send_message()
		elif self.type == "Image":
			self.send_image()
		elif self.type == "Document":
			self.send_document()
		elif self.type == "Audio":
			self.send_audio()
		elif self.type == "Video":
			self.send_video()
		else:
			self.send_message()
	def whatsapp_client(self):
		wa = WhatsApp(
					phone_id="281222978402210",
					token="EAAlXQfMg4WYBOwXInAXRL6DRosO4cYhW8EupZAkel5bxJPbZAnMipygBWTzZAfx9KRPEZBgdZCIvObMOoeaZBuCo24t1TMNo1fGZCjnuQ53OxE9NshZC4UoZCfb4zFwuYLtYJQOB3k10duBtZCszTWW3NcPiaW8yUL97WizKDSAqUmRJLpLcausksZBBARtIQ2XCk6j",
					server=None,  # Not using Flask
					callback_url='173.212.196.39:4021/api/method/royalsmb.whatsapp_integration.whatsapp_client.webhook',
					verify_token="royalsmb",
					app_id='2629215553904998',
					app_secret="f317faaff962b2b1d5c0c73d35d31080",
				)
		return wa

	def send_message(self):
		wa = self.whatsapp_client()
		# remove the plus sign from the phone number
		wa.send_message(
			to=self.to,
			text=self.message,
			preview_url=True,
		)
	def send_image(self):
		wa = self.whatsapp_client()
		wa.send_image(
			to=self.to,
			image=f"http://173.212.196.39:4021{self.upload}",
			caption=self.message,
		)

	def send_document(self):
		wa = self.whatsapp_client()
		wa.send_document(
			to=self.to,
			document=f"http://173.212.196.39:4021{self.upload}",
			filename = self.get_document_name(),
			caption=self.message,
		)

	def send_audio(self):
		wa = self.whatsapp_client()
		wa.send_audio(
			to=self.to,
			audio=self.upload,
		)
	def send_video(self):
		wa = self.whatsapp_client()
		wa.send_video(
			to=self.to,
			video=self.uplod,
			caption=self.message,
		)
	def get_document_name(self):
		file = frappe.get_doc("File", {"file_url": self.upload})
		return file.file_name
