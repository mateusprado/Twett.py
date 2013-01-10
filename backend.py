#!/usr/bin/python
# -*- coding: ascii -*-

import web
from services import Services
from rest import Rest

urls = (
	'/update', 'update')
	
app = web.application(urls, globals(), True)

class update:
	def POST(self):

		status = Rest(web).get_param(param='status')		
		return status

if __name__ == "__main__":
	app.run()