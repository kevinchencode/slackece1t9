import sys
import imaplib
import getpass
import email
import email.header
import json
import io
import datetime


def process_mails (M):
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print "No messages found!"
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        decode = email.header.decode_header(msg['Subject'])[0]
        subject = unicode(decode[0])
        print 'Message %s: %s' % (num, subject)
        print 'Raw Date:', msg['Date']
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print "Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S")

def process_latest (Account):
	for i in range(5):
		rv, data = Account.uid('search', None, "ALL")
		print 'Email number ' + str(i + 1)
		latest_id = data[0].split()[-(i + 1)]
	
		# fetch email with latest uid with protocol rfc822
		rv, data = Account.uid('fetch', latest_id, '(RFC822)')
		latest_email = data[0][1] # latest email in tuple
		email_message = email.message_from_string(latest_email)
		print 'From: ' + email_message['From']
		print 'Subject ' + email_message['Subject']
		maintype = email_message.get_content_maintype()
		text = ""
		if email_message.is_multipart():
			html = None
			for part in email_message.get_payload():
				if part.get_content_charset() is None:
   		             # We cannot know the character set, so return decoded "something"
					text = part.get_payload(decode=True)
					continue
	
				charset = part.get_content_charset()

				if part.get_content_type() == 'text/plain':
					text = unicode(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')
	
				if part.get_content_type() == 'text/html':
					html = unicode(part.get_payload(decode=True), str(charset), "ignore").encode('utf8', 'replace')

			if text is not None:
				print text.strip()
			elif html is not None:
				print html.strip()
		
		else:
			text = unicode(email_message.get_payload(decode=True), email_message.get_content_charset(), 'ignore').encode('utf8', 'replace')
			print text.strip()	
		
	print '\nThose are all of your emails you fucking small tittied hoe\n'

if __init__ == '__main__':
	Account = imaplib.IMAP4_SSL('outlook.office365.com') 

	try:
		emailAddress = raw_input('What is your email address?: ') #email_address
		connectionStatus, data = Account.login(emailAddress, getpass.getpass())

		# login() returns two strings

	except imaplib.IMAP4.error:
		print "You fucked up"
	    #	print data - data is uninitialized if login fails
		sys.exit(1)

	print connectionStatus, data

	##
	# Try getting the names of mailboxes and dumping into a json file
	##

	connectionStatus, mailboxes = Account.list()
	if connectionStatus == 'OK':
	#use "with statements" to open files so scope is accurate
		##
		# Create a file called mailboxes.txt and create title
		##

		boxList = open('mailboxes.txt', 'w')
		boxList.write('Mailboxes: \n')#don't have this
		boxList.close()

		##
		# Now dump all mailbox info into file in json form
		##

		boxList = open('mailboxes.txt', 'a')
		json.dump(mailboxes, boxList)


		##
		# Append protocol version
		##

		##do not need anymore
		boxList.write('\n\n' + str(Account.PROTOCOL_VERSION))	

		##
		# Process shit!!
		##
		
		#dont need this
		print "Printing mailbox..."
		connectionStatus, data = Account.select("INBOX")
		# process_mails (Account)
		process_latest(Account)
		Account.close()
	else:
		print 'you fucked up m8~\n'

	Account.logout()

	print "logging out... return 0\n"

	sys.exit(0)
