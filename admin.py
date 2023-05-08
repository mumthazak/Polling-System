from flask import *
from database import*



import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template("admin_home.html")

@admin.route('/admin_count_vote')
def admin_count_vote():
	data={}
	# q="SELECT*FROM`elections`"
	# res=select(q)
	# data['election']=res
	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	eid=request.args['eid']
	# else:
	# 	action=None
	# if action=='count':
	q="SELECT COUNT(`candidate_id`) AS COUNT,`candidates`.`candidate_id`,`election_id`,CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`)AS candname FROM `vote` INNER JOIN `candidates` USING (`candidate_id`) INNER JOIN `elections` USING (`election_id`) GROUP BY `candidate_id`"%(eid)
	res1=select(q)
	data['status']=res1

	return render_template("admin_count_vote.html",data=data)

@admin.route('/admin_manage_booth',methods=['get','post'])
def admin_manage_booth():
	data={}
	q="SELECT * FROM `districts`"
	res=select(q)
	data['dist']=res

	if 'submit' in request.form:
		booth=request.form['booth']
		district=request.form['district']
		uname=request.form['uname']
		passs=request.form['psw']
		q="SELECT * FROM `login` WHERE `username`='%s'"%(uname)
		res5=select(q)
		if res5:
			flash('USERNAME ALREADY EXIST')
			return redirect(url_for('admin.admin_manage_booth'))
		else:
			q="INSERT INTO `login`(`username`,`password`,`login_type`)VALUES('%s','%s','booth')"%(uname,passs)
			log_id=insert(q)
			q="INSERT INTO `booths`(`login_id`,`district_id`,`booth`)VALUES('%s','%s','%s')"%(log_id,district,booth)
			insert(q)

			return redirect(url_for('admin.admin_manage_booth'))

	q="SELECT *,`booths`.`login_id` AS booth_lid FROM `booths` INNER JOIN `districts` USING(`district_id`)"
	res=select(q)
	data['booth']=res


	if 'action' in request.args:
		action=request.args['action']
		bid=request.args['bid']
	else:
		action=None

	if action=='delete':
		q="delete from booths where login_id='%s'"%(bid)
		print(q)
		delete(q)
		q="delete from login where login_id='%s'"%(bid)
		delete(q)
		flash('DELETED')

		return redirect(url_for('admin.admin_manage_booth'))

	if action=='update':
		q="SELECT * FROM `booths` INNER JOIN `districts` USING (`district_id`) WHERE `booths`.`login_id`='%s'"%(bid)
		data['booth_up']=select(q)
	if 'updatez' in request.form:
		booth=request.form['booth']
		district=request.form['district']
		q="UPDATE `booths` SET `district_id`='%s' ,`booth`='%s' WHERE `login_id`='%s'"%(district,booth,bid)
		update(q)
		flash('UPDATED')
		return redirect(url_for('admin.admin_manage_booth'))
	return render_template("admin_manage_booth.html",data=data)
@admin.route('/admin_manage_candidates')
def admin_manage_candidates():
	data={}
	q="SELECT *,candidates.login_id as lids FROM `candidates` INNER JOIN `districts` USING(`district_id`)  INNER JOIN `elections` USING(`election_id`)"
	res=select(q)
	data['candidate']=res
	

	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None
	print(action)
	if action=="accept":
		q="UPDATE `candidates` SET `candidate_status`='accepted' WHERE `login_id`='%s'"%(lid)
		update(q)
		q1="UPDATE `login` SET `login_type`='candidate' WHERE `login_id`='%s'"%(lid)
		update(q1)
		return redirect(url_for('admin.admin_manage_candidates'))
	if action=='reject':
		q="UPDATE `candidates` SET `candidate_status`='rejected' WHERE `login_id`='%s'"%(lid)
		update(q)
		q1="UPDATE `login` SET `login_type`='rejected' WHERE `login_id`='%s'"%(lid)
		update(q1)

		return redirect(url_for('admin.admin_manage_candidates'))
	return render_template("admin_manage_candidates.html",data=data)

@admin.route('/admin_manage_districts',methods=['get','post'])
def admin_manage_districts():
	data={}
	if 'submit'in request.form:
		district=request.form['district']
		uname=request.form['uname']
		passs=request.form['psw']
		q="INSERT INTO `login`(`username`,`password`,`login_type`)VALUES('%s','%s','district')"%(uname,passs)
		log_id=insert(q)
		q="INSERT INTO `districts`(`login_id`,`district`)VALUES('%s','%s')"%(log_id,district)
		insert(q)
	q="SELECT * FROM `districts` "	
	res=select(q)
	data['district']=res


	if 'action' in request.args:
		action=request.args['action']
		did=request.args['did']
	else:
		action=None

	if action=='delete':
		q="delete from districts where login_id='%s'"%(did)
		print(q)
		delete(q)
		q="delete from login where login_id='%s'"%(did)
		delete(q)
		flash('DELETED')
		return redirect(url_for('admin.admin_manage_districts'))

	if action=='update':
		q="SELECT * FROM `districts` WHERE `login_id`='%s'"%(did)
		data['district_up']=select(q)
	if 'updatez' in request.form:
		district=request.form['district']
		q="UPDATE `districts` SET `district`='%s' WHERE `login_id`='%s'"%(district,did)
		update(q)
		flash('UPDATED')
		return redirect(url_for('admin.admin_manage_districts'))
	return render_template("admin_manage_districts.html",data=data)

@admin.route('/admin_manage_elections',methods=['get','post'])
def admin_manage_elections():
	if 'submit' in request.form:
		body=request.form['body']
		edate=request.form['edate']
		ddate=request.form['date']
		q="INSERT INTO `elections` (`body`,`election_date`,`declared_on`,`status`) VALUES('%s','%s','%s','pending')"%(body,edate,ddate)
		insert(q)

	data={}
	q="SELECT * FROM `elections` "	
	res=select(q)
	data['election']=res

	if 'action' in request.args:
		action=request.args['action']
		eid=request.args['eid']
	else:
		action=None
	if action=='started':
		q="UPDATE `elections` SET `status`='started' WHERE `election_id`='%s'"%(eid)
		update(q)
		return redirect(url_for('admin.admin_manage_elections'))
	if action=='completed':
		q="UPDATE `elections` SET `status`='completed' WHERE `election_id`='%s'"%(eid)
		update(q)
		q="INSERT INTO result(candidate_id,total_vote) SELECT candidate_id,COUNT(*) AS total_vote FROM vote  GROUP BY candidate_id ORDER BY total_vote DESC "
		insert(q)	
		# q="SELECT COUNT(`candidate_id`) AS COUNT,`candidates`.`candidate_id`,`election_id`,CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`)AS candname FROM `vote` INNER JOIN `candidates` USING (`candidate_id`) INNER JOIN `elections` USING (`election_id`) WHERE `election_id`='%s' GROUP BY `candidate_id`"%(eid)
		# res1=select(q)
		# for i in range(0,len(res1)):
		# 	q="INSERT INTO`result`(`candidate_id`,`total_vote`) VALUES('%s','%s')"%(res1[i]['candidate_id'],res1[i]['COUNT'])
		# 	insert(q)
		return redirect(url_for('admin.admin_manage_elections'))

	if 'action' in request.args:
		action=request.args['action']
		eid=request.args['eid']
	else:
		action=None

	if action=='delete':
		q="delete from elections where election_id='%s'"%(eid)
		print(q)
		delete(q)
		flash('DELETED')
		return redirect(url_for('admin.admin_manage_elections'))

	if action=='update':
		q="SELECT * FROM `elections` WHERE `election_id`='%s'"%(eid)
		data['election_up']=select(q)
	if 'updatez' in request.form:
		body=request.form['body']
		edate=request.form['edate']
		q="UPDATE `elections` SET `election_date`='%s',body='%s' WHERE `election_id`='%s'"%(edate,body,eid)
		update(q)
		flash('UPDATED')
		return redirect(url_for('admin.admin_manage_elections'))	
	return render_template("admin_manage_elections.html",data=data)

@admin.route('/admin_manage_voters',methods=['get','post'])
def admin_manage_voters():

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
		age=request.form['age']
		dob=request.form['dob']
		place=request.form['place']
		city=request.form['city']
		state=request.form['state']
		phone=request.form['num']
		email=request.form['email']
		uname=request.form['uname']
		passs=request.form['psw']
		q="INSERT INTO `login`(`username`,`password`,`login_type`) VALUES ('%s','%s','voter')"%(uname,passs)	
		login_id=insert(q)

		q="INSERT INTO `voters`(`login_id`,`booth_id`,`election_id`,`first_name`,`last_name`,`age`,`dob`,`place`,`city`,`state`,`phone`,`email`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(login_id,booth,election,fname,lname,age,dob,place,city,state,phone,email)
		insert(q)

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
		return redirect(url_for('admin.admin_manage_voters'))
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name`,voters.login_id as voter_log FROM `voters` INNER JOIN `booths` USING(`booth_id`) INNER JOIN `elections` USING(`election_id`) INNER JOIN `login` ON (`voters`.`login_id`=`login`.`login_id`) "
	res=select(q)
	data['voter']=res

	if 'action' in request.args:
		action=request.args['action']
		vid=request.args['vid']
	else:
		action=None

	if action=='delete':
		q="delete from voters where login_id='%s'"%(vid)
		print(q)
		delete(q)
		q="delete from login where login_id='%s'"%(vid)
		delete(q)
		flash('DELETED')
		return redirect(url_for('admin.admin_manage_voters'))

	if action=='update':
		q="SELECT * FROM `voters` WHERE `login_id`='%s'"%(vid)
		data['voter_up']=select(q)
	if 'updatez' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		age=request.form['age']
		dob=request.form['dob']
		place=request.form['place']
		city=request.form['city']
		state=request.form['state']
		phone=request.form['num']
		email=request.form['email']
		q="UPDATE `voters` SET `first_name`='%s',`last_name`='%s',`age`='%s',`dob`='%s',`place`='%s',`city`='%s',`state`='%s',`phone`='%s',`email`='%s'WHERE `login_id`='%s'"%(fname,lname,age,dob,place,city,state,phone,email,vid)
		update(q)
		flash('UPDATED')
		return redirect(url_for('admin.admin_manage_voters'))
	if action=='accept':
		q="UPDATE login SET login_type='voter' WHERE login_id='%s'"%(vid)
		update(q)
		flash('REQUEST ACCEPTED')
		return redirect(url_for('admin.admin_manage_voters'))
	return render_template("admin_manage_voters.html",data=data)

@admin.route('/admin_view_result')
def admin_view_result():
	data={}
	# if 'action' in request.args:
		# action=request.args['action']
	eid=request.args['eid']
	# else:
		# action=None
	# if action=='result':
	q="SELECT *, CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`)AS NAME FROM `result` INNER JOIN `candidates` USING (`candidate_id`)  where result.election_id='%s'" %(eid) 
	res1=select(q)
	data['status']=res1
	return render_template("admin_view_result.html",data=data)



@admin.route('/count_vote',methods=['get','post'])
def count_vote():
	data={}
	eid=request.args['eid']
	q = "select * from result where election_id='%s'" %(eid)
	res = select(q)
	if len(res) == 0 :
		q="INSERT INTO result(election_id,candidate_id,total_vote) SELECT election_id,candidate_id,COUNT(*) AS total_vote FROM vote inner join candidates using(candidate_id) where election_id='%s' GROUP BY candidate_id ORDER BY total_vote DESC " %(eid)
		insert(q)
		flash("Result published")
		return redirect(url_for('admin.admin_view_result',eid=eid))
	else:
		flash("Result has already published")
		return redirect(url_for('admin.admin_view_result',eid=eid))
	return render_template('admin_count_vote.html',data=data)



@admin.route('/clear_tables',methods=['get','post'])
def clear_tables():
	data={}
	tables = ['booths','candidates','districts','elections','login','result','vote','voters']
	for table in tables:
		q = "truncate table %s" % table
		update(q)
	q = "insert into login values(null,'admin','admin','admin')" 
	insert(q) 
	return redirect(url_for('public.homepage'))
