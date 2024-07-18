from flask import request
from datetime import datetime
from models import db, Income
from flask_restful import Resource


class IncomeResource(Resource):

    # The user can retrieve all the incomes
    def get(self):
        incomes = Income.query.all()

        return [income.to_dict() for income in incomes], 200

    # The user adds the income
    def post(self):
        data = request.get_json()
        new_income = Income(
            source=data['source'], amount=data['amount'], date=datetime.now())

        db.session.add(new_income)
        db.session.commit()
        return new_income.to_dict(), 201

    # Update the expense
    def update(self, id):
        income = Income.query.get(id)
        if income == None:
            return {'message': 'Income not found'}, 400

        data = request.get_json()
        income.source = data['source']
        income.amount = data['amount']

        db.session.commit()
        return income.to_dict(), 200

  # The user can delete the income
    def delete(self, id):
        income = Income.query.filter_by(id == id).first()

        if income == None:
            return {"message": "Expense not found"}, 404

        db.session.delete(income)
        db.commit()
        print("Expenses successfully")
        return []
