import os
import env
from config import Config
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config["MONGO_DB"] = "awesome-reads"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config.from_object('config.Config')
#from app import routes

bootstrap = Bootstrap(app)

mongo = PyMongo(app)

# MAIN PAGE
@app.route('/')
@app.route('/home') # chnaged for setting up
def home():
    return render_template('home.html', title='Awesome-Reads')
                            #users=mongo.db.users.find())

@app.route('/user/<username>')
#@login_required
def user(username):
    users = mongo.db.users.find_one()
    return render_template('user.html', user=user, title='Profile')
                            

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    #return render_template('user.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome Back {form.username.data}, theres loads of new books to enjoy!', 'success')
        return redirect(url_for('home')) 
    else:
        flash('Login Failed. Check yo\'self', 'danger')
        return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
