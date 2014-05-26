import os

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)
# abs_file_path = os.path.join(script_dir, rel_path)

CSRF_ENABLED = True
SECRET_KEY = 'Replace_With_SecretKey'

if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

DATABASE_QUERY_TIMEOUT = 0.5

# email server
# Currently set up to work with gmail
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'Replace_with_Username'
MAIL_PASSWORD = 'Replace_With_Password'

# administrator list
ADMINS = ['webmaster@localhost']
