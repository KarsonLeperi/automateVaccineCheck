class PersonalData:
	"This is the personal data"
	webdriver= "Test"
	sleeptime = 60     # This is the time between different checks of the website. The website only refreshes every minute so the minimum should be 60
	max_distance = 150
	state = "OR"
	zipcode = 97005
	notification = "email"   # Choose text, email, or none
	max_runtime = 300     # max run time for the program to run and attempt to find a slot
	urls = ['http://vaxxmax.com/cvs',
        'http://vaxxmax.com/walgreens',
        'http://vaxxmax.com/riteaid']
		#,
		#'http://vaxxmax.com/walmart']
		
	safeway_url = "https://www.mhealthappointments.com/covidappt"

	#Email Settings
	#You might need to allow less secure apps to work https://myaccount.google.com/lesssecureapps
	email_acct =          # email address to use (recommend to use gmail, otherwise you will need to update the smtp_server variable)
	email_pwd =	      # password for email address above
	email_recepient =     # email to send the alert to (can use the same email as email_acct
	email_subject = "Alert"
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	
	#Text Message Settings
	# for this feature to work, you will need to create an account on twilio. They will provide you with the account_sid, auth_token, and message_from (phone number) variable.
	from twilio.rest import Client
	

	account_sid =       # get from Twilio
	auth_token =        # Get from Twilio
	client = Client(account_sid, auth_token)
	message_from =      # Get from Twilio
	message_to=	    # Personal phone number

	
	def __init__(self):
		pass
