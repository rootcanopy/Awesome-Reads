import env
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# APP REGISTRATION FORM
class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    
    email = StringField('Email Address', validators=[DataRequired(), Email()])  
    
    password = PasswordField('Password')
    
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match!")])
    
    submit = SubmitField('Sign Up!')

# LOGIN TO APP
class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])  
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me!', default=True)
    
    submit = SubmitField('Log Me In!')