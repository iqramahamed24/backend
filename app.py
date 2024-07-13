# This are the views or what the end user will see
import os
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


from models import db
from resources.user import Register, Login
from resources.expense import ExpenseResource
from resources.budget import BudgetResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_ECHO'] = True

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

# Set up of views
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(ExpenseResource, '/expenses')
api.add_resource(BudgetResource, '/budgets')


if __name__ == '__main__':
    app.run()
