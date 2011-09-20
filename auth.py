import oauth2 as oauth

class Auth:
	
	def __init__(self):
		self.consumer = oauth.Consumer(key='yourConsumerKey',
	 					   secret='youConsumerSecret')
	
		self.token = oauth.Token(key='yourTokenKey',
	 				 secret='yourTokenSecret')