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
        return '%r' % (self.username)
    def __init__(self, u_id, username, fname, lname, passcode, email, loc, bio, profImg, joined):
        self.u_id = u_id
        self.username = username
        self.fname = fname
        self.lname = lname
        self.passcode = passcode
        self.email = email
        self.loc = loc
        self.bio = bio
        self.profImg = profImg
        self.joined = joined

class Posts(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    img = db.Column(db.String(64))
    capt = db.Column(db.String(128))
    created = db.Column(db.String(16))
    
    def __repr__(self):
        return '<Post %r>' % (self.p_id)
    def __init__(self, pid, uid, img, caption, cdate):
        self.p_id = pid
        self.user_id = uid
        self.img = img
        self.capt = caption
        self.created = cdate

class Likes(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Like %r>' % (self.l_id)
    def __init__(self, lid, uid, pid):
        self.l_id = lid
        self.user_id = uid
        self.post_id = pid
        
class Follow(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Follow %r>' % (self.f_id)
    def __init__(self, fid, uid, fol_id):
        self.f_id = fid
        self.user_id = uid
        self.follower_id = fol_id