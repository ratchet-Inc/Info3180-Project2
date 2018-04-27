# classes needs to be completed/adjusted, current setup is for the views! (drake pun.... get it?)

from app import db

class UserProfile(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    fname = db.Column(db.String(32))
    lname = db.Column(db.String(32))
    passcode = db.Column(db.String(256))
    email = db.Column(db.String(128), unique=True)
    loc = db.Column(db.String(64))
    bio = db.Column(db.String(128))
    profImg = db.Column(db.String(64))
    joined = db.Column(db.String(16))
    
    def is_authentic(self):
        return True
    def is_active(self):
        return False
    def get_id(self):
        return str(self.u_id) # python 2 specific, i think
    
    def __repr__(self):
        return '<User %r>' % (self.username)

class Post(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    img = db.Column(db.String(64))
    capt = db.Column(db.String(128))
    created = db.Column(db.String(16))
    
    def __repr__(self):
        return '<Post %r>' % (self.p_id)

class Likes(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Like %r>' % (self.l_id)
        
class Follow(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Follow %r>' % (self.f_id)