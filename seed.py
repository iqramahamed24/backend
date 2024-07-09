# For our dummy data when testing out our application
from datetime import datetime
from app import app
from models import db, User

with app.app_context():
    print("Inputting data")
    User.query.delete()
   #  Budget.query.delete()
   #  Expense.query.delete()
   #  Income.query.delete()

    # To append our new users to this empty array
    new_user = []

    charles = User(user_name="Charles Kibet", email="charles@gmail.com",
                   phone_number="071234768", created_at=datetime.now())
    new_user.append(charles)

    guido = User(user_name="Guido Python", email="guido@gmail.com",
                 phone_number="071234778", created_at=datetime.now())
    new_user.append(guido)

    db.session.add_all(new_user)
    db.session.commit()
    print("Users added successfully")
