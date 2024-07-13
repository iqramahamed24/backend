from flask_restful import Resource
from flask import request
from models import db, Budget


class BudgetResource(Resource):
    # Add budget
    def post(self):

        data = request.get_json()
        new_budget = Budget(
            amount=data['amount'],
            description=data['description']

        )
        db.session.add(new_budget)
        db.session.commit()
        print("Budget added successfully")

    # Get budgets
    def get(self):
        budgets = Budget.query.all()

        return [budget.to_dict() for budget in budgets], 200

    # Update budgets
    def update(id):
        budget = Budget.query.get(id)
        if budget == None:
            return {'message', 'Budget not found'}, 404

        data = request.get_json()
        budget.amount = data['amount']
        budget.category = data['category']
        budget.description = data['description']
        db.session.commit()
        return budget.to_dict(), 200

    # Delete budgets
    def delete(id):
        budget = Budget.query.get(id)
        if budget == None:
            return {'message': "Budget not found"}, 404

        db.session.delete(budget)
        db.session.commit()
        print('Deleted successfully')
        return []
