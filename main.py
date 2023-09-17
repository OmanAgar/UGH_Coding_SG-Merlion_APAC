import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash



#********INITIALISATION********#
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'testing123'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)



#********OBJECTS*********#
import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    email = db.Column(db.String(100), unique = True, nullable = False,primary_key = True)
    password = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default = func.now())
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    phonenumber = db.Column(db.Integer, nullable = False,unique = True)
    def __repr__(self):
        return f'<User {self.name}>'

class Driver(db.Model):
    email = db.Column(db.String(100), nullable = False,unique = True,primary_key = True)
    vehiclenumber = db.Column(db.String(100), nullable = False)
    peopleallowedtocarry = db.Column(db.Integer, nullable = False)
    model = db.Column(db.String(100), nullable = False)
    seats = db.Column(db.Integer, nullable = False)

# coords use long1,lat1,long2,lat2
class Route(db.Model):
    lo1 = db.Column(db.Float, nullable = False)
    la1 = db.Column(db.Float, nullable = False)
    lo2 = db.Column(db.Float, nullable = False)
    la2 = db.Column(db.Float, nullable = False)
    driver = db.Column(db.String(100), nullable = False,primary_key = True)
    rider = db.Column(db.String(100), nullable = False)

with app.app_context():
    #db.drop_all()
    db.create_all()


#********ROUTING********#
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup", methods = ['POST'])
def signup_post():
    firstname = request.form['first-name']
    lastname = request.form['last-name']
    password = request.form['password']
    phonenumber = request.form['phone-number']
    confirmpassword = request.formm["confirm-password"]
    user = User.query.filter_by(email=email).first()
    
    if confrmpassword != password:
        flash('Email address already exists')
        return redirect(url_for('signup'))        

    if user:
        flash('Email address already exists')
        return redirect(url_for('signup'))

    new_user = User(email=email, name=name, 
    password=generate_password_hash(password,method='sha-256'))

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods = ['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
  
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    login_user(user)
    return redirect(url_for("profile"))

@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))   

app.run(  # Starts the site
        host="192.168.18.4",  # Required to run the site. must use your own ip
        debug=True  # to run Flask in debug mode
       )
