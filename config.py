import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
 SECRETKEY= os.environ.get('SECRETKEY')or "or strong unguessable string"
 MAIL_SERVER=os.environ.get('MAIL_SERVER',smtp.googlemail.com)
 MAIL_PORT=int(os.environ.get('MAIL_PORT',587))
 MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS','true').lower()in \
 ['true','on','1']
 MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
 MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
 CUSTOM_MAIL_SUBJECT_PREFIX='[CUSTOM]'
 CUSTOM_MAIL_SENDER='CUSTOM Admin <name@example.com>'
 CUSTOM_ADMIN=os.environ.get('CUSTOM_ADMIN')
 SQLALCHEMY_TRACK_MODIFICATIONS=False

@staticmethod
def init_app(app):
  pass
class DevelopmentConfig(Config):
  DEBUG=True
  SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABASE_URL')
class TestingConfig(Config):
  TESTING=True
  SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL')
class ProductionConfig(Config):
 SQLALCHEMY_DATABASEURL=os.environ.get('DATABASEURL')

config={
 development:DevelopmentConfig,
 testing:TestingConfig,
 production:ProductionConfig,
 default:DevelopmentConfig
}
