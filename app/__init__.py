from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost/database" # needs to be modified
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # some kind of warning suppression

app.config['UPLOAD_FOLDER'] = "./static/uploads/" # user image upload folder location
app.config['POSTS_FOLDER'] = "./static/posts/" # posts image upload folder location

db = SQLAlchemy(app)

# flask login bs
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # critial to the location of our views.py login entry.

app.config.from_object(__name__) # idk why, but just to be safe.
from app import views