#!/usr/bin/python3

# Define generic Mail Settings 
user = 'bli'
passwd = 'bla'
header = 'To: bla From:' + user

# Set approriate Mail Body
class email:
    @staticmethod
    def withsim():
        body = 'Automatic SIM Update Finished'

    def withoutsim():
        body = 'No SIM in tray'

# Send Mail
if True:
    email.withsim()
else:
    email.withoutsim()

print("send mail " + header)
