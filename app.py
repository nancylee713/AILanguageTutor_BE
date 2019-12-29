import os
from flask import Flask, request, jsonify, json
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


# secret = bcrypt.generate_password_hash('password').decode('utf-8')
# bcrypt.check_password_hash(secret, 'password')


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from models import User, UserProfile


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/signup", methods=['GET','POST'])
def create_new_user():
    req=request.get_json()
    password=request.args.get('password')
    print("Email : {}, Password: {}".format(req['email'],req['password']))
    hash = bcrypt.generate_password_hash(req['password']).decode('utf-8')
    print(hash)
    check_user_exists = User.query.filter_by(email=req['email']).first()
    if check_user_exists:
            return jsonify({'error': 'Email already exists'}), 409


    user = User(email=req['email'], password=hash)
#     db.session.add(user)
#     db.session.commit()
    return jsonify(req), 222


@app.route("/login", methods=['GET', 'POST'])
def login_user():
        req=request.get_json()
        user=User.query.filter_by(email=req['email']).first()
        print(user)
        # print(bcrypt.check_password_hash(user.password, req['password']))
        if user and bcrypt.check_password_hash(req['password'], user.password):
                profile=UserProfile.query.filter_by(user_id=user.id).first()
                print(profile)
        return jsonify('testing')



@app.route('/users')
def get_users():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
            return(str(e))


@app.route('/users_profile')
def get_users_profile():
    try:
        users = UserProfile.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
            return(str(e))
      
      
if __name__ == '__main__':
    app.run()
