from flask import Flask,render_template,redirect,request,session
from datetime import datetime
from db import db
from models import Detail, Customer, Gender
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object('config')
db.init_app(app)
	
@app.route('/')
def home():
	pass

@app.route('/addcustomer', methods=['POST','GET'])
def addcustomer():
	if request.method =='POST':
		name = request.form['name']
		email = request.form['email']
		id_master_gender = request.form['gender']
		customer = Customer(name,email,id_master_gender)

		errors = []
		if name is None or name =='':
			errors.append('Are you fucking kidding me?, Input your name now!!!')
		if email is None or email =='':
			errors.append("Please input email or you don't have email? Hmm KAMPUNGAN!!!")
		if errors:
			for err in errors:
				return err

		db.session.add(customer)
		db.session.commit()

		session['customer_id'] = customer.id
	return 'customer successfully added'

@app.route('/detail',methods=['POST','GET'])
def add_detail():
	if request.method == 'POST':
		#get session customer
		id_customer = session.get('customer_id')
		#get user input
		address = request.form['address']
		birth_date = request.form['birth_date']
		birth_place=request.form['birth_place']
		job = request.form['job']

		#validate birthdate
		dateValidate(birth_date)
		
		#create object
		detail = Detail(id_customer,address,birth_place,birth_date,job)
		
		#handle error message
		errors = []
		
		#handle input error
		if address is None or address =='':
			errors.append('Please input your address')
		if birth_place is None or birth_place=='':
			errors.append('Please input your birth place')
		if birth_date is None or birth_date=='':
			errors.append('Please input your birth date')
		if job is None or job =='':
			errors.append('Input your job or you are unemployment? KASIHAN :(')
		if not dateValidate(birth_date):
			errors.append('Input your birth date please,')
		if errors:
			for err in errors:
				return err

		#insert data to database
		db.session.add(detail)
		db.session.commit()
		
		
		return 'congratulation, successful input data'		
def dateValidate(birth_date):
	#default format
	formatting = '%d-%m-%Y'
	#date validate, process
	try:
		date = datetime.strptime(birth_date,formatting)
		return True
	except ValueError:
		return False
	
if __name__=='__main__':
	app.run(debug=True)