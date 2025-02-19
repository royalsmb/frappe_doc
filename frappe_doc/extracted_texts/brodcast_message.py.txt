# Copyright (c) 2024, royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import today
from pywa import WhatsApp
from pywa.types import Template as Temp

class BrodcastMessage(Document):
	def validate(self):
		self.send_template()
	# 	if self.header_type != "TEXT" and not self.attach:
	# 		frappe.throw(_("Attachment is required for {0} type").format(self.header_type))
		
	def on_submit(self):
		self.send_template()
	def whatsapp_client(self):
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
		return wa
	def send_template(self):
		body = []
		if self.fields:
			for field in self.fields:
				body.append(Temp.TextValue(value=field.field_name))
		lang = ""
		lang_code = frappe.db.get_value("WhatsApp Templates", self.template, "language_code")
		if lang_code == "en":
			lang = Temp.Language.ENGLISH
		elif lang_code == "en_US":
			lang = Temp.Language.ENGLISH_US
		elif lang_code == "en_UK":
			lang = Temp.Language.ENGLISH_UK
		
		if self.header_type == "TEXT" and self.header_value:
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						header=Temp.TextValue(value=self.header_value) if self.header_value else None,
						body=body if body else None,
					),
				)
		elif self.header_type == "IMAGE":
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						header=Temp.Image(image=f"https://web.royalsmb.com{self.attach}")
					),
				)
		elif self.header_type == "DOCUMENT":
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						header=Temp.Document(document=f"https://web.royalsmb.com{self.attach}")
					),
				)
		elif self.header_type == "AUDIO":
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						header=Temp.Audio(audio=f"https://web.royalsmb.com{self.attach}")
					),
				)
		elif self.header_type == "VIDEO":
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						header=Temp.Video(video=f"https://web.royalsmb.com{self.attach}")
					),
				)
		else:
			for contact in self.contacts:
				wa = self.whatsapp_client()
				wa.send_template(
					to=contact.phone,
					template=Temp(
						name=self.template,
						language=lang,
						body=body if body else None,
					),
				)
		
	# def validate(self):
	# 	if self.type == "Text" and not self.message:
	# 		frappe.throw(_("Message is required for Text type"))
	# 	if self.type == "Image" and not self.upload:
	# 		frappe.throw(_("Image is required for Image type"))
	# 	if self.type == "Document" and not self.upload:
	# 		frappe.throw(_("Document is required for Document type"))
	# 	if self.type == "Audio" and not self.upload:
	# 		frappe.throw(_("Audio is required for Audio type"))
	# 	if self.type == "Video" and not self.upload:
	# 		frappe.throw(_("Video is required for Video type"))

	# def on_submit(self):
	# 	if self.type == "Text":
	# 		self.send_message()
	# 	elif self.type == "Image":
	# 		self.send_image()
	# 	elif self.type == "Document":
	# 		self.send_document()
	# 	elif self.type == "Audio":
	# 		self.send_audio()
	# 	elif self.type == "Video":
	# 		self.send_video()
	# 	else:
	# 		self.send_message()
	
	# def send_message(self):
	# 	wa = self.whatsapp_client()
	# 	# remove the plus sign from the phone number
	# 	for contact in self.contacts:
	# 		wa.send_message(
	# 			to=contact.phone,
	# 			text=self.message,
	# 			preview_url=True,
	# 		)

	# def send_image(self):
	# 	wa = self.whatsapp_client()
	# 	for contact in self.contacts:
	# 		wa.send_image(
	# 			to=contact.phone,
	# 			image=f"http://173.212.196.39:4021{self.upload}",
	# 			caption=self.message,
	# 		)

	# def send_document(self):
	# 	wa = self.whatsapp_client()
	# 	for contact in self.contacts:
	# 		wa.send_document(
	# 			to=contact.phone,
	# 			document=f"http://173.212.196.39:4021{self.upload}",
	# 			filename = self.get_document_name(),
	# 			caption=self.message,
	# 		)

	# def send_audio(self):
	# 	wa = self.whatsapp_client()
	# 	for contact in self.contacts:
	# 		wa.send_audio(
	# 			to=contact.phone,
	# 			audio=self.upload,
	# 		)
	# def send_video(self):
	# 	wa = self.whatsapp_client()
	# 	for contact in self.contacts:
	# 		wa.send_video(
	# 			to=contact.phone,
	# 			video=self.uplod,
	# 			caption=self.message,
	# 		)
	# def get_document_name(self):
	# 	file = frappe.get_doc("File", {"file_url": self.upload})
	# 	return file.file_name

