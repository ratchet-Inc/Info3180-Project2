from os.path import join, dirname, realpath
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'v\xf9\xf7\x11\x13\x18\xfaMYp\xed_\xe8\xc9w\x06\x8e\xf0f\xd2\xba\xfd\x8c\xda'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:1234@localhost/project2db" # needs to be modified
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # some kind of warning suppression
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jywbykmldqworr:ded89bd565bccfacf40b47c867ac8ba0594d45dd3d72f5a50066af83440ad4d2@ec2-23-23-142-5.compute-1.amazonaws.com:5432/ddir1kqhhc1ap4'

app.config['UPLOAD_FOLDER'] = join(dirname(realpath(__file__)), 'static/uploads/') # user image upload folder location
app.config['POSTS_FOLDER'] = join(dirname(realpath(__file__)), 'static/posts/') # posts image upload folder location

db = SQLAlchemy(app)

# flask login bs
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # critial to the location of our views.py login entry.
login_manager.session_protection = "strong"
login_serializer = URLSafeTimedSerializer(app.secret_key)

csrf = CSRFProtect(app)
WTF_CSRF_ENABLED = True

app.config.from_object(__name__) # idk why, but just to be safe.
from app import views