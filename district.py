from flask import *
from database import*

district=Blueprint('district',__name__)

@district.route('/district_home')
def district_home():
	return render_template("district_home.html")

@district.route('/district_view_booths')
def district_view_booths():
	data={}
	did=session['district_id']
	q="SELECT * FROM `booths` INNER JOIN `districts` USING (`district_id`) WHERE `district_id`='%s'"%(did)
	res=select(q)
	data['booths']=res
	return render_template("district_view_booths.html",data=data)
	
@district.route('/district_view_voters')

def district_view_voters():
	data={}
	did=session['district_id']
	
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS NAME FROM `voters` INNER JOIN `booths` USING (`booth_id`) INNER JOIN `districts` USING (`district_id`) INNER JOIN `elections` USING(`election_id`) WHERE `district_id`='%s'"%(did)
	res=select(q)
	data['voters']=res

	return render_template("district_view_voters.html",data=data)