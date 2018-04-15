class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SQLALCHEMY_DATABASE_URI = 'postgresql://flask:111111flask@flaskdb.c0pugcp6ni5m.us-west-2.rds.amazonaws.com:5432/flask_db'
	SECRET_KEY = 'semething very secret'

	### Flask Security
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'
	SECURITY_REGISTERABLE = True