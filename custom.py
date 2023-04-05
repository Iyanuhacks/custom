import os
from app import create_app,db
from app.models import User,Role
from flask_migrate import Migrate
import unnittest
app=createapp(os.getenv('FLASKCONFIG')or'default')
migrate=Migrate(app,db)
@app.shell_context_processor

def make_shell_context():
 return dict(db=db,User=User,Role=Role)
@app.cli.command()

def test():
 """Run the unit tests."""
 tests=unittest.TestLoader().discover('tests')
 unittest.TextTestRunner(verbosity=2).run(tests)
