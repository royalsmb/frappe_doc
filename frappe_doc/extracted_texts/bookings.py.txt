import frappe
from datetime import datetime, timedelta
from frappe.utils import getdate, cint, today, flt, validate_email_address
import razorpay
import frappe
from datetime import datetime, timedelta, date
import json
from frappe.types import DF
from frappe.utils import getdate, nowdate
from frappe import FrappeTypeError
from dinks.config import validate_request_params 
from inspect import signature
from dinks.v1.config import create_customer

@frappe.whitelist()
def create_booking(
            court: str,
            date: date,
            start_time: str,
            end_time: str,
            players_count: int = 1,
            team_id: str = None
            ):
    """Create a court booking for a specific court, date, and time schedule."""
    try:
        # Check if court is already booked
        existing_booking = frappe.get_all(
            "Court Schedule",
            {"court": court, "date": date, "start_time": start_time, "end_time": end_time},
        )
        if existing_booking:
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Court is already booked for the selected time and date"
            })
            return

        # Ensure customer exists or create one
        if not frappe.db.exists("Customer", {"email": frappe.session.user}):
            full_name = frappe.db.get_value("User", frappe.session.user, "full_name")
            create_customer(full_name, frappe.session.user) 
        customer = frappe.get_doc("Customer", {"email": frappe.session.user})

        # Create Booking
        booking = frappe.new_doc("Booking")
        booking.customer = customer.name
        booking.court = court
        booking.date = date
        booking.start_time = start_time
        booking.end_time = end_time
        booking.players = players_count
        booking.team_id = team_id
        booking.insert()
        booking.submit()
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Booking created successfully.",
            "data": {
                "court": court,
                "date": date,
                "start_time": start_time,
                "end_time": end_time,
                "players": players_count,
                "team_id": team_id
            }
        })
    except Exception as e:
        frappe.log_error(f"Error creating booking: {str(e)}", "Create Booking")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })





@frappe.whitelist()
def booking_pass(
        date: str,
        email: str,
        court: str,
        team_id: str = None

        ):
    try:   
              
        validate_request_params(allowed_params=set(signature(booking_pass).parameters.keys()))
        date = getdate(date)
        if not validate_email_address(email):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid email address."
            })
            return

        

        if not frappe.db.exists("Court", court):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid court."
            })
            return

        if team_id and not frappe.db.exists("Team", team_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid team."
            })
            return

        

        if not frappe.db.exists("Booking", {"court": court, "date": date}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid booking."
            })
            return

        booking = frappe.get_doc("Booking", {"court": court, "date": date})
        booking = frappe.get_doc("Booking", {"court": court, "date": date, "team_id": team_id}) if team_id else booking
        team = frappe.get_doc("Team", team_id) if team_id else None
        

        data = {
            "email_id": email,
            "booking_id": booking.name,
            "court_id": court,
            "date": date,
            "location_id": frappe.db.get_value("Court Schedule", {"booking": booking.name}, "location") or "",
            "team_id": team_id,
            "total_players": team.players_count if team else booking.players,
            "booking_person": booking.customer,
            "start_time": frappe.get_value("Court Schedule", {"booking":booking.name}, "start_time"),
            "end_time": frappe.get_value("Court Schedule", {"booking":booking.name}, "end_time"),
            "pay_at_court": True if booking.pay_at_court else False
            }    
        
        
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Confirmed booking pass",
            "data": data
        })
    except Exception as e:
        frappe.log_error(f"Error confirming booking pass: {str(e)}", "Booking Pass")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def booking_history():
    user_id = frappe.session.user
    try:
        court_bookings = frappe.get_all("Booking", {"owner": user_id})
        event_bookings = frappe.get_all("Event Registration", {"owner": user_id})
        court_data = []
        event_data = []
        for booking in court_bookings:
            doc = frappe.get_doc("Booking", booking.name)
            if not frappe.db.exists("Court", doc.court):
                continue
            court = frappe.get_doc("Court", doc.court)
            location = frappe.get_doc("Location", court.location)
            court_data.append({
                "booking_id": doc.name,
                "court_name": doc.court,
                "location": location.name,
                "date": doc.date,
                "time": f"{doc.start_time} - {doc.end_time}",
                "image_url": frappe.utils.get_url(location.thumbnail),
                "location_address_url": location.address_url,
                "players": doc.players,
                "customer": doc.customer
        
            })
        frappe.local.response.update({
            "http_status_code": 200,
            "data": court_data
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
    
@frappe.whitelist()
def modify_booking(booking_id: str, new_date: str = None, new_time_slot: dict = None):
    try:
        if not frappe.db.exists("Booking", booking_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid booking ID"
            })
            return
        start_time = new_time_slot.get("start_time")
        end_time = new_time_slot.get("end_time")
        if frappe.db.exists("Booking", {"date": new_date, "start_time": start_time, "end_time": end_time}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "The Selected timeis already booked"
            })
            return


        booking = frappe.get_doc("Booking", booking_id)
        if new_date:
            frappe.db.set_value("Booking", booking_id, "date", new_date)
        if new_time_slot:
            frappe.db.set_value("Booking", booking_id, "start_time", start_time)
            frappe.db.set_value("Booking", booking_id, "end_time", end_time)
        frappe.db.commit()
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Booking modified successfully",
            "new_booking_details": {
                "booking_id": booking_id,
                "court": booking.court,
                "date": new_date,
                "start_time": start_time,
                "end_time": end_time
            }
        })
    except Exception as e:
        frappe.log_error(f"Error modifying booking: {str(e)}", "Modify Booking")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def cancel_booking(booking_id:str):
    try:
        if not frappe.db.exists("Booking", booking_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid booking ID"
            })
            return
        booking = frappe.get_doc("Booking", booking_id)
        booking.cancel()
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Booking cancelled successfully",
            "refund":"A refund of 100% will be processed in 7 business days"
        })
    except Exception as e:
        frappe.log_error(f"Error cancelling booking: {str(e)}", "Cancel Booking")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def view_court_details(court_id):
    if not frappe.db.exists("Court", court_id):
        frappe.local.response.update({
            "http_status_code": 400,
            "error": "Invalid court ID"
        })
        return
    court = frappe.get_doc("Court", court_id)
    location = frappe.get_doc("Location", court.location)
    facilites = frappe.get_all("Location Facilities", {"parent": location.name}, pluck="facility_name")
    no_of_indoor_courts = frappe.db.count("Court", {"location": location.name, "court_type": "Indoor"})
    no_of_outdoor_courts = frappe.db.count("Court", {"location": location.name, "court_type": "Outdoor"})

    frappe.local.response.update({
        "http_status_code": 200,
        "data": {
            "court_id": court.name,
            "court_name": court.court_name,
            "location": location.location_name,
            "image_url": frappe.utils.get_url(location.thumbnail),
            "location_address_url": location.address_url,
            "full_address": location.address,
            "no_of_indoor_courts": no_of_indoor_courts,
            "no_of_outdoor_courts": no_of_outdoor_courts,
            "facilities": facilites
        }
    })