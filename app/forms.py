# classes can also be adjusted and modified

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('passcode', validators=[InputRequired()])

class registerForm(FlaskForm):
    fname = StringField('firstName', validators=[InputRequired()])
    lname = StringField('lastName', validators=[InputRequired()])
    username = StringField('userName', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    bio = StringField('bio', validators=[InputRequired()])
    img = FileField('profilePicture', validators=[FileAllowed(['jpeg', 'jpg', 'png'], 'Images only!')])
    email = StringField('userEmail', validators=[InputRequired(), Email()])
    passcode = StringField('password', validators=[InputRequired()])
    
class postForm(FlaskForm):
    photo = FileField('PostImage', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    capt = StringField('PostCaption', validators=[InputRequired()])