#!/usr/bin/python3
import os.path

# Define Logfile 
logpath = 'pymail.log'

# Check if Logfile is present
if os.path.isfile(logpath):
    # Open file in append-mode
    log = open(logpath, "a")
else:
    # Create file 
    log = open(logpath, "w+")
    log.write("Creating new File!\n")

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

# "Send Mail" - write it to the log
log.write("send mail " + header + " body: " + email.body + "\n")

log.close()

