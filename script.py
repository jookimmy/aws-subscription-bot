import schedule
import time
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com')
	server.ehlo()
except:
	print('Could not establish a connection to server')

username = 'messages@gmail.com'
password = 'password'

FROM = username
TO = 'joo199@gmail.com'
ME = 'joo199@gmail.com'
SUBJECT = 'Daily Subcription Message'

messages_bank = {}

mefile = open('tokens.txt', 'r')
file = mefile.read().split("\n")
mefile.close()
count = 0
for i in range(0,len(file)):
	if file[i] != '':
		messages_bank[count] = file[i]
		count+=1

token_number = random.randint(0, 730) % len(messages_bank)
print("Count of Messages: %s" % len(messages_bank))
print(messages_bank)
message = messages_bank.pop(0) + ('\n' * 2) + 'Thank you!' + '\n-Joowon'

last_day = ""
if len(messages_bank) == 0:
	last_day = "Today's message is the last one! Thanks so much for subscribing to this mailing list :)"

email = """\
From: Message Bot <%s>
To: %s
Subject: %s

Message Day: %s
%s

%s
""" % (FROM, TO, SUBJECT, 61 - len(messages_bank), last_day, message)
message_type = "Text"

newfile = open('tokens.txt', 'w')
for message in messages_bank:
	if messages_bank[message] != '':
		newfile.write('%s\n' % messages_bank[message])
newfile.close()

try:
	server.login(username, password)
	server.sendmail(FROM, TO, email)
	server.sendmail(FROM, ME, "Sent Today's Message")
	server.close()

except:
	print('Email could not be sent')


print("Count of Messages: %s" % len(messages_bank))
print(email)
