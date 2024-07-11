# For our dummy data when testing out our application
from datetime import datetime
from app import app
from models import db, User,Income
with app.app_context():
    print("Inputting data")
    User.query.delete()
    Income.query.delete()
    # Budget.query.delete()
    # Expense.query.delete()

    # To append our new users to this empty array
    new_user = []

    charles = User(user_name="Charles Kibet", email="charles@gmail.com",password="charles"
                  )
    new_user.append(charles)

    guido = User(user_name="Guido Python", email="guido@gmail.com",password="charles"
                 )
    new_user.append(guido)

    db.session.add_all(new_user)
    db.session.commit()
    print("Users added successfully")

    new_income = []
    income = Income(amount=4000, user=charles, date=datetime.now())
    income = Income(amount=4000, user=guido, date=datetime.now())
    db.session.add_all(new_income)
    db.session.commit()
    print("Income added successfully")
