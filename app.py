# This are the views or what the end user will see
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from datetime import datetime
# from functools import wraps

from models import db, User, Expense, Budget

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Manage your funds more easily</h1>'


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization'].split(" ")[1]
#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 401
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#             current_user = User.query.filter_by(id=data['user_id']).first()
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 401
#         return f(current_user, *args, **kwargs)
#     return decorated


@app.route('/users')
def users():

    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    print(users_list)
    return []



# Register User
@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    new_user = User(user_name = data['user_name'], email = data['email'],password=data['password'])

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict())



# Login User
# app.route('/login', methods = ['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(email = data['email']).first()
#     if user and user.verify_password(data['password']):
#         token = user.generate_auth_token()
#         return jsonify({'token': token}), 200
#     return jsonify({'message': 'Invalid credentials'}), 401



# Add Expense
@app.route('/expenses', methods = ['POST'])
# @token_required
def add_expense():
    data = request.get_json()
    new_expense = Expense(amount = data['amount'], category = data['category'], description = data['description'], created_at = datetime.now())

    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201




# Get Expenses
@app.route('/expenses', methods = ['GET'])
# @token_required
def get_expenses():
    expenses = Expense.query.all()

    return jsonify([expense.to_dict() for expense in expenses]), 200



# Update Expense
@app.route('/expenses/<int:id>', methods = ['PATCH'])
# @token_required
def update_expense(id):
    expense = Expense.query.get(id)
    if  expense ==None:
        return jsonify({'message': 'Expense not found'}), 400
    
    data = request.get_json()
    expense.amount = data['amount']
    expense.category = data['category']
    expense.description = data['description']
    db.session.commit()
    return jsonify(expense.to_dict()), 200



# Delete Expense
@app.route('/expenses/<int:id>', methods = ['DELETE'])
# # @token_required
def delete_expense(id):
    expense = Expense.query.filter_by(id = id).first()
    if expense == None:
        return jsonify({"message": "Expense not found"}), 404
    
    db.session.delete(expense)
    db.session.commit()
    print("Deleted successfully")
    return []








# Add Budget
@app.route('/budgets', methods = ['POST'])
# @token_required
def add_budget():
    data = request.get_json()
    new_budget = Budget(
        amount = data['amount'],
        description = data['description']
        
    )
    db.session.add(new_budget)
    db.session.commit()
    return jsonify(new_budget.to_dict()), 201




# Get Budgets
@app.route('/budgets', methods = ['GET'])
# @token_required
def get_budgets():
    budgets = Budget.query.all()

    return jsonify([budget.to_dict() for budget in budgets]), 200



# Update Budget
@app.route('/budgets/<int:id>', methods = ['PATCH'])
# @token_required
def update_budget(id):
    budget = Budget.query.get(id)
    if budget ==None:
        return jsonify({'message', 'Budget not found'}), 404
    
    data = request.get_json()
    budget.amount = data['amount']
    budget.category = data['category']
    budget.description = data['description']
    db.session.commit()
    return jsonify(budget.to_dict()), 200




# Delete Budget
@app.route('/budgets/<int:id>', methods = ['DELETE'])
# @token_required
def delete_budget(id):
    budget = Budget.query.filter_by(id=id).first()
    if  budget ==None:
        return jsonify({'message': "Budget not found"}), 404
    
    db.session.delete(budget)
    db.session.commit()
    print('Deleted successfully')
    return []







if __name__ == '__main__':
    app.run()
