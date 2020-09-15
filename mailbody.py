#!/usr/bin/python3

# Define generic Mail Settings 
user = 'bli'
passwd = 'bla'
header = 'To: bla From:' + user
global body 

# Set approriate Mail Body
class email:
    # When SIM is present
    if True:
        body = 'Automatic SIM Update Finished'
    else:
        body = 'No SIM in tray'

# Send Mail
if True:
    print("send mail " + header + " body: " + email.body)
else:
    print("send mail " + header + " body: " + email.body)

