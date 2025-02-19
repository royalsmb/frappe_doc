import frappe
from frappe.utils import getdate
@frappe.whitelist()
def get_teams(date: str, court: str, time_slot: dict):
    try:
        date = getdate(date)
        start_time = time_slot.get("start_time")
        end_time = time_slot.get("end_time")
        if not frappe.db.exists("Court Schedule", {"court": court, "date": date, "start_time": start_time, "end_time": end_time}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid court schedule"
            })
            return

        court_schedule = frappe.get_doc("Court Schedule", {"court": court, "date": date, "start_time": start_time, "end_time": end_time}, ["court", "start_time", "end_time"])
        teams = frappe.get_all("Team", {"slot": court_schedule.get("name")}, ["name", "team_leader", "players_count", "status"])
        data = []
        for team in teams:
            team_doc = frappe.get_doc("Team", team.get("name"))
            data.append({
                "team_id": team.get("name"),
                "team_leader": team.get("team_leader"),
                "players_count": team.get("players_count"),
                "time_slot":{
                    "start_time": court_schedule.get("start_time"),
                    "end_time": court_schedule.get("end_time"),
                },
                "status": team.get("status"),
            })
            frappe.local.response.update({
                "http_status_code": 200,
                "message": "Teams fetched successfully",
                "data": data
            })
    except Exception as e:
        frappe.log_error(f"Error fetching teams: {str(e)[:100]}", "Get Teams")
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })

@frappe.whitelist()
def join_team(team_id:str, player_id:str):
    try:
        if not frappe.db.exists("Team", team_id):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Invalid team"
            })
            return
        team = frappe.get_doc("Team", team_id)
        if frappe.db.exists("Team Players", {"parent": team_id, "player_id": player_id}):
            frappe.local.response.update({
                "http_status_code": 400,
                "error": "Player already in team"
            })
            return
        team.append("team_players", {
            "player_id": player_id
        })
        team.save()
        frappe.db.commit()
        data = {
            "team_id": team_id,
            "leader": team.team_leader,
            "players_count": team.players_count,
            "time_slot": {
                "start_time": frappe.get_value("Court Schedule", team.slot, "start_time"),
                "end_time": frappe.get_value("Court Schedule", team.slot, "end_time"),
            },
            
        }
        frappe.local.response.update({
            "http_status_code": 200,
            "message": "Joined team successfully",
            "data": data
            
        })
    
    except Exception as e:
        frappe.log_error(f"Error joining team: {str(e)}", "Join Team")
        frappe.clear_messages()
        frappe.local.response.update({
            "http_status_code": 400,
            "error": str(e)
        })