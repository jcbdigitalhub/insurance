# -*- coding: utf-8 -*-
# Copyright (c) 2015, Opensource Solutions Philippines and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class InsuranceCompany(Document):
	pass

	def get_current(self):
		"""get series current"""
		if self.prefix:
			self.current_value = frappe.db.get_value("Series",
				self.prefix, "current")

	def on_update(self):
		"""insert series if missing"""
		prefix = self.prefix
		if not frappe.db.exists('Series', prefix):
			prefix = prefix
			frappe.db.sql("insert into tabSeries (name, current) values (%s, %s)", (prefix,self.current_value))
		else:
			if self.prefix:
				frappe.db.sql("update `tabSeries` set current = %s where name = %s",
					(self.current_value, prefix))

