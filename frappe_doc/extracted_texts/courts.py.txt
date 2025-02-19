import frappe
from frappe.utils import getdate, nowdate
from datetime import datetime, timedelta

# Helper Functions
@frappe.whitelist()
def get_days(start_date: str, days: int = 30):
    """Generate a list of dates from the given start_date for the next `days` days."""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    return [(start + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]

def is_email_valid(email: str):
    """Validate if the provided email address is valid."""
    return frappe.utils.validate_email_address(email)

def fetch_schedules(court: str):
    """Fetch all schedules for a specific court."""
    return frappe.get_all(
        "Court Schedule",
        filters={"court": court},
        fields=["start_time", "end_time", "date"]
    )

# API Functions
@frappe.whitelist()
def get_next_30_days():
    """Get a list of the next 30 days starting from today."""
    frappe.local.response.update({
        "http_status_code": 200,
        "data": get_days(start_date=nowdate(), days=30)
    })
@frappe.whitelist()
def get_location_booked_slots(location:str, date:str):
    try:
        data = []
        morning_slots = frappe.get_all("Time Slots", {"slot_category": "Morning"}, pluck='name')
        afternoon_slots = frappe.get_all("Time Slots", {"slot_category": "Afternoon"}, pluck='name')
        evening_slots = frappe.get_all("Time Slots", {"slot_category": "Evening"}, pluck='name')
        schedules = frappe.get_all("Court Schedule", {"location": location, "date": date}, ["date", "start_time", "end_time"])
        booked_slots = []
        for schedule in schedules:
            start_time = schedule.get("start_time")
            end_time = schedule.get("end_time")
            booked_slots.append({
                "start_time": start_time,
                "end_time": end_time
            })
        

        frappe.local.response.update({
            "http_status_code": 200,
            "date": date,
            "data": {
                "all_slots": {
                    "morning_slots": morning_slots,
                    "afternoon_slots": afternoon_slots,
                    "evening_slots": evening_slots
                },
                "booked_slots": booked_slots
            }
        })
    except Exception as e:
        frappe.log_error(f"Error fetching booked slots: {str(e)}", "Get Booked Slots")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def get_available_courts(date: str, time_slot: dict):
    """Fetch courts that are available on a specific date and time schedule."""
    try:
        date = getdate(date)
        all_courts = frappe.get_all("Court", fields=["*"])
        indoor_courts = []
        outdoor_courts = []
        start_time = time_slot.get("start_time")
        end_time = time_slot.get("end_time")
        for court in all_courts:
            schedules = fetch_schedules(court.name)
            
            if frappe.db.exists("Court Schedule", {"court": court.name, "date": date, "start_time": start_time, "end_time": end_time}):
                if court.court_type == "Indoor":
                    indoor_courts.append({
                        "court_id": court.name,
                        "court_name": court.court_name,
                        "is_available": False
                    })
                else:
                    outdoor_courts.append({
                        "court_id": court.name,
                        "court_name": court.court_name,
                        "is_available": False
                    })
                
            else:
                if court.court_type == "Indoor":
                    indoor_courts.append({
                        "court_id": court.name,
                        "court_name": court.court_name,
                        "is_available": True
                    })
                else:
                    outdoor_courts.append({
                        "court_id": court.name,
                        "court_name": court.court_name,
                        "is_available": True
                    })
                
        frappe.local.response.update({
            "http_status_code": 200,
            "data": {
                "indoor_courts": indoor_courts,
                "outdoor_courts": outdoor_courts
            }
        })

    except Exception as e:
        frappe.log_error(f"Error fetching available courts: {str(e)}", "Get Available Courts")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def create_booking(court: str, date: str, time_schedules: str, customer_name: str, email: str):
    """Create a court booking for a specific court, date, and time schedule."""
    if not is_email_valid(email):
        frappe.local.response.update({
            "http_status_code": 400,
            "error": "Invalid email address."
        })
        return

    try:
        # Check if court is already booked
        existing_booking = frappe.get_all(
            "Court Schedule",
            filters={"court": court, "date": date, "time_schedules": ("like", f"%{time_schedules}%")},
        )
        if existing_booking:
            ffrappe.local.response.update({
                "http_status_code": 400,
                "error": "Court is already booked for the selected time."
            })
            return

        # Ensure customer exists or create one
        customer = frappe.db.get_value("Customer", {"email_id": email}, "name")
        if not customer:
            customer_doc = frappe.get_doc({
                "doctype": "Customer",
                "customer_name": customer_name,
                "email_id": email,
                "customer_type": "Individual",
                "customer_group": "Individual",
                "territory": "All Territories"
            })
            customer_doc.insert()
            frappe.db.commit()
            customer = customer_doc.name


        # Create Booking
        booking = frappe.get_doc({
            "doctype": "Court Schedule",
            "court": court,
            "date": date,
            "time_schedules": time_schedules,
            "customer": customer
        })
        booking.insert()
        frappe.db.commit()

        frappe.local.response.update({
            "http_status_code": 200,
            "data": "Booking created successfully."
        })

    except Exception as e:
        frappe.log_error(f"Error creating booking: {str(e)}", "Create Booking")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist(allow_guest=True)
def get_everything(location):
    try:
        dates = get_days(location)  # Fetch next 30 days
        schedule_data = []

        # Fetch all courts for the location at once
        courts = frappe.get_all("Location Courts", filters={"court": location}, fields=["name", "court_number", "status"], order_by="court_number")

        for date in dates:
            date_str = date.get("date")
            court_data = []
            for court in courts:
                schedules = frappe.get_all("Court Schedules", filters={"court": location, "date": date_str, "court_number": court.name}, fields=["court_number", "time"])
                # Find if the court has a schedule for the current date
                # scheduled_court = next((s for s in schedules if s.get("court_number") == court.get("name")), None)
                s_data = []
                for s in schedules:
                    if s.get("court_number") == court.get("name"):
                        s_data.append({
                            "time": s.get("time")
                        })
                court_data.append({
                    "court_number": court.get("court_number"),
                    "schedules": s_data
                })
            
            
            schedule_data.append({
                "date": date_str,
                "court_data": court_data
            })

            frappe.local.response.update({
                "http_status_code": 200,
                "data": schedule_data
            })

    except Exception as e:
        frappe.log_error(f"Error fetching courts: {str(e)}", "Get Courts")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist(allow_guest=True)
def get_locations():
    try:
        locations = frappe.get_all("Location")
        data = []
        for loc in locations:
            location = frappe.get_doc("Location", loc.get("name"))
            location_photos = frappe.get_all("Location Photo", {"location": location.get("name")}, ["photo"])
            photos = []
            for photo in location_photos:
                photos.append(frappe.utils.get_url(photo.get("photo")))
            facilities = []
            for facility in location.facilities:
                facilities.append(facility.get("facility_name"))
                
            data.append({
                "name": location.get("name"),
                "location_name": location.get("location_name"),
                "thumbnail": frappe.utils.get_url(location.get("thumbnail")),
                "city": location.city,
                "address": location.get("address"),
                "address_url": location.get("address_url"),
                "full_address": location.get("full_address"),
                "price": location.get("price"),
                "indoor_courts": location.get("indoor_courts"),
                "outdoor_courts": location.get("outdoor_courts"),
                "facilities": facilities,
                "photos": photos
            })

        frappe.local.response.update({
            "http_status_code": 200,
            "data": data
        })
    except Exception as e:
        frappe.log_error(f"Error fetching locations: {str(e)}", "Get Locations")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })


@frappe.whitelist()
def get_court_schedules():
    form_data = frappe.request.get_json()
    date = form_data.get("date")
    location = form_data.get("location")
    time_slot = form_data.get("time_slot")
    start_time = time_slot.get("start_time")
    end_time = time_slot.get("end_time")


    court_schedules = frappe.get_list("Court Schedule", {"location": location, "date": date, "start_time": start_time, "end_time": end_time}, ["court", "start_time", "end_time"])
    schedules = []
    for schedule in court_schedules:
        if schedule.get("start_time") == start_time or schedule.get("end_time") == end_time:
            schedules.append({
                "court": schedule.get("court"),
                "start_time": schedule.get("start_time"),
                "end_time": schedule.get("end_time")
            })
    courts = frappe.get_all("Court", {"location": location}, ["name", "court_name", "court_type"])
    indoor_courts = []
    outdoor_courts = []
    for court in courts:
        if not any(schedule.get("court") == court.get("name") for schedule in schedules):
            if court.get("court_type") == "Indoor":
                indoor_courts.append({
                    "court_id": court.get("name"),
                    "court_name": court.get("court_name"),
                    "is_available": True
                })
            else:
                outdoor_courts.append({
                    "court_id": court.get("name"),
                    "court_name": court.get("court_name"),
                    "is_available": True
                })

    
    
    frappe.local.response.update({
        "http_status_code": 200,
        "message": "Schedules fetched successfully",
        "data": {
            "indoor_courts": indoor_courts,
            "outdoor_courts": outdoor_courts
        },
        
    })
