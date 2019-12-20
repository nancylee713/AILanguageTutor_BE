from app import db
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
import datetime

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

  def __init__(self, email, password, created_date, updated_date):
    self.email = email
    self.password = password
    self.created_date = created_date
    self.updated_date = updated_date


  def __repr__(self):
    return '<id {}>'.format(self.id)


  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'password': self.password,
      'created_date': self.created_date,
      'updated_date': self.updated_date
    }

class UserProfile(db.Model):
  __tablename__ = 'users_profile'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  age = db.Column(db.Integer)
  proficiency = db.Column(db.String())
  user_id = db.Column(db.Integer, ForeignKey(User.id))
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

  def __init__(self, name, age, proficiency, user_id, created_date, updated_date):
    self.name = name
    self.age = age
    self.proficiency = proficiency
    self.user_id = user_id
    self.created_date = created_date
    self.updated_date = updated_date


  def __repr__(self):
    return '<id {}>'.format(self.id)


  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'proficiency': self.proficiency,
      'user_id': self.user_id,
      'created_date': self.created_date,
      'updated_date': self.updated_date

    }

class SpeechQuestion(db.Model):
    __tablename__ = 'speech_questions'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String())
    text = db.Column(db.String())
    image_url = db.Column(db.String())
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, level, text, image_url, created_date, updated_date):
        self.level = level
        self.text = text
        self.image_url = image_url
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


    def serialize(self):
        return {
         'id': self.id,
         'level': self.level,
         'text': self.text,
         'image_url': self.image_url,
         'created_date': self.created_date,
         'updated_date': self.updated_date

        }

class GrammarQuestion(db.Model):
    __tablename__ = 'grammar_questions'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String())
    text = db.Column(db.String())
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, level, text, created_date, updated_date):
        self.level = level
        self.text = text
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


    def serialize(self):
        return {
         'id': self.id,
         'level': self.level,
         'text': self.text,
         'created_date': self.created_date,
         'updated_date': self.updated_date

        }

class UserSpeech(db.Model):
    __tablename__ = 'users_speech'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    speech_question_id = db.Column(db.Integer, ForeignKey(SpeechQuestion.id))
    status = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, user_id, speech_question_id, status, created_date, updated_date):
        self.user_id = user_id
        self.speech_question_id = speech_question_id
        self.status = status
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


    def serialize(self):
        return {
         'id': self.id,
         'user_id': self.user_id,
         'speech_question_id': self.speech_question_id,
         'status': self.status,
         'created_date': self.created_date,
         'updated_date': self.updated_date

        }

class UserGrammar(db.Model):
    __tablename__ = 'users_grammar'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    grammar_question_id = db.Column(db.Integer, ForeignKey(GrammarQuestion.id))
    status = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, user_id, grammar_question_id, status, created_date, updated_date):
        self.user_id = user_id
        self.grammar_question_id = grammar_question_id
        self.status = status
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


    def serialize(self):
        return {
         'id': self.id,
         'user_id': self.user_id,
         'grammar_question_id': self.grammar_question_id,
         'status': self.status,
         'created_date': self.created_date,
         'updated_date': self.updated_date

        }
