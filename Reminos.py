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


import os
import sys



#This will send an SMS to your configured admin phone. I think we will use Twilio .
#I have no idea whether  Twiliohas an option for configuring a client's phone
# in order for them to receive the birthday wish.Well let's see how it goes...

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


