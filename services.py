# -*- coding: ascii -*-

import oauth2 as oauth

from auth import Auth
from api import Api


class Services:
	
	def __init__(self):
		self.auth = Auth()

	def update(self, status):
		Api(self.auth).update(status)			

	def direct_message(self, to, text):
		Api(self.auth).direct_message(to, text)