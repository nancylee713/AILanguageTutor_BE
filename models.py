from app import db

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import datetime

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String())
  password = db.Column(db.String())

  def __init__(self, email, password):
    self.email = email
    self.password = password


  def __repr__(self):
    return '<id {}>'.format(self.id)


  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'password': self.password

    }


class UserProfile(db.Model):
  __tablename__ = 'users_profile'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String())
  age = db.Column(db.Integer)
  proficiency = db.Column(db.String())
  user_id = db.Column(db.Integer, ForeignKey(User.id))
  created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
  updated_date = db.Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

  user = relationship('User', backref='users_profile')

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
      'updated_date': self.updated_date,

    }
