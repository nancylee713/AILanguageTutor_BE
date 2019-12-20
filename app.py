import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from models import User, UserProfile, SpeechQuestion, GrammarQuestion, UserSpeech, UserGrammar


@app.route("/")
def hello():
    return "Hello World!"

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
