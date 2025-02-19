(() => {
  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/employees_with_unmarked_attendance.html
  frappe.templates["employees_with_unmarked_attendance"] = `{% if data.length %}

<div class="form-message yellow">
	<div>
		{{
			__(
				"Attendance is pending for these employees between the selected payroll dates. Mark attendance to proceed. Refer {0} for details.",
				["<a href='/app/query-report/Monthly%20Attendance%20Sheet'>Monthly Attendance Sheet</a>"]
			)
		}}
	</div>
</div>

<table class="table table-bordered small">
	<thead>
		<tr>
			<th style="width: 14%" class="text-left">{{ __("Employee") }}</th>
			<th style="width: 16%" class="text-left">{{ __("Employee Name") }}</th>
			<th style="width: 12%" class="text-left">{{ __("Unmarked Days") }}</th>
		</tr>
	</thead>
	<tbody>
		{% for item in data %}
			<tr>
				<td class="text-left"> {{ item.employee }} </td>
				<td class="text-left"> {{ item.employee_name }} </td>
				<td class="text-left"> {{ item.unmarked_days }} </td>
			</tr>
		{% } %}
	</tbody>
</table>

{% } else { %}

<div class="form-message green">
	<div>{{ __("Attendance has been marked for all the employees between the selected payroll dates.") }}</div>
</div>

{% } %}`;

  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/feedback_summary.html
  frappe.templates["feedback_summary"] = `<div class="feedback-summary-section my-4 d-flex">
	<!-- Ratings Summary -->
	<div class="rating-summary-numbers col-3">
		<div class="feedback-count mt-1 mb-2 text-secondary">
			{{ __("Average Rating") }}
		</div>
		<h2 class="average-rating mb-2">{{ average_rating }}</h2>

		{%=
			frappe.render_template("rating",
				{number_of_stars: 5, average_rating: average_rating, for_summary: true}
			)
		%}

		<div class="feedback-count text-secondary mt-2">
			{{ __("based on") }} {{ cstr(feedback_count) }} {{ feedback_count > 1 ? __("reviews") : __("review") }}
		</div>
	</div>

	<!-- Rating Progress Bars -->
	<div class="rating-progress-bar-section pb-0 col-4">
		{% for(let i=5; i>0; i--) { %}
		<div class="row {{ i!=1 && 'mb-3' }}">
			<div class="col-sm-3 text-nowrap flex align-items-center">
				<svg class="icon icon-sm mr-2">
					<use href="#icon-star" class="like-icon"></use>
				</svg>
				<span>{{ i }}</span>
			</div>
			<div class="col-md-7">
				<div
					class="progress rating-progress-bar"
					title="{{ reviews_per_rating[i-1] }} % of reviews are {{ i }} star"
				>
					<div
						class="progress-bar progress-bar-cosmetic"
						role="progressbar"
						aria-valuenow="{{ reviews_per_rating[i-1] }}"
						aria-valuemin="0"
						aria-valuemax="100"
						style="width: {{ reviews_per_rating[i-1] }}%;"
					></div>
				</div>
			</div>
			<div class="col-sm-1 small">{{ reviews_per_rating[i-1] }}%</div>
		</div>
		{% } %}
	</div>
</div>
`;

  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/feedback_history.html
  frappe.templates["feedback_history"] = `<div class="feedback-history mb-3">
	{% if (feedback_history.length) { %}
		{% for (let i=0, l=feedback_history.length; i<l; i++) { %}
			<div class="feedback-content p-3 d-flex flex-row mt-3" data-name="{{ feedback_history[i].name }}">
				<!-- Reviewer Info -->
				<div class="reviewer-info mb-2 col-xs-3">
					<div class="row">
						<div class="col-xs-2">
							{{ frappe.avatar(feedback_history[i].user, "avatar-medium") }}
						</div>
						<div class="col-xs-10">
							<div class="ml-2">
								<div class="title font-weight-bold">
									{{ strip_html(feedback_history[i].reviewer_name || feedback_history[i].user) }}
								</div>
								{% if (feedback_history[i].reviewer_designation) { %}
									<div class="small text-muted">
										{{ strip_html(feedback_history[i].reviewer_designation) }}
									</div>
								{% } %}
							</div>
						</div>
					</div>
				</div>

				<!-- Feedback -->
				<div class="reviewer-feedback col-xs-6">
					<div class="rating">
						{%= frappe.render_template("rating",
								{number_of_stars: 5, average_rating: feedback_history[i].total_score, for_summary: false}
							)
						%}
					</div>
					<div class="feedback my-3">
						{{ feedback_history[i].feedback }}
					</div>
				</div>

				<!-- Feedback Date & Link -->
				<div class="feedback-info col-xs-3 d-flex flex-row justify-content-end align-items-baseline">
					<div class="time small text-muted mr-2">
						{{ frappe.datetime.comment_when(feedback_history[i].added_on) }}
					</div>
					<a href="{{ frappe.utils.get_form_link(feedback_doctype, feedback_history[i].name) }}" title="{{ __("Open Feedback") }}">
						<svg class="icon icon-sm">
							<use href="#icon-link-url"></use>
						</svg>
					</a>
				</div>
			</div>
		{% } %}

	{% } else { %}
		<div class="no-feedback d-flex flex-col justify-content-center align-items-center text-muted">
			<span>{{ __("No feedback has been received yet") }}</span>
		</div>
	{% } %}
</div>`;

  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/rating.html
  frappe.templates["rating"] = `<div class="d-flex flex-col">
	<div class="rating {{ for_summary ? 'ratings-pill' : ''}}">
		{% for (let i = 1; i <= number_of_stars; i++) { %}
			{% if (i <= average_rating) { %}
				{% right_class = 'star-click'; %}
			{% } else { %}
				{% right_class = ''; %}
			{% } %}

			{% if ((i <= average_rating) || ((i - 0.5) == average_rating)) { %}
				{% left_class = 'star-click'; %}
			{% } else { %}
				{% left_class = ''; %}
			{% } %}

			<svg class="icon icon-md" data-rating={{i}} viewBox="0 0 24 24" fill="none">
				<path class="right-half {{ right_class }}" d="M11.9987 3.00011C12.177 3.00011 12.3554 3.09303 12.4471 3.27888L14.8213 8.09112C14.8941 8.23872 15.0349 8.34102 15.1978 8.3647L20.5069 9.13641C20.917 9.19602 21.0807 9.69992 20.7841 9.9892L16.9421 13.7354C16.8243 13.8503 16.7706 14.0157 16.7984 14.1779L17.7053 19.4674C17.7753 19.8759 17.3466 20.1874 16.9798 19.9945L12.2314 17.4973C12.1586 17.459 12.0786 17.4398 11.9987 17.4398V3.00011Z" fill="var(--star-fill)" stroke="var(--star-fill)"/>
				<path class="left-half {{ left_class }}" d="M11.9987 3.00011C11.8207 3.00011 11.6428 3.09261 11.5509 3.27762L9.15562 8.09836C9.08253 8.24546 8.94185 8.34728 8.77927 8.37075L3.42887 9.14298C3.01771 9.20233 2.85405 9.70811 3.1525 9.99707L7.01978 13.7414C7.13858 13.8564 7.19283 14.0228 7.16469 14.1857L6.25116 19.4762C6.18071 19.8842 6.6083 20.1961 6.97531 20.0045L11.7672 17.5022C11.8397 17.4643 11.9192 17.4454 11.9987 17.4454V3.00011Z" fill="var(--star-fill)" stroke="var(--star-fill)"/>
			</svg>
		{% } %}
	</div>
	{% if (!for_summary) { %}
		<p class="ml-3" style="line-height: 2;">
			({{ flt(average_rating, 2) }})
		</p>
	{% } %}
</div>
`;

  // ../hrms/hrms/public/js/utils/index.js
  frappe.provide("hrms");
  $.extend(hrms, {
    proceed_save_with_reminders_frequency_change: () => {
      frappe.ui.hide_open_dialog();
      frappe.call({
        method: "hrms.hr.doctype.hr_settings.hr_settings.set_proceed_with_frequency_change",
        callback: () => {
          cur_frm.save();
        }
      });
    },
    set_payroll_frequency_to_null: (frm) => {
      if (cint(frm.doc.salary_slip_based_on_timesheet)) {
        frm.set_value("payroll_frequency", "");
      }
    },
    get_current_employee: async (frm) => {
      var _a, _b;
      const employee = (_b = (_a = await frappe.db.get_value("Employee", { user_id: frappe.session.user }, "name")) == null ? void 0 : _a.message) == null ? void 0 : _b.name;
      return employee;
    },
    validate_mandatory_fields: (frm, selected_rows, items = "Employees") => {
      const missing_fields = [];
      for (d in frm.fields_dict) {
        if (frm.fields_dict[d].df.reqd && !frm.doc[d] && d !== "__newname")
          missing_fields.push(frm.fields_dict[d].df.label);
      }
      if (missing_fields.length) {
        let message = __("Mandatory fields required for this action:");
        message += "<br><br><ul><li>" + missing_fields.join("</li><li>") + "</ul>";
        frappe.throw({
          message,
          title: __("Missing Fields")
        });
      }
      if (!selected_rows.length)
        frappe.throw({
          message: __("Please select at least one row to perform this action."),
          title: __("No {0} Selected", [__(items)])
        });
    },
    setup_employee_filter_group: (frm) => {
      const filter_wrapper = frm.fields_dict.filter_list.$wrapper;
      filter_wrapper.empty();
      frappe.model.with_doctype("Employee", () => {
        frm.filter_list = new frappe.ui.FilterGroup({
          parent: filter_wrapper,
          doctype: "Employee",
          on_change: () => {
            frm.advanced_filters = frm.filter_list.get_filters().reduce((filters, item) => {
              if (item[3]) {
                filters.push(item.slice(1, 4));
              }
              return filters;
            }, []);
            frm.trigger("get_employees");
          }
        });
      });
    },
    render_employees_datatable: (frm, columns, employees, no_data_message = __("No Data"), get_editor = null, events = {}) => {
      frm.set_df_property("quick_filters_section", "collapsible", 0);
      frm.set_df_property("advanced_filters_section", "collapsible", 0);
      if (frm.employees_datatable) {
        frm.employees_datatable.rowmanager.checkMap = [];
        frm.employees_datatable.options.noDataMessage = no_data_message;
        frm.employees_datatable.refresh(employees, columns);
        return;
      }
      const $wrapper = frm.get_field("employees_html").$wrapper;
      const employee_wrapper = $(`<div class="employee_wrapper">`).appendTo($wrapper);
      const datatable_options = {
        columns,
        data: employees,
        checkboxColumn: true,
        checkedRowStatus: false,
        serialNoColumn: false,
        dynamicRowHeight: true,
        inlineFilters: true,
        layout: "fluid",
        cellHeight: 35,
        noDataMessage: no_data_message,
        disableReorderColumn: true,
        getEditor: get_editor,
        events
      };
      frm.employees_datatable = new frappe.DataTable(employee_wrapper.get(0), datatable_options);
    },
    handle_realtime_bulk_action_notification: (frm, event, doctype) => {
      frappe.realtime.off(event);
      frappe.realtime.on(event, (message) => {
        hrms.notify_bulk_action_status(
          doctype,
          message.failure,
          message.success,
          message.for_processing
        );
        if (message.success)
          frm.refresh();
      });
    },
    notify_bulk_action_status: (doctype, failure, success, for_processing = false) => {
      let action = __("create/submit");
      let action_past = __("created");
      if (for_processing) {
        action = __("process");
        action_past = __("processed");
      }
      let message = "";
      let title = __("Success");
      let indicator = "green";
      if (failure.length) {
        message += __("Failed to {0} {1} for employees:", [action, doctype]);
        message += " " + frappe.utils.comma_and(failure) + "<hr>";
        message += __(
          "Check <a href='/app/List/Error Log?reference_doctype={0}'>{1}</a> for more details",
          [doctype, __("Error Log")]
        );
        title = __("Failure");
        indicator = "red";
        if (success.length) {
          message += "<hr>";
          title = __("Partial Success");
          indicator = "orange";
        }
      }
      if (success.length) {
        message += __("Successfully {0} {1} for the following employees:", [
          action_past,
          doctype
        ]);
        message += __(
          "<table class='table table-bordered'><tr><th>{0}</th><th>{1}</th></tr>",
          [__("Employee"), doctype]
        );
        for (const d2 of success) {
          message += `<tr><td>${d2.employee}</td><td>${d2.doc}</td></tr>`;
        }
        message += "</table>";
      }
      frappe.msgprint({
        message,
        title,
        indicator,
        is_minimizable: true
      });
    },
    fetch_geolocation: async (frm) => {
      if (!navigator.geolocation) {
        frappe.msgprint({
          message: __("Geolocation is not supported by your current browser"),
          title: __("Geolocation Error"),
          indicator: "red"
        });
        hide_field(["geolocation"]);
        return;
      }
      frappe.dom.freeze(__("Fetching your geolocation") + "...");
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          frm.set_value("latitude", position.coords.latitude);
          frm.set_value("longitude", position.coords.longitude);
          await frm.call("set_geolocation");
          frappe.dom.unfreeze();
        },
        (error) => {
          frappe.dom.unfreeze();
          let msg = __("Unable to retrieve your location") + "<br><br>";
          if (error) {
            msg += __("ERROR({0}): {1}", [error.code, error.message]);
          }
          frappe.msgprint({
            message: msg,
            title: __("Geolocation Error"),
            indicator: "red"
          });
        }
      );
    },
    get_doctype_fields_for_autocompletion: (doctype) => {
      const fields = frappe.get_meta(doctype).fields;
      const autocompletions = [];
      fields.filter((df) => !frappe.model.no_value_type.includes(df.fieldtype)).map((df) => {
        autocompletions.push({
          value: df.fieldname,
          score: 8,
          meta: __("{0} Field", [doctype])
        });
      });
      return autocompletions;
    },
    add_shift_tools_button_to_list: (list_view, action = "Assign Shift") => {
      list_view.page.add_inner_button(
        __("Shift Assignment Tool"),
        () => {
          const doc = frappe.model.get_new_doc("Shift Assignment Tool");
          doc.action = action;
          doc.company = frappe.defaults.get_default("company");
          doc.status = "Active";
          frappe.set_route("Form", "Shift Assignment Tool", doc.name);
        },
        __("Shift Tools")
      );
      list_view.page.add_inner_button(
        __("Roster"),
        () => {
          window.location.href = "/hr/roster";
        },
        __("Shift Tools")
      );
    },
    add_shift_tools_button_to_form: (frm, fields) => {
      frm.add_custom_button(
        __("Shift Assignment Tool"),
        () => {
          const doc = frappe.model.get_new_doc("Shift Assignment Tool");
          Object.assign(doc, fields);
          doc.company = frappe.defaults.get_default("company");
          doc.status = "Active";
          frappe.set_route("Form", "Shift Assignment Tool", doc.name);
        },
        __("Shift Tools")
      );
      frm.add_custom_button(
        __("Roster"),
        () => {
          window.location.href = "/hr/roster";
        },
        __("Shift Tools")
      );
    }
  });

  // ../hrms/hrms/public/js/utils/payroll_utils.js
  hrms.payroll_utils = {
    set_autocompletions_for_condition_and_formula: function(frm, child_row = "") {
      const autocompletions = [];
      frappe.run_serially([
        ...["Employee", "Salary Structure", "Salary Structure Assignment", "Salary Slip"].map(
          (doctype) => frappe.model.with_doctype(doctype, () => {
            autocompletions.push(
              ...hrms.get_doctype_fields_for_autocompletion(doctype)
            );
          })
        ),
        () => {
          frappe.db.get_list("Salary Component", {
            fields: ["salary_component_abbr"]
          }).then((salary_components) => {
            autocompletions.push(
              ...salary_components.map((d2) => ({
                value: d2.salary_component_abbr,
                score: 9,
                meta: __("Salary Component")
              }))
            );
            autocompletions.push(
              ...["base", "variable"].map((d2) => ({
                value: d2,
                score: 10,
                meta: __("Salary Structure Assignment field")
              }))
            );
            if (child_row) {
              ["condition", "formula"].forEach((field) => {
                frm.set_df_property(
                  child_row.parentfield,
                  "autocompletions",
                  autocompletions,
                  frm.doc.name,
                  field,
                  child_row.name
                );
              });
              frm.refresh_field(child_row.parentfield);
            } else {
              ["condition", "formula"].forEach((field) => {
                frm.set_df_property(field, "autocompletions", autocompletions);
              });
            }
          });
        }
      ]);
    }
  };

  // ../hrms/hrms/public/js/utils/leave_utils.js
  hrms.leave_utils = {
    add_view_ledger_button(frm) {
      if (frm.doc.__islocal || frm.doc.docstatus != 1)
        return;
      frm.add_custom_button(__("View Ledger"), () => {
        frappe.route_options = {
          from_date: frm.doc.from_date,
          to_date: frm.doc.to_date,
          transaction_type: frm.doc.doctype,
          transaction_name: frm.doc.name
        };
        frappe.set_route("query-report", "Leave Ledger");
      });
    }
  };

  // ../hrms/hrms/public/js/salary_slip_deductions_report_filters.js
  frappe.provide("hrms.salary_slip_deductions_report_filters");
  hrms.salary_slip_deductions_report_filters = {
    filters: [
      {
        fieldname: "company",
        label: __("Company"),
        fieldtype: "Link",
        options: "Company",
        reqd: 1,
        default: frappe.defaults.get_user_default("Company")
      },
      {
        fieldname: "month",
        label: __("Month"),
        fieldtype: "Select",
        reqd: 1,
        options: [
          { value: 1, label: __("Jan") },
          { value: 2, label: __("Feb") },
          { value: 3, label: __("Mar") },
          { value: 4, label: __("Apr") },
          { value: 5, label: __("May") },
          { value: 6, label: __("June") },
          { value: 7, label: __("July") },
          { value: 8, label: __("Aug") },
          { value: 9, label: __("Sep") },
          { value: 10, label: __("Oct") },
          { value: 11, label: __("Nov") },
          { value: 12, label: __("Dec") }
        ],
        default: frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth() + 1
      },
      {
        fieldname: "year",
        label: __("Year"),
        fieldtype: "Select",
        reqd: 1
      },
      {
        fieldname: "department",
        label: __("Department"),
        fieldtype: "Link",
        options: "Department"
      },
      {
        fieldname: "branch",
        label: __("Branch"),
        fieldtype: "Link",
        options: "Branch"
      }
    ],
    onload: function() {
      return frappe.call({
        method: "hrms.payroll.report.provident_fund_deductions.provident_fund_deductions.get_years",
        callback: function(r) {
          var year_filter = frappe.query_report.get_filter("year");
          year_filter.df.options = r.message;
          year_filter.df.default = r.message.split("\n")[0];
          year_filter.refresh();
          year_filter.set_input(year_filter.df.default);
        }
      });
    }
  };
})();
//# sourceMappingURL=hrms.bundle.A6T6RA2E.js.map
