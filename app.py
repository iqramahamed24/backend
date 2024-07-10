# This are the views or what the end user will see
from flask import Flask,make_response,request
from flask_migrate import Migrate

from models import db, User,Income,Budget,Expense

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Manage your funds more easily</h1>'


@app.route('/users')
def users():

    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    print(users_list)
    return []

@app.route('/incomes')
def income():
    income = Income.query.all()
    print(income)

@app.route('/budgets')
def budget():
    budget = Budget.query.all()
    print(budget)
    
@app.route('/expenses')
def expense():
    expense = Expense.query.all()
    print(expense)


if __name__ == '__main__':
    app.run()
