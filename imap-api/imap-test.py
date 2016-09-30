import sys
import imaplib
import getpass
import email
import email.header
import json
import io

EMAIL_ACC = 'rayray.kim@mail.utoronto.ca'

Account = imaplib.IMAP4_SSL('outlook.office365.com') 

try:
	emailAddress = raw_input('What is your email address?: ') 
	connectionStatus, data = Account.login(EMAIL_ACC, getpass.getpass())

	# login() returns two strings

except imaplib.IMAP4.error:
	print "You fucked up\n"
    #	print data - data is uninitialized if login fails
	sys.exit(1)

print connectionStatus, data

##
# Try getting the names of mailboxes and dumping into a json file
##

connectionStatus, mailboxes = Account.list()
if connectionStatus == 'OK':
	boxList = open('mailboxes.txt', 'w')
	boxList.write('Mailboxes: \n')
	boxList.write(str(mailboxes))
	

Account.logout()

print "logging out... return 0\n"

sys.exit(0)
