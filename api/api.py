# -*- coding: ascii -*-

import oauth2 as oauth

class Api:	
	
	def __init__(self, auth):		
		self.auth = auth
		
	def update(self, status):
		client = oauth.Client(self.auth.consumer, self.auth.token)
		resp, content = client.request(
	      	'http://api.twitter.com/1/statuses/update.rss?status='+status,
	        method='POST')
	
	def direct_message(self, to, text):
		client = oauth.Client(self.auth.consumer, self.auth.token)
		resp, content = client.request(
			'http://api.twitter.com/1/direct_messages/new.rss?screen_name='+to+'&text='+text,
			method='POST')