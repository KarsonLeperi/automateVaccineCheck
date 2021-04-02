class PersonalData:
	"This is the personal data"
	webdriver= "Test"
	sleeptime = 6
	max_distance = 150
	state = "OR"
	notification = "Text"   # Choose Text, Email, or none
	max_runtime = 60
	urls = ['http://vaxxmax.com/cvs',
        'http://vaxxmax.com/walgreens',
        'http://vaxxmax.com/riteaid']

	#Email Settings
	email_acct = "karsonleperipython@gmail.com"
	email_pwd = "ThisIsATestPythonPassword"
	email_recepient = "karsonleperi@gmail.com"
	email_subject = "Alert"
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	
	#Text Message Settings
	#from twilio.ret import Client
	
	account_sid = "you acc ID"
	auth_token = "your token"
#	client = Client(account_sid, auth_token)
	message_from = "+1*******+"
	message_t0="+12405958160"
	
	def __init__(self):
		pass