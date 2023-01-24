# Copyright (c) 2022, opex and contributors
# For license information, please see license.txt

import threading

import frappe
from frappe.model.document import Document

class OpEx4(Document):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		print('in constructor')
		
		# delayedCall = threading.Timer(5, self.add_realtime_events)
		# delayedCall.start()
		# self.add_realtime_events()

	def add_realtime_events(self):
		print('events')
		frappe.connect()
		frappe.publish_realtime('show_popup',
							{'task_id': 1, 'foo': 'bar'},
							user=frappe.session.user)