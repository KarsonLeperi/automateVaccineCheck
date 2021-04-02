import secret
import time

#Load personal data (template available for filling in)
info = secret.PersonalData()
# add data formatting check (proper email, proper state abreviation, correct data types)

#set up while loop. runs python file for costco check and vaxxmax check. breaks when it finds a solution
t0 = time.time()
elapsed_time = 0

while elapsed_time < info.max_runtime:
	elapsed_time = time.time() - t0
	time.sleep(info.sleeptime)
		

#create message and send to text, email, or terminal
if success == True:
	message_body = f"Vaccine appointment available at {store}, in {City}. {URL}"
else:
	message_body = "No Luck. Try Again.

if info.notification.lower() == "text":
	message = info.client.messages.create(body = message_body, 
										  from_ = info.message_from,
										  to = info.message_t0)
	message.sid
	
elif info.notification.lower() == "email":
	server = smtplib.SMTP(info.smtp_server, info.smtp_port)
	server.starttls()
	server.login(info.email_acct, info.email.pwd)
	email_message = F"Subject: {info.email_subject}\n\n{message_body}"
	server.sendmail(info.email_acct, info.to_email. email_message)
	
else:
	print(message_body)