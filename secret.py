class PersonalData:
	"This is the personal data"
	webdriver= "Test"
	sleeptime = 60
	max_distance = 150
	state = "OR"
	notification = "email"   # Choose text, email, or none
	max_runtime = 300
	urls = ['http://vaxxmax.com/cvs',
        'http://vaxxmax.com/walgreens',
        'http://vaxxmax.com/riteaid',
		'http://vaxxmax.com/walmart']

	#Email Settings
	email_acct = 
	email_pwd =
	email_recepient = 
	email_subject = "Alert"
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	
	#Text Message Settings
	from twilio.rest import Client
	
	account_sid = 
	auth_token = 
	client = Client(account_sid, auth_token)
	message_from = 
	message_to=
	
	def __init__(self):
		pass