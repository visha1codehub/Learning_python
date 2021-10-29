# def adding():
#     a = int(input("1st number"))
#     b = int(input("2nd number"))
#     print(a+b)


# def subtracting():
#     c = int(input("1st number"))
#     d = int(input("2nd number"))
#     print(c-d)
    
# def multiplying():
#     e = int(input("1st number"))
#     f = int(input("2nd number"))
#     print(e*f)
    
    
# def dividing():
#     g = int(input("1st number"))
#     h = int(input("2nd number"))
#     print(g/h)

# adding()
# subtracting()
# multiplying()
# dividing()

# def greet(name):
#     print("Hello",name)
#     print("You are welcome")
# greet('Vishal')
# python script for sending message update

import time
from time import sleep
from sinchsms import SinchSMS

# function for sending SMS
def sendSMS():

	# enter all the details
	# get app_key and app_secret by registering
	# a app on sinchSMS
	number = 9695077615
	app_key = 123564
	app_secret = 'VishalDhannu'

	# enter the message to be sent
	message = 'Hello Message!!!'

	client = SinchSMS(app_key, app_secret)
	print("Sending '%s' to %s" % (message, number))

	response = client.send_message(number, message)
	message_id = response['messageId']
	response = client.check_status(message_id)

	# keep trying unless the status retured is Successful
	while response['status'] != 'Successful':
		print(response['status'])
		time.sleep(1)
		response = client.check_status(message_id)

	print(response['status'])

if __name__ == "__main__":
    sendSMS()
