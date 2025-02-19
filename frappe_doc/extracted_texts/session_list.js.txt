frappe.listview_settings['Session'] = {
    // add_fields: ["status", "produciton_item", "weight", "qty","produced_qty", "planned_start_date", "expected_delivery_date"],
    filters: [["status", "!=", "Cancelled"]],
  get_indicator: function(doc) {
    if(doc.status==="Submitted") {
      return [__("Open"), "orange", "status,=,Submitted"];
    } else {
      return [__(doc.status), {
        "Draft": "red",
        "Open": "orange",
        "Closed": "green",
        "Cancelled": "red"
      }[doc.status], "status,=," + doc.status];
    }
  }//*/
  };