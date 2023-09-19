import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import phonenumbers
import math

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
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100),nullable=False)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    phonenumber = db.Column(db.Integer, nullable = False,unique = True)
    id = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'

class Driver(db.Model):
    email = db.Column(db.String(100), nullable = False,unique = True,primary_key = True)
    vehiclenumber = db.Column(db.String(100), nullable = False)
    peopleallowedtocarry = db.Column(db.Integer, nullable = False)
    model = db.Column(db.String(100), nullable = False)
    seats = db.Column(db.Integer, nullable = False)

# coords use long1,lat1,long2,lat2
class Route(db.Model):
    origin = db.Column(db.String(100), nullable = False)
    destination = db.Column(db.String(100), nullable = False)
    driver = db.Column(db.String(100), nullable = False)
    rider = db.Column(db.String(100), nullable = False,primary_key = True)
    eta = db.Column(db.Integer, nullable = False)
    distance = db.Column(db.Integer, nullable = False)

with app.app_context():
    #db.drop_all()
    db.create_all()


#********ROUTING********#
@app.route('/')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup", methods = ['POST'])
def signup_post():
    firstname = request.form['first-name']
    lastname = request.form['last-name']
    password = request.form['password']
    phonenumber = request.form['phone-number']
    email = request.form['email']
    confirmpassword = request.form["confirm-password"]
    user = User.query.filter_by(email=email).first()
    try:
        phonenumberverification = phonenumbers.parse(phonenumber)
    except:
        flash('Invalid phone number (Ex: +65 1234 5678)⠀⠀')
        return redirect(url_for('signup'))
    if not phonenumbers.is_possible_number(phonenumberverification):
        flash('Invalid phone number (Ex: +65 1234 5678)⠀⠀')
        return redirect(url_for('signup'))
    if confirmpassword != password:
        flash('Passwords do not match⠀⠀')
        return redirect(url_for('signup'))     
    if user:
        flash('Email address already exists⠀⠀')
        return redirect(url_for('signup'))
    email_list = [*email]
    if "@" not in email_list or "." not in email_list:
        flash('Email must contain "@" and "."⠀⠀')
        return redirect(url_for('signup'))
    if len([*password]) <=7:
        flash('Password must be at least 8 characters long⠀⠀')
        return redirect(url_for('signup'))

    new_user = User(email=email, firstname=firstname, lastname=lastname,
    password=generate_password_hash(password,method='sha-256'),phonenumber=phonenumber)

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
    email_list = [*email]
    if "@" not in email_list or "." not in email_list:
        flash('Email must contain "@" and "."⠀⠀')
        return redirect(url_for('login'))
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    login_user(user)
    return redirect(url_for("home"))
@app.route("/home")
@login_required
def home():
    routes = Route.query.filter_by(rider=current_user.email).all()
    return render_template("home.html",routes=routes)

# Updated home_post route handler
@app.route("/home", methods=["POST"])
@login_required
def home_post():
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    user = current_user
    rider_email = user.email
    routes = Route.query.filter_by(rider=current_user.email).all()
    #xy coords
    locations = {
        "UberLand Shopping Complex": [1,0],
        "UberLand Middle School": [-1,4],
        "UberLand Airport": [5,1],
        "UberLand Bus Interchange": [-3,1],
        "UberLand Food Centre": [-4,-1],
        "UberLand Swimming Complex": [2,2],
        "UberLand Estates": [-4,3],
        "UberLand Country Club": [1,0]
            }
    distance = (locations[origin][0]**)-(locations[destination][0]**)+(locations[origin][1]**)-(locations[destnation][1]**)
    distance.sqrt()
    print(distance)
    eta = distance*2+2
    print(eta)
    if origin == destination:
        flash('Not allowed to have the same origin and destination. Please try again')
    elif routes != []:
        flash('You are not allowed to have more than one route. Please try again')
    else:
        new_route = Route(
            origin=origin,
            destination=destination,
            driver="None",
            rider=rider_email,
            eta = eta,
            distance = distance
        )
        db.session.add(new_route)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for("index"))

@app.route("/cancel_route")
@login_required
def cancel_route():
    try:
        route_to_cancel = Route.query.get(current_user.email)
        if route_to_cancel.rider == current_user.email:
            db.session.delete(route_to_cancel)
            db.session.commit()
    except:
        return redirect(url_for("home"))
    return redirect(url_for("home"))

# Replit required code to run
if __name__ == "__main__":
    app.run(host="172.20.10.2",debug=True)
