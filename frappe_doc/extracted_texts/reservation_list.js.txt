frappe.listview_settings['Reservation'] = {
    // add_fields: ["status", "produciton_item", "weight", "qty","produced_qty", "planned_start_date", "expected_delivery_date"],
    filters: [["status", "!=", "Cancelled"]],
  get_indicator: function(doc) {
    if(doc.status==="Submitted") {
      return [__("To Check In"), "orange", "status,=,Submitted"];
    } else {
      return [__(doc.status), {
        "Draft": "red",
        "To Check In": "orange",
        "Checked  In": "green",
        "Cancelled": "red"
      }[doc.status], "status,=," + doc.status];
    }
  }//*/
  };