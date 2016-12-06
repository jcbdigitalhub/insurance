// Copyright (c) 2016, Opensource Solutions Philippines and contributors
// For license information, please see license.txt

frappe.ui.form.on('Insurance Company', {
	refresh: function(frm) {},

	onload: function(frm) {
	cur_frm.call('get_current','',function(r){});}
});
