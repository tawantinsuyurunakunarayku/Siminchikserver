import smtplib

def sendEmail(fromaddr,password,toaddrs,message):
	
	fromaddr = fromaddr
	toaddrs  = toaddrs
	msg = message
 
	username = fromaddr
	password = password

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()