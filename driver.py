import os
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


class Driver(db.Model):
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
