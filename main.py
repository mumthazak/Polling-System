from flask import Flask
from public import public
from admin import admin
from district import district
from booth import booth
from candidates import candidates
from voters import voters

import smtplib      
from email.mime.text import MIMEText
from flask_mail import Mail


app=Flask(__name__)
app.secret_key="abc"


mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'projectsriss2020@gmail.com'
app.config['MAIL_PASSWORD'] = 'messageforall'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(district,url_prefix="/district")
app.register_blueprint(booth,url_prefix="/booth")
app.register_blueprint(candidates,url_prefix="/candidates")
app.register_blueprint(voters,url_prefix="/voters")
app.run(debug=True,port=5002)