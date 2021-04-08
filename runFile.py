import secret
import time
import websiteCheck
import smtplib

#Load personal data (template available for filling in)
info = secret.PersonalData()
# add data formatting check (proper email, proper state abreviation, correct data types)

#set up while loop. runs python file for costco check and vaxxmax check. breaks when it finds a solution
t0 = time.time()
elapsed_time = 0

while elapsed_time < info.max_runtime:
	[vaxMax, costco, safeway, success_costco, success_vaxMax, success_safeway] = websiteCheck.webCheck(info)
	if success_costco or success_vaxMax:
		break
	elapsed_time = time.time() - t0
	time.sleep(info.sleeptime)
		

#create message and send to text, email, or terminal. 
#AS of last check, costco pharmacy website is down. Removed from reporting
values = vaxMax.iloc[0]
store = values['store']
City = values['city']
distance = values['distance']
if store == "cvs":
	URL = info.urls[0]
elif store == "walgreens":
	URL = info.urls[1]
elif store == "rite-aid":
	URL = info.urls[2]
else:
	URL = "error"
if success_vaxMax == True and success_safeway == True:
	message_body = f"Vaccine appointment available at {store}, in {City}, {distance} miles away. {URL}. Also, Safeway, {safeway[0]}. {info.safeway_url}"
elif success_vaxMax == True and success_safeway == False:
	message_body = f"Vaccine appointment available at {store}, in {City}, {distance} miles away. {URL}."
elif success_vaxMax == False and success_safeway == True:
	message_body = f"Vaccine appointment available at Safeway, {safeway[0]}. {info.safeway_url}"
else:
	message_body = "No Luck. Try Again."

if info.notification.lower() == "text":
	message = info.client.messages.create(body = message_body, 
										  from_ = info.message_from,
										  to = info.message_to)
	message.sid
	
elif info.notification.lower() == "email":
	server = smtplib.SMTP(info.smtp_server, info.smtp_port)
	server.ehlo()
	server.starttls()
	server.login(info.email_acct, info.email_pwd)
	email_message = f"Subject: {info.email_subject}\n\n{message_body}"
	server.sendmail(info.email_acct, info.email_recepient, email_message)
	server.quit()
	
else:
	print(message_body)