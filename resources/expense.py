from flask_restful import Resource
from flask import request
from models import db,Expense
from datetime import datetime


class ExpenseResource(Resource):
    def get(self):
        expenses = Expense.query.all()

        return [expense.to_dict() for expense in expenses], 200
    
    def post(self):
        data = request.get_json()
        new_expense = Expense(amount=data['amount'], category=data['category'],
                          description=data['description'], created_at=datetime.now())

        db.session.add(new_expense)
        db.session.commit()
        return new_expense.to_dict(), 201
