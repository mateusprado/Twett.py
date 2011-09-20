# -*- coding: ascii -*-

class Rest:

	def __init__(self, web):
		self.web = web

	def get_param(self, param):
		data = self.web.input()

		return data.param