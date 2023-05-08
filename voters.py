from flask import *
from database import*
from core import *

voters=Blueprint('voters',__name__)

@voters.route('/voters_home')
def voters_home():
	return render_template("voters_home.html")

@voters.route('/voters_view_district_details')
def voters_view_district_details():
	data={}

	vid=session['voter_id']
	q="SELECT * FROM `districts`"
	res=select(q)
	data['result']=res

	return render_template("voters_view_district_details.html",data=data)

@voters.route('/voters_view_booth')
def voters_view_booth():
	data={}
	vid=session['voter_id']
	ids=request.args['ids']

	q="SELECT* FROM `booths` WHERE `district_id`='%s'"%(ids)
	res=select(q)
	data['result']=res

	return render_template("voters_view_booth.html",data=data)



@voters.route('/voters_view_candidates')
def voters_view_candidates():
	data={}
	vid=session['voter_id']
	
	q="SELECT * FROM `candidates`  INNER JOIN `elections` USING (`election_id`) WHERE `candidate_status`='accepted' and district_id=(SELECT `district_id` FROM `voters` INNER JOIN `booths` USING (`booth_id`) WHERE `voter_id`='%s')"%(session['voter_id'])
	res=select(q)
	data['voters']=res
	return render_template("voters_view_candidates.html",data=data)

@voters.route('/voters_view_election_status')
def voters_view_election_status():
	data={}
	vid=session['voter_id']
	
	q="SELECT* FROM `elections`"
	res=select(q)
	data['status']=res
	return render_template("voters_view_election_status.html",data=data)

@voters.route('/voters_make_vote')
def voters_make_vote():
	data={}
	vid=session['voter_id']
	ids=request.args['ids']
	data['ids']=ids
	q="SELECT * FROM `vote` INNER JOIN `candidates` USING (`candidate_id`) INNER JOIN `elections` USING (`election_id`) WHERE `election_id`='%s' AND `voter_id`='%s'"%(ids,vid)
	print(q)
	res=select(q)
	if res:
		flash('ALREADY VOTED')
		return redirect(url_for('voters.voters_view_election_status'))
	else:

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS NAME FROM `candidates` WHERE `election_id`='%s' and district_id=(SELECT `district_id` FROM `voters` INNER JOIN `booths` USING (`booth_id`) WHERE `voter_id`='%s')"%(ids,session['voter_id'])
		res=select(q)
		data['candidates']=res

	if 'action'in request.args:
		action=request.args['action']
		cids=request.args['cids']

	else:
		action=None

	if action=='vote':
		cid=request.args['cids']
		q = "select * from vote order by vote_id desc"
		res = select(q)
		if len(res) > 0 :
			previous_hash = res[0]['hash_value']
		else:
			previous_hash = '0'
		hashing_value = str(vid) + str(ids) + str(previous_hash)
		new_hash = get_hashed_value(hashing_value)
		q="INSERT INTO `vote`(`vote_time`,`voter_id`,`candidate_id`,`hash_value`) VALUES(NOW(),'%s','%s','%s')"%(vid,cid,new_hash)
		insert(q)
		# q="INSERT INTO `vote` (`vote_time`,`voter_id`,`candidate_id`) VALUES (NOW(),'%s','%s')"%(vid,cids)
		# insert(q)
		return redirect(url_for('voters.voters_view_election_status'))

	return render_template("voters_make_vote.html",data=data)


@voters.route('/voters_view_result')
def voters_view_result():
	data={}
	vid=session['voter_id']
	# eid=request.args['eid']
	q="SELECT *, CONCAT (`candidates`.`first_name`,' ',`candidates`.`last_name`)AS NAME FROM `result` INNER JOIN `candidates` USING (`candidate_id`)"
	res=select(q)
	data['result']=res
	return render_template("voters_view_result.html",data=data)

	
