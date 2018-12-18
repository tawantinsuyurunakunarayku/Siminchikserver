
from twilio.rest import Client

# put your own credentials here
ACCOUNT_SID = 'AC4f76765b56dc73b1eef87140334d6bd1'
AUTH_TOKEN = '77aa852263b4b577d1621c43215c3199'

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def sendMessage():

	message = client.messages.create(
	    to="+51940978985", 
	    from_="+13156132282",
	    body="Bienvenido a Quechua ASR")

	print(message.sid)


def addNumber():

	call = client.calls.create(
	    to="+51940978985",
	    from_="+13156132282",
	    url="http://demo.twilio.com/docs/voice.xml"
	)

	print(call.sid)


addNumber()