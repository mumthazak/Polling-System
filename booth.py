from flask import *
from database import*

booth=Blueprint('booth',__name__)

@booth.route('/booth_home')
def booth_home ():
	return render_template("booth_home.html")

@booth.route('/booth_view_voters')
def booth_view_voters ():
	data={}
	bid=session['booth_id']
	q="SELECT * FROM `voters` INNER JOIN `booths` USING (`booth_id`) INNER JOIN `elections` USING (`election_id`)"
	res=select(q)
	data['voters']=res
	return render_template("booth_view_voters.html",data=data)


