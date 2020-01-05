import os
from flask import Flask, request, jsonify, json, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from flask_seeder import FlaskSeeder

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

from models import User, UserProfile, SpeechQuestion, GrammarQuestion, UserSpeech, UserGrammar
unsplash_access_key = app.config['UNSPLASH_ACCESS_KEY']


@app.route("/")
def generate_speech_question():
    word_list = ['cup', 'dish', 'fork']
    level = 'beginner'

    for text in word_list:
        params = { "query": text }
        headers = {
            "Accept-Version": "v1",
            "Authorization": "Client-ID {}".format(unsplash_access_key)
        }
        response = requests.get("https://api.unsplash.com/search/photos", params=params, headers=headers)
        image_url = json.loads(response.text)["results"][0]["urls"]["full"]

        speech_question = SpeechQuestion(text=text, level=level, image_url=image_url)
        db.session.add(speech_question)
        db.session.commit()

    print("{} {}-level words have been added to the database!".format(len(word_list), level))

@app.route("/signup", methods=['GET','POST'])
def create_new_user():
    req=request.get_json()
    password=request.args.get('password')
    print("Email : {}, Password: {}".format(req['email'],req['password']))
    hash = bcrypt.generate_password_hash(req['password']).decode('utf-8')
    check_user_exists = User.query.filter_by(email=req['email']).first()
    if check_user_exists:
            return jsonify({'error': 'Email already exists'}), 409


    user = User(email=req['email'], password=hash)
    db.session.add(user)
    db.session.commit()
    return jsonify({'user_id':user.id, 'email':user.email}), 222


@app.route("/login", methods=['GET', 'POST'])
def login_user():
        req=request.get_json()
        user=User.query.filter_by(email=req['email']).first()
        if user and bcrypt.check_password_hash(req['password'], user.password):
                profile=UserProfile.query.filter_by(user_id=user.id).first()
                print(profile)
        # not sure what to return here either
        return jsonify('testing')


@app.route("/create_user_profile", methods=['GET', 'POST'])
def create_user_profile():
        req=request.get_json()
        user_profile=UserProfile(user_id=req['user_id'], name=req['name'], age=req['age'], proficiency=req['proficiency'])
        db.session.add(user_profile)
        db.session.commit()
        return jsonify(user_profile.serialize())



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

@app.route('/speech_questions')
def get_speech_questions():
    try:
        users = SpeechQuestion.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

@app.route('/grammar_questions')
def get_grammar_questions():
    try:
        users = GrammarQuestion.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

@app.route('/users_speech')
def get_users_speech():
    try:
        users = UserSpeech.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

@app.route('/users_grammar')
def get_users_grammar():
    try:
        users = UserGrammar.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
    app.run()
