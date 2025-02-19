frappe.pages['dink'].on_page_load = function(wrapper) {
    new MyPage(wrapper);
}

MyPage = Class.extend({
    init: function(wrapper) {
        this.page = frappe.ui.make_app_page({
            parent: wrapper,
            title: 'Khan',
            single_column: true
        });
        this.make();
    },
    make: function() {
        let me = this;

        // Loop to create 10 widgets
        for (let i = 0; i < 10; i++) {
            let body = `
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">

			
		<div id="sales-widget-${i}" class="card d-inline-block" style="max-width: 300px;">
    <div class="card-header">
        <h5 class="card-title text-truncate" title="Annual Sales ${i}">Annual Sales ${i}</h5>
        <small class="text-muted">Subtitle for Widget ${i}</small>
    </div>
    <div class="card-body d-flex flex-column" style="max-height: 300px; overflow-y: auto;">
        <div class="d-flex justify-content-between align-items-center">
            <div class="number h4 mb-0">GMD ${i * 1000}.00</div>
        </div>
        <!-- Add more content here if necessary -->
    </div>
    <div class="card-footer">
        <!-- Footer content (if needed) -->
    </div>
</div>

            `;
            
            // Append each widget to the page main container
            $(body).appendTo(me.page.main);

            // Add click event for each widget using its unique ID
            $(`#sales-widget-${i}`).on('click', function() {
                me.show_modal(i); // Pass the index to the modal function
            });
        }
    },
    show_modal: function(index) {
        // Define a Frappe modal
        let dialog = new frappe.ui.Dialog({
            title: `Annual Sales Details for Widget ${index}`,
            fields: [
                {
                    label: 'Message',
                    fieldname: 'message',
                    fieldtype: 'HTML',
                    options: `<p>This is the Annual Sales Modal for Widget ${index}.</p>`
                }
            ],
            primary_action_label: 'Close',
            primary_action: function() {
                dialog.hide();
            }
        });

        // Show the modal
        dialog.show();
    }
});
