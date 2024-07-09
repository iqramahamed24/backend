#This are the views or what the end user will see
from flask import Flask
from flask_migrate import Migrate

from models import db,User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] 

migrate = Migrate(app,db)

@app.route('/')
def home():
  return '<h1>Manage your funds more easily</h1>'

@app.route('/users')
def users():
   users = User.query.all()
   print(users)
