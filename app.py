# This are the views or what the end user will see
from flask import Flask
from flask_migrate import Migrate
from datetime import datetime
# from functools import wraps

from models import db, User

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


if __name__ == '__main__':
    app.run()
