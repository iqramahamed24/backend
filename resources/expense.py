from flask_restful import Resource
from flask import request
from models import db, Expense
from datetime import datetime


class ExpenseResource(Resource):

    # Add a new expense
    def post(self):
        data = request.get_json()
        new_expense = Expense(amount=data['amount'], category=data['category'],
                              description=data['description'], created_at=datetime.now())

        db.session.add(new_expense)
        db.session.commit()
        return new_expense.to_dict(), 201

    # Retrieving the expenses
    def get(self):
        expenses = Expense.query.all()

        return [expense.to_dict() for expense in expenses], 200

    # Update the expense
    def update(self, id):
        expense = Expense.query.get(id)
        if expense == None:
            return {'message': 'Expense not found'}, 400

        data = request.get_json()
        expense.amount = data['amount']
        expense.category = data['category']
        expense.description = data['description']
        db.session.commit()
        return expense.to_dict(), 200

    # Deleting the expense
    def delete(self, id):
        expense = Expense.query.filter_by(id == id).first()

        if expense == None:
            return {"message": "Expense not found"}, 404

        db.session.delete(expense)
        db.commit()
        print("Expenses successfully")
        return []
