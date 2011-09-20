# Twett-py

# How to use?

# Update status
	Services().update(status='Your status here')
# Send direct message
	Services().direct_message(to='diegomnarducci', text='a message')
	
# Web Client
	$ python frontend.py
	curl -d "status=Your new Status" -X POST http://0.0.0.0:8080/update