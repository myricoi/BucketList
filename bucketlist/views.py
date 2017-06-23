from flask import render_template, request, redirect, url_for
from bucketlist import app
from .classes import User, users, Bucketlist, bucketlists
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if(not request.form['submit']):
		return render_template('index.html')
	else:
		login_details = [request.form['username'], request.form['password']]
		check_details = True
		for detail in login_details:
			if(not detail):
				reply = {'message':'* (field is required)','value1':login_details[0],'value2':login_details[1]}
				return  render_template('index.html', field_empty_response = reply)
		
		
		if('.' in login_details[0]):
			reply = {'message':'* (invalid username, dot not allowed)','value1':login_details[0],'value2':login_details[1]}
			return render_template('index.html', response = reply)
		else:
			first_letter = ""
			try:
				first_letter = int(login_details[0][0])
			except:
				pass
			if(isinstance(first_letter, int)):
				reply = {'message':'* (username cannot start with a number)', 'value1': login_details[0], 'value2': login_details[1]}
				return render_template('index.html', response = reply)
			else:
				for user in users:
					if(user.getLoginDetails() == login_details):
						return redirect(url_for('view_bucketlist'))
				return "<script>window.alert('No such user found.'); window.location='http://localhost:5000/index';</script>"



				


@app.route('/sign_up', methods = ['GET','POST'])
def sign_up():
	if(request.form['submit_sign_up']):
		check_details = True
		signup_details = [request.form['first_name'], request.form['last_name'], request.form['user_name'], request.form['reg_password'], request.form['confirm_password'], request.form['email']]
		for detail in signup_details:
			if(not detail):
				value=signup_details
				return render_template('index.html',signup_response = True, response_1 = True, values = value)
		if('.' in signup_details[0] or '.' in signup_details[1] or '.' in signup_details[2]):
			value=signup_details
			return render_template('index.html',signup_response = True, response_2 = True, values = value)
		else:
			first_letter_1 = ""
			first_letter_2 = ""
			first_letter_3 = ""
			try:
				first_letter_1 = int(signup_details[0][0])
			except:
				try:
					first_letter_2 = int(signup_details[1][0])
				except:
					try:
						first_letter_3 = int(signup_details[2][0])
					except:
						pass
			if(isinstance(first_letter_1, int) or isinstance(first_letter_2, int) or isinstance(first_letter_3, int)):
				value=signup_details
				return render_template('index.html',signup_response = True, response_3 = True, values = value)
			else:
				if(signup_details[3] != signup_details[4]):
					value=signup_details
					return render_template('index.html',signup_response = True, response_4 = True, values = value)
				else:
					for user in users:
						if(user.getLoginDetails() == [signup_details[2], signup_details[3]]):
							return "<script> window.alert('user already exists. login to continue'); window.location='http://localhost:5000/index';</script>"
					new_user = User(signup_details[0],signup_details[1],signup_details[2],signup_details[3],signup_details[5])
					return "<script> window.alert('Account created. Log in to continue'); window.location='http://localhost:5000/index';</script>"
	else:
		return "<script>window.location='http://localhost:5000/index';</script>"

@app.route('/create_bucketlist', methods = ['GET','POST'])
def createBucketlist():
	bucketlist_name = request.form['bucketlist_name']
	username = request.form['username']
	password = request.form['password']
	owner = None

	for user in users:
		if([user.username, user.password] == [username, password]):
			owner = user
			break

	new_bucketlist = Bucketlist(bucketlist_name, owner)
	return redirect(url_for('view_bucketlist'), current_user = owner.getLoginDetails())

@app.route('/view_bucketlist', methods = ['GET','POST'])
def view_bucketlist():
	
	my_bucketlist = []
	for bucketlist in bucketlists:
		if(bucketlist.getOwner() == logged_in_user):
			my_bucketlist.append(bucketlist)
	return render_template('after_login.html', my_bucketlists = my_bucketlist)



