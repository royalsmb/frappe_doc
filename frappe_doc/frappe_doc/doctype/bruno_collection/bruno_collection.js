// Copyright (c) 2025, royalsmb and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Bruno Collection", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Bruno Collection', {
    refresh: function(frm) {
        // Add Generate Collection button handler
        if (!frm.is_new()) {
        frm.add_custom_button(__('Generate Collection'), function() {
            frappe.call({
                method: 'frappe_doc.bruno.utils.generate_bruno_collection',
                args: {
                    docname: frm.doc.name,
                    module_name: frm.doc.module
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint({
                            message: __('Collection generated successfully'),
                            indicator: 'green'
                        });
                        
                        frm.reload_doc();
                    } else {
                        frappe.show_alert({
                            title: __('Error'),
                            indicator: 'red',
                            message: r.message.message || __('Error generating collection')
                        });
                    }
                }
            });
        }).addClass('btn-primary');
        
        // Add Download Collection button handler
        // if (frm.doc.collection_status === 'Generated') {
            frm.add_custom_button(__('Download Collection'), function() {
                frappe.call({
                    method: 'frappe_doc.bruno.utils.download_collection',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message && r.message.status === 'success') {
                            window.open(r.message.file_url, '_blank');
                        } else {
                            frappe.msgprint({
                                title: __('Error'),
                                indicator: 'red',
                                message: r.message.message || __('Error downloading collection')
                            });
                        }
                    }
                });
            }).addClass('btn-primary');
        // }
    }
}
});