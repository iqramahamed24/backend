#For our dummy data when testing out our application
from datetime import datetime
from app import app
from models import db,User,Budget,Expense,Income

with app.app_context():
   print("Inputing data")
   User.query.delete()
  #  Budget.query.delete()
  #  Expense.query.delete()
  #  Income.query.delete()
   
   #To append our new users to this empty arrat
   users = []
   
   charles= User(username="Charles Kibet",email="charles@gmail.com",phone_number="071234768",created_at=datetime)
   users.append(charles)
   
   guido= User(username="Guido Python",email="guido@gmail.com",phone_number="071234768",created_at=datetime)
   users.append(guido)
   
   
   db.session.all(users)
   db.session.commit()
   print("Users added successfully")