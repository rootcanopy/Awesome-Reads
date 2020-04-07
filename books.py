import os
import env
from config import Config
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)

#app.config["MONGO_DB"] = "awesome-reads"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config.from_object(Config)
#from app import routes

bootstrap = Bootstrap(app)

mongo = PyMongo(app)

# MAIN PAGE
@app.route('/')
@app.route('/home') # chnaged for setting up
def home():
    return render_template('home.html', title="Awesome-Reads")
                            #users=mongo.db.users.find())

@app.route('/user')
#@login_required
def user():
    return render_template('user.html', username=['username'],
                            user = mongo.db.users.find())

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm
    return render_template('login.html', title="Login", form=form)
    

if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)