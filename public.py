from flask import *
from database import*
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
from datetime import *

public=Blueprint('public',__name__)

@public.route('/')
def homepage():
	return render_template("index.html")


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		passs=request.form['psw']
		q="SELECT*FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,passs)
		res=select(q)

		if res:
			if res[0]['login_type']=='admin':
				flash('WELCOME ADMIN')
				return redirect(url_for("admin.admin_home"))

			elif res[0]['login_type']=='candidate':
				flash('WELCOME CANDIDATE')
				q="SELECT * FROM `candidates` WHERE `login_id`='%s'"%(res[0]['login_id'])
				res1=select(q)
				session['cid']=res1[0]['candidate_id']
				return redirect(url_for("candidates.candidates_home"))

			elif res[0]['login_type']=='district':
				q="SELECT * FROM `districts` WHERE `login_id`='%s'"%(res[0]['login_id'])
				res1=select(q)
				session['district_id']=res1[0]['district_id']
				return redirect(url_for("district.district_home"))

			elif res[0]['login_type']=='booth':
				q="SELECT * FROM `booths` WHERE `login_id`='%s'"%(res[0]['login_id'])
				res1=select(q)
				if res1:
					session['booth_id']=res1[0]['booth_id']
					return redirect(url_for("booth.booth_home"))
				else:
					flash("Username Or Password Incorrect")

			elif res[0]['login_type']=='voter':
				flash('WELCOME VOTER')
				q="SELECT * FROM `voters` WHERE `login_id`='%s'"%(res[0]['login_id'])
				res1=select(q)
				session['voter_id']=res1[0]['voter_id']
				return redirect(url_for("voters.voters_home"))




	return render_template("login.html")

@public.route('/candidates_register',methods=['get','post'])
def candidates_register():
	data={}
	q="SELECT * FROM `elections`"
	res=select(q)
	data['election']=res
	q="SELECT * FROM `districts`"
	res=select(q)
	data['dist']=res
	if 'submit' in request.form:
		uname=request.form['uname']
		district=request.form['district']
		passs=request.form['psw']
		election=request.form['election']
		fname=request.form['fname']
		lname=request.form['lname']
		
		dob=request.form['dob']
		place=request.form['place']
		city=request.form['city']
		state=request.form['state']
		pno=request.form['pno']
		email=request.form['email']
		aadhar=request.form['aadhar']
		d= datetime.strptime(dob, '%Y-%m-%d')
		a=datetime.today()
		v=a.year-d.year
		print(v,"...")
		print(d)
		
		
		
		if v<18:
			flash('UNDER AGE')
		else:
			q="SELECT * FROM `candidates` WHERE `aadhar`='%s'"%(aadhar)
			print(q)
			res8=select(q)
			if res8:
				flash('REGISTRATION FAILD BECAUSE AADHAR NUMBER ALREADY EXIST')
			else:
				q="INSERT INTO `login`(`username`,`password`,`login_type`) VALUES('%s','%s','pending')"%(uname,passs)
				login_id=insert(q)
				q="INSERT INTO `candidates` (`login_id`,`election_id`,`first_name`,`last_name`,`age`,`dob`,`place`,`city`,`state`,`phone`,`email`,`candidate_status`,district_id,aadhar) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','pending','%s','%s')"%(login_id,election,fname,lname,v,dob,place,city,state,pno,email,district,aadhar)
				insert(q)
				flash('REGISTERED')
	return render_template("candidates_register.html",data=data)

@public.route('/voter_reg',methods=['get','post'])
def voter_reg():

	data={}
	q="SELECT * FROM `booths`"
	res=select(q)
	data['booth']=res

	
	q="SELECT * FROM `elections`"
	res=select(q)
	data['election']=res

	if 'submit' in request.form:
		booth=request.form['booth']
		election=request.form['election']
		fname=request.form['fname']
		lname=request.form['lname']
		
		dob=request.form['dob']
		place=request.form['place']
		city=request.form['city']
		state=request.form['state']
		phone=request.form['num']
		email=request.form['email']
		uname=request.form['uname']
		passs=request.form['psw']
		aadhar=request.form['aadhar']
		d= datetime.strptime(dob, '%Y-%m-%d')
		a=datetime.today()
		v=a.year-d.year
		print(v,"...")
		print(d)
		
		
		
		if v<18:
			flash('UNDER AGE')
		else:
			q="SELECT * FROM `voters` WHERE `aadhar`='%s'"%(aadhar)
			res8=select(q)
			if res8:
				flash('REGISTRATION FAILD BECAUSE AADHAR NUMBER ALREADY EXIST')
			else:
				q="INSERT INTO `login`(`username`,`password`,`login_type`) VALUES ('%s','%s','voter_pending')"%(uname,passs)	
				login_id=insert(q)

				q="INSERT INTO `voters`(`login_id`,`booth_id`,`election_id`,`first_name`,`last_name`,`age`,`dob`,`place`,`city`,`state`,`phone`,`email`,aadhar)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(login_id,booth,election,fname,lname,v,dob,place,city,state,phone,email,aadhar)
				insert(q)
				flash('REGISTERED')

				try:
					gmail = smtplib.SMTP('smtp.gmail.com', 587)

					gmail.ehlo()

					gmail.starttls()

					gmail.login('projectsriss2020@gmail.com','messageforall')

				except Exception as e:
					print("Couldn't setup email!!"+str(e))

				msg = MIMEText("Your Username is " + uname +" and password is " + passs  )
				# msg = MIMEText("Your password is Haii")

				msg['Subject'] = 'Your Username and Password'

				msg['To'] = email

				msg['From'] = 'projectsriss2020@gmail.com'

				try:

					gmail.send_message(msg)
					print(msg)
					print(email)

				except Exception as e:

					print("COULDN'T SEND EMAIL", str(e))

					# For Message Close

			    # return jsonify({'tasks':"success"})
				return redirect(url_for('public.voter_reg'))
		
	return render_template("voter_reg.html",data=data)