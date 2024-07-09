# This is the schema of our database --> In our database we shall have four models/tables

from flask_sqlalchemy import SQLALCHEMY
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


metadata = MetaData(metadata=convention)

db = SQLALCHEMY(metadata=metadata)



# Models
class User(db.Model, SerializerMixin):

    # This is the users table in our database
    __tablename__ = "users"

    # This are the columns in our database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.TIMESTAMP)
    
class Expense(db.Model,SerializerMixin):

    #This is the table to store our expenses
    __tablename__ = "expenses"
    
    #This  will be the columns in our database
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer)
    category = db.Column(db.Integer)
    description = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP)
    

class Budget(db.Model,SerializerMixin):

    #This will be the table to stores the user's budget
    __tablename__ = "budgets"
    
    #This will be the columns in pur database
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer,nullable=False)
    balance = db.Column(db.Integer)
    
class Income(db.Model,SerializerMixin):

    #This will store the income of our users
    __tablename__ = 'incomes'
    
    #This will be the columns in our database
    id = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer,nullable=False)
    date = db.Column(db.TIMESTAMP)
    
