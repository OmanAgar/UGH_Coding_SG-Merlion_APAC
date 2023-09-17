import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import objects


#********OBJECTS*********#
import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now())
    def __repr__(self):
        return f'<User {self.name}>'

class Driver(db.Model):
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    phonenumber = db.Column(db.Integer, nullable = False)
    vehiclenumber = db.Column(db.String(100), nullable = False)
    peopleallowedtocarry = db.Column(db.Integer, nullable = False)
    model = db.Column(db.String(100), nullable = False)
    seats = db.Column(db.Integer, nullable = False)

class Rider(db.Model):
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    phonenumber = db.Column(db.Integer, nullable = False)

# coords use long1,lat1,long2,lat2
class Route(db.Model):
    def __init__(self,lo1,la1,lo2,la2,driver,rider):
        lo1 = db.Column(Float, nullable = False)
        la1 = db.Column(Float, nullable = False)
        lo2 = db.Column(Float, nullable = False)
        la2 = db.Column(Float, nullable = False)
        self.driver = db.Column(db.String(100), nullable = False)
        self.rider = db.Column(db.String(100), nullable = False)

with app.app_context():
    #db.drop_all()
    db.create_all()

#********INITIALISATION********#
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'testing123'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

