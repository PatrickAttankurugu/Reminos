import argparse

import MySQLdb
import requests,urllib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import timedelta
import datetime

# I intend to use flask-SQLAlchemy to interface with the database

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Factory

# HOW FLASK APP WORKS
#All Flask app code is in app.py. As you probably want to host this in the cloud,
# authentication is there from the start.

#This is done by adding the login_required decorator to all private routes. 
#When you go to the app you first have to login

from bdays import get_birthdays
from env import SECRET_KEY

# os module is used to notify user 
import os
import sys




# Birthday file is the one in which the actual birthdays 
# and dates are present

birthdayFile='C:\Users\PATRICK\Desktop\GITHUB PROJECTS\birthdays.csv'

def checkTodaysBirthdays(): 
    fileName = open(birthdayFile, 'r') 
    today = time.strftime('%m%d') 
    flag = 0
    for line in fileName: 
        if today in line: 
            line = line.split(' ') 
            flag =1
            # line[1] contains Name and line[2] contains Surname 
            os.system('notify-send "Birthdays Today: ' + line[1] 
            + ' ' + line[2] + '"') 
    if flag == 0: 
            os.system('notify-send "No Birthdays Today!"') 
  
if __name__ == '__main__': 
    checkTodaysBirthdays()


#This will send an SMS to your configured admin phone. I think we will use Twilio .
#I have no idea whether  Twiliohas an option for configuring a client's phone
# in order for them to receive the birthday wish.Well let's see how it goes...



# Depending on whether I am able to perform all operations with the CSV file and python, I may not perform 
# SQL queries. However, if I am not succesful with only the CSV along with python, I will replace excel with SQL
# Let's see how it goes

class SendEmail(BaseReminder):
    provider = 'GMAIL_CREDENTIALS'

    def __init__(self, bday_guy, *args, **kwargs):
        super(SendEmail, self).__init__(bday_guy, *args, **kwargs)

        self.email_body = self.env.get_template('email_body.html')
        self.email_subject = self.env.get_template('email_subject.html')
        self.toaddr = get_all_emails()

    def gmail_authenticate(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        return server

    def execute(self):
        server = self.gmail_authenticate()
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ", ".join(self.toaddr)
        msg['Subject'] = self.email_subject.render()
        body = self.email_body.render(bday_member=self.bday_guy.name)
        
        #I have to lern SQL for the next 3 days and see whether it will be enough for the project

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(self.username, self.toaddr, text)
        server.quit()




class SendSMS:

	def sendToAdmin():
		pass
  	  	
    
	def sendToClient():
		pass



class SendEmail:
	def SendToAdmin():
		pass



	def SendToClient():
		pass


