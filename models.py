from db import db

class Detail(db.Model):
	__tablename__='customer_detail'
	id = db.Column(db.Integer,primary_key=True)
	id_customer = db.Column(db.Integer,db.ForeignKey('customer.id'))
	address=db.Column(db.String(20))
	birth_place = db.Column(db.String(20))
	birth_date = db.Column(db.DateTime)
	job = db.Column(db.String(20))

	def __init__(self, id_customer, address, birth_place,birth_date,job):
		self.id_customer = id_customer
		self.address = address
		self.birth_place = birth_place
		self.birth_date = birth_date
		self.job = job
		
	def __repr__(self):
		return '<Detail {}>'.format(self.id_customer)

class Customer(db.Model):
	__tablename__='customer'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(20))
	email = db.Column(db.String(20))
	id_master_gender = db.Column(db.Integer,db.ForeignKey('master_gender.id'))
	customer_detail = db.relationship('Detail', backref='detail',lazy='dynamic')

	def __init__(self,name,email,id_master_gender):
		self.name = name
		self.email = email
		self.id_master_gender = id_master_gender

	def __repr__(self):
		return '<Customer {}>'.format(self.name)

class Gender(db.Model):
	__tablename__='master_gender'
	id = db.Column(db.Integer,primary_key=True)
	gender = db.Column(db.String(10))
	customer = db.relationship('Customer',backref='customer',lazy='dynamic')