import os
import env
from config import Config
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config["MONGO_DB"] = "awesome-reads"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config.from_object('config.Config')


bootstrap = Bootstrap(app)
mongo = PyMongo(app)


# MAIN PAGE
@app.route('/')
def base():
    return render_template('base.html', title='Awesome-Reads')
                            

@app.route('/home')
def home():
    return render_template('home.html', title='Awesome-Reads')

@app.route('/books')
def books():
    return render_template('books.html', title='Search Books')


@app.route('/user/<username>')
#@login_required
def user(username):
    users = mongo.db.users.find_one()
    return render_template('user.html', user=user, title='Profile')
                            

@app.route('/register', methods=['GET', 'POST'])
def register():
    # registration form function
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        users = mongo.db.users
        # checks if we already have the enterered user
        existing_user = users.find_one({'username': request.form['username']})


        if exisitng_user is None:
            # encrypt the password
            hash_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # register the user in mongo
            users.insert_one({'name': request.form['username'],
                            'password': password_hash,
                            'email': request.form['email']})
            session['username'] = request.form['username']
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('user'))
        else:
            flash('Registration Failed. Check yo\'self, please try again!', 'danger')
            return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users.find_one()
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome Back {form.username.data}, theres loads of new books to enjoy!', 'success')
        return redirect(url_for('user.html')) 
    else:
        flash('Login Failed. Check yo\'self', 'danger')
        return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
