import frappe
from frappe import _
import subprocess
#configure the system after the app is installed
def before_install():

    #edit the systemsettings doctype
    system_settings = frappe.get_doc("System Settings")
    system_settings.enable_onboarding = 0
    system_settings.time_zone = "Africa/Banjul"
    system_settings.language = "en"
    system_settings.save()

    #edit the website settings doctype
    web_settings = frappe.get_doc("Website Settings")
    web_settings.disable_signup = 1
    # web_settings.website_theme = "Base"
    web_settings.banner_image = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-logo.png"
    web_settings.splash_image = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-icon.png"
    web_settings.favicon = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-icon.png"
    web_settings.footer_logo = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-logo.png"
    web_settings.footer_powered = "Royalsmb"
    web_settings.hide_footer_signup = 1
    web_settings.app_name = "Royalsmb"
    web_settings.app_logo = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-icon.png"
    web_settings.save()

    #navbar settings
    navbar = frappe.get_doc("Navbar Settings")
    navbar.app_logo = "https://eu2.contabostorage.com/c1174160a74e4cd5969819a60bf2fad7:royalsmb-files/royalsmb-logo.png"
    navbar.logo_width = 200
    navbar.save()
#create site on submit
