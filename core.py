import qrcode
import cv2
import numpy as np
import uuid
import hashlib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

def get_hashed_value(string):
	string = hashlib.sha224(string.encode()).hexdigest()
	return str(string)
def generate_private_key():
	pass
	return str(uuid.uuid4())
def generate_qr_code(string):
	path = "qr_codes/" + str(uuid.uuid4()) + ".png"
	img = qrcode.make(string)
	img.save(path)
	return path
def sent_mail(to,sub,message,image = None):
	import smtplib
	gmail_user = ''  
	gmail_password = ''
	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		msg = MIMEMultipart()
		if image:
			msg.attach(MIMEImage(open(image,"rb").read()))
		msg.attach(MIMEText(message,"plain"))
		server.sendmail(gmail_user, to, msg.as_string())
		server.close()
		return True

	except Exception as e:  
		print (e)
		return False
