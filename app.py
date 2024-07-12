# This are the views or what the end user will see
import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from datetime import datetime
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


from models import db, User, Budget, Expense
from resources.user import Register, Login
from resources.expense import ExpenseResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_ECHO'] = True

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
# Access tokens should be short lived, this is for this phase only

migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)


@app.route('/')
def home():
    return '<h1>Manage your funds more easily</h1>'

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(ExpenseResource,'/expenses')

@app.route('/users')
def users():

    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    print(users_list)
    return []

# Add Expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(amount=data['amount'], category=data['category'],
                          description=data['description'], created_at=datetime.now())

    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201

# Update Expense
@app.route('/expenses/<int:id>', methods=['PATCH'])
# @token_required
def update_expense(id):
    expense = Expense.query.get(id)
    if expense == None:
        return jsonify({'message': 'Expense not found'}), 400

    data = request.get_json()
    expense.amount = data['amount']
    expense.category = data['category']
    expense.description = data['description']
    db.session.commit()
    return jsonify(expense.to_dict()), 200


# Delete Expense
@app.route('/expenses/<int:id>', methods=['DELETE'])
# # @token_required
def delete_expense(id):
    expense = Expense.query.filter_by(id=id).first()
    if expense == None:
        return jsonify({"message": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()
    print("Deleted successfully")
    return []


# Add Budget
@app.route('/budgets', methods=['POST'])
# @token_required
def add_budget():
    data = request.get_json()
    new_budget = Budget(
        amount=data['amount'],
        description=data['description']

    )
    db.session.add(new_budget)
    db.session.commit()
    return jsonify(new_budget.to_dict()), 201


# Get Budgets
@app.route('/budgets', methods=['GET'])
# @token_required
def get_budgets():
    budgets = Budget.query.all()

    return jsonify([budget.to_dict() for budget in budgets]), 200


# Update Budget
@app.route('/budgets/<int:id>', methods=['PATCH'])
# @token_required
def update_budget(id):
    budget = Budget.query.get(id)
    if budget == None:
        return jsonify({'message', 'Budget not found'}), 404

    data = request.get_json()
    budget.amount = data['amount']
    budget.category = data['category']
    budget.description = data['description']
    db.session.commit()
    return jsonify(budget.to_dict()), 200

# Delete Budget


@app.route('/budgets/<int:id>', methods=['DELETE'])
# @token_required
def delete_budget(id):
    budget = Budget.query.filter_by(id=id).first()
    if budget == None:
        return jsonify({'message': "Budget not found"}), 404

    db.session.delete(budget)
    db.session.commit()
    print('Deleted successfully')
    return []


if __name__ == '__main__':
    app.run()
