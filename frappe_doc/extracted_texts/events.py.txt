import frappe
from dinks.config import validate_request_params
from inspect import signature

@frappe.whitelist()
def get_events(location: str):
    try:
        validate_request_params(allowed_params=set(signature(get_events).parameters.keys()))
        events = frappe.get_all("Dink Event", {"location":location})
        data = []
        
        for event in events:
            doc = frappe.get_doc("Dink Event", event.name)
            event_facilities = []
            location_facilities = []
            things_to_know = []
            for facility in doc.event_facilities:
                event_facilities.append({
                    "title": facility.title,
                    "sub_title": facility.sub_title
                })
            for facility in doc.location_facilities:
                location_facilities.append(facility.facility_name)
            for things in doc.things_to_keep_in_mind:
                things_to_know.append({
                    "title": things.title,
                    "sub_title": things.sub_title
                })
            
            data.append({
            "event_id": doc.name,
            "event_name": doc.event_name,
            "price": doc.price,
            "date": doc.date,
            "time": f'{doc.from_time} - {doc.to_time}',
            "spots_available": doc.spots_available,
            "image": frappe.utils.get_url(doc.image) or "",
            "event_info": doc.event_info,
            "event_facilities": event_facilities,
            "location_facilities": location_facilities, 
            "things_to_keep_in_mind": things_to_know
            })
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Events fetched successfully",
            "data": data
        })
    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def register_event(event_id:str):
    try:
        validate_request_params(allowed_params=set(signature(register_event).parameters.keys()))
        if not frappe.db.exists("Dink Event", event_id):
            frappe.local.response.update({
            "http_status_code": 400,
            "error": "Invalid Event Id"
            })
            return
        user_id = frappe.session.user
        user_doc = frappe.get_doc("User", user_id)
        user = user_doc.full_name
        mobile = user_doc.mobile_no
        date = frappe.utils.today()
        if frappe.db.exists("Event Registration", {"user_id": user_id, "event": event_id}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "You have already registered for this event"
            })
            return
        booking = frappe.new_doc("Event Registration")
        booking.user_id = user_id
        booking.user = user
        booking.mobile = mobile
        booking.event = event_id
        # booking.players = players
        booking.date = date
        booking.save(ignore_permissions=True)
        booking.submit()
        frappe.db.commit()
        event = frappe.get_doc("Dink Event", event_id)

        frappe.local.response.update({
            "http_status_code": 400,
            "message": "Successfully registered for the event",
            "data": {
                "user_id": user_id,
                "user_name": user,
                "event_booking_id": booking.name,
                "event_id": event_id,
                "event_name": event.event_name,
                "event_location": event.location,
                "price": event.price,
                "date": date,
                "start_time": event.from_time,
                "end_time": event.to_time
                }
            })

    except Exception as e:
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })
