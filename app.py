# This are the views or what the end user will see
from flask import Flask
from flask_migrate import Migrate

from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Manage your funds more easily</h1>'


@app.route('/users')
def users():

    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())
    print(users_list)
    return []


if __name__ == '__main__':
    app.run()
