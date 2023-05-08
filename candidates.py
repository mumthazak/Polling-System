from flask import *
from database import*

candidates=Blueprint('candidates',__name__)

@candidates.route('/candidates_home')
def candidates_home():
	id=session['cid']
	print(id)
	return render_template("candidates_home.html")

@candidates.route('/candidates_view_voting_status')
def candidates_view_voting_status():
	data={}
	id=session['cid']
	
	q="SELECT *,CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`) AS candidate_name FROM `result` INNER JOIN `candidates` USING (`candidate_id`) WHERE `election_id`=(SELECT `election_id` FROM `candidates` WHERE `candidate_id`='%s')"%(id)
	res=select(q)
	data['result']=res
	return render_template("candidates_view_voting_status.html",data=data)

@candidates.route('/candidates_view_boothwise')
def candidates_view_boothwise():
	data={}
	id=session['cid']
	q="SELECT * FROM `booths`"
	data['booth']=select(q)
	if 'action' in request.args:
		action=request.args['action']
		bid=request.args['id']
	else:
		action=None
	if action=='result':

		q="SELECT COUNT(`vote_id`) AS vote,`candidate_id`,`voter_id`,CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`) AS cand_name FROM `vote` INNER JOIN `voters` USING(`voter_id`) INNER JOIN `candidates` USING (`candidate_id`) WHERE `booth_id`='%s' GROUP BY `candidate_id`"%(bid)
		res=select(q)
		data['booth_result']=res
	
	return render_template("candidates_view_boothwise.html",data=data)

@candidates.route('/candidates_view_districtwise')
def candidates_view_districtwise():
	data={}
	id=session['cid']
	q="SELECT * FROM `districts`"
	data['district']=select(q)
	if 'action' in request.args:
		action=request.args['action']
		did=request.args['id']
	else:
		action=None
	if action=='result':

		q="SELECT COUNT(`vote_id`)  AS vote,`candidate_id`,`voter_id`,CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`) AS cand_name FROM `vote` INNER JOIN `voters` USING(`voter_id`)INNER JOIN `booths` USING (`booth_id`) INNER JOIN `candidates` USING (`candidate_id`) WHERE `district_id`='%s' GROUP BY `candidates`.`candidate_id`"%(did)
		res=select(q)
		data['dis_result']=res
	return render_template("candidates_view_districtwise.html",data=data)



