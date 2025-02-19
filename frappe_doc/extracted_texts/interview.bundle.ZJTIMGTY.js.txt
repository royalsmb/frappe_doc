(() => {
  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/interview_feedback.html
  frappe.templates["interview_feedback"] = `<div class="feedback-section col-xs-12">
	{% if feedbacks.length %}
	<h4 class="my-4 mx-5" style="font-size: 18px">
		{{ __("Overall Average Rating") }}
	</h4>
	{%=
		frappe.render_template(
			"feedback_summary",
			{ number_of_stars: 5, average_rating: average_rating, feedback_count: feedbacks.length, reviews_per_rating: reviews_per_rating }
		)
	%}

	<div class="m-5">
		<h4 class="mb-2" style="font-size: 18px">{{ __("Feedback Summary") }}</h4>
		<p class="mb-5 text-secondary">
			{{ __("Average rating of demonstrated skills") }}
		</p>
		<div class="row">
			{% for(const d of skills_average_rating) { %}
			<div class="col-md-4 mb-4">
				{%= frappe.render_template("circular_progress_bar", {skill: d.skill, rating: d.rating * 5}) %}
			</div>
			{% } %}
		</div>
	</div>
	{% } %}

	{%= frappe.render_template("feedback_history", { feedback_history: feedbacks, feedback_doctype: "Interview Feedback" }) %}
</div>
`;

  // frappe-html:/home/frappe/frappe-bench/apps/hrms/hrms/public/js/templates/circular_progress_bar.html
  frappe.templates["circular_progress_bar"] = `<div class="circular-progress mx-auto mb-3">
	{% degree = Math.floor(rating*360/5) %}
	{% deg_right = degree > 180 ? 180 : degree %}
	{% deg_left = degree > 180 ? degree - 180 : 0 %}
	<span class="progress-left" style="--deg-left: {{ deg_left }}deg">
		<span class="progress-bar" style="border-color: var(--gray-600)"></span>
	</span>
	<span class="progress-right" style="--deg-right: {{ deg_right }}deg">
		<span class="progress-bar" style="border-color: var(--gray-600)"></span>
	</span>
	<div class="progress-value">{{ flt(rating, 2) }}</div>
</div>
<h5 class="text-center">{{ skill }}</h5>
`;
})();
//# sourceMappingURL=interview.bundle.ZJTIMGTY.js.map
