import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import osmapi as osm , bs4 as bs , openrouteservice as ors , math
ors_key = "5b3ce3597851110001cf62488f97a0c484214cacb893f3be729f251a"

db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.Integer)

class Driver(db.Model):
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    phonenumber = db.Column(db.Integer, nullable = False)
    vehiclenumber = db.Column(db.String(100), nullable = False)
    peopleallowedtocarry = db.Column(db.Integer, nullable = False)
    model = db.Column(db.String(100), nullable = False)
    seats = d
    def __init__(self,fn,ln,a,pn,vn,p,n,m,s):
        self.info = {"First Name":fn,"Last Name":ln,"Age":a,
                    "Phone Number":pn,"Vehicle Number":vn,"People":p,"Notice":n}
        self.vehicle = {"Model":m,"Seats":s}
    def return_info(self):
        return self.info
    def return_vehicle(self):
        return self.vehicle
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.info
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.vehicle

def add_driver(Driver,fn,ln,a,pn,vn,p,n,m,s):
    return Driver(fn,ln,a,pn,vn,p,n,m,s)


class Rider:
    def __init__(self,fn,ln,a,pn):
        self.info = {"First Name":fn,"Last Name":ln,"Age":a,
                    "Phone Number":pn}
    def return_info(self):
        return self.info
    def change_info(self,content,index):
        self.info.insert(content,index)
        self.info.pop(index+1)
        return self.info

def make_rider(Rider,fn,ln,a,pn):
    return Rider(fn,ln,a,pn)

# coords use long1,lat1,long2,lat2
class Route:
    def __init__(self,lo1,la1,lo2,la2,driver,rider):
        self.lo1 = lo1
        self.la1 = la1
        self.la2 = la2
        self.lo2 = lo2
        self.formatted = ((lo1,la1),(lo2,la2))
        self.driver = driver
        self.rider = rider
    def setup_routes(self):
        try:
            client = ors.Client(key=ors_key)
            self.routes = client.directions(self.formatted)
            return True
        except:
            return False
    def return_duration(self):
        return math.ceil(self.routes['routes'][0]['summary']['duration']/60*100)/100
    def return_distance(self):
        return math.ceil(self.routes['routes'][0]['summary']['distance']/1000*1000)/1000

def make_route(lo1,la1,lo2,la2,driver,rider):
    return Route(lo1,la1,lo2,la2,driver,rider)
