from app import db
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from datetime import datetime

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
  profile = db.relationship('UserProfile', backref='user', lazy=True)

  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.created_date = self.created_date
    self.updated_date = self.updated_date

  def __repr__(self):
      return f"User(id: '{self.id}', email: '{self.email}')"



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
  name = db.Column(db.String(),unique=True, nullable=False)
  age = db.Column(db.Integer)
  proficiency = db.Column(db.String(), nullable=False)
  user_id = db.Column(db.Integer, ForeignKey(User.id), nullable=False)
  created_date = db.Column(DateTime, default=datetime.utcnow)
  updated_date = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

  def __init__(self, name, age, proficiency, user_id):
    self.name = name
    self.age = age
    self.proficiency = proficiency
    self.user_id = user_id
    self.created_date = self.created_date
    self.updated_date = self.updated_date


  def __repr__(self):
    return f"UserProfile(name: '{self.name}', level: '{self.proficiency}', user_id: '{self.user_id}')"


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

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  level = db.Column(db.String(), nullable=False)
  text = db.Column(db.Text, nullable=False)
  image_url = db.Column(db.String())
  created_date = db.Column(DateTime, default=datetime.utcnow)
  updated_date = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

  def __init__(self, level, text, image_url):
    self.level = level
    self.text = text
    self.image_url = image_url
    self.created_date = self.created_date
    self.updated_date = self.updated_date

  def __repr__(self):
      return f"SpeechQuestion(id: '{self.id}', level: '{self.level}')"


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
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, level, text):
        self.level = level
        self.text = text
        self.created_date = self.created_date
        self.updated_date = self.updated_date

    def __repr__(self):
        return f"GrammarQuestion(id: '{self.id}', level: '{self.level}')"


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
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, user_id, speech_question_id, status, created_date, updated_date):
        self.user_id = user_id
        self.speech_question_id = speech_question_id
        self.status = status
        self.created_date = self.created_date
        self.updated_date = self.updated_date

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
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, user_id, grammar_question_id, status, created_date, updated_date):
        self.user_id = user_id
        self.grammar_question_id = grammar_question_id
        self.status = status
        self.created_date = self.created_date
        self.updated_date = self.updated_date

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
