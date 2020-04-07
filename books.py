import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

#app.config["MONGO_DB"] = "awesome-reads"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)

# MAIN PAGE
@app.route('/')
@app.route('/home') # chnaged for setting up
def home():
    return render_template('home.html')
                            #users=mongo.db.users.find())

@app.route('/user')
#@login_required
def user():
    return render_template('user.html', username=['username'],
                            user = mongo.db.users.find())

@app.route('/login')
def login():
    return render_template('login.html')
    

if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)