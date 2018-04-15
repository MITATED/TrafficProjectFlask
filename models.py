from app import db
from datetime import datetime
from re import sub

from flask_security import UserMixin, RoleMixin



def slugify(s):
	pattern = r'[^\w+]'
	return sub(pattern, '-', str(s))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		return '#{} {}'.format(self.id, self.title)


### Flask Security ###

roles_users = db.Table('roles_users', 
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
	)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())

	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(255))



