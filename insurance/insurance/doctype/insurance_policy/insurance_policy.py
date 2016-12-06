	# -*- coding: utf-8 -*-
# Copyright (c) 2015, Opensource Solutions Philippines and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import msgprint, throw, _

class InsurancePolicy(Document):
	pass

	def get_amount(self): 
		plan = frappe.db.sql("select * from `tabInsurance Plan` where %s between `from` and `to`",self.area, as_dict=1)
		if plan:
			self.limit_of_liability = plan[0].sum_insured
			self.evat = plan[0].vat
			self.doc_stamp = plan[0].doc_stamp
			self.lgt = plan[0].lgt
			self.connection_fee = plan[0].connection_fee
			self.total = plan[0].total_premium
			self.net_of_premium = plan[0].net_premium
		else:
			msgprint(_("No plan matches found.  Please check the area entered."))
                        self.limit_of_liability = 0
                        self.evat = 0
                        self.doc_stamp = 0
                        self.lgt = 0
                        self.connection_fee = 0
                        self.total = 0
                        self.net_of_premium = 0
