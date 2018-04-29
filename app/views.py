"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

# added a bunch of imports for functionality
import os
from datetime import datetime
from app import app, db, login_manager
from flask import render_template, request, redirect, flash, session, abort, url_for, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from forms import LoginForm, registerForm, postForm
from models import UserProfile, Posts, Likes, Follows

###
# Routing for your application.
###

@app.route('/api/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like(post_id):
    rows = db.session.query(Likes).count()
    l = Likes(lid=rows, uid=session['id'], pid=post_id)
    db.session.add(l)
    db.session.commit()
    return 0

@app.route('/api/users/<int:users_id>/follow', methods=['POST'])
@login_required
def follow(users_id):
    rows = db.session.query(Follows).count()
    f = Follows(fid=rows, uid=users_id, fol_id=session['id'])
    db.session.add(f)
    db.session.commit()
    return '{"status":"OK", "msg":"success"}'

@app.route('/api/users/<int:users_id>/posts', methods=['GET'])
@login_required
def user(users_id):
    print "requested id=%d", users_id
    prof = UserProfile.query.filter_by(u_id=users_id).first()
    if prof:
        json = '{"user_id":'+str(users_id)+', "username":"'+prof.username+'", "fname":"'+prof.fname+'", "lname":"'+prof.lname+'", "loc":"'+prof.loc+'", "email":"'+prof.email+'", "bio":"'+prof.bio+'", "joined":"'+prof.joined+'", "image":"'+app.config['UPLOAD_FOLDER']+prof.profImg+'"'
        posts = Posts.query.filter_by(user_id=users_id).all()
        json = json + ', "post":{"posts":['
        for i in xrange(0, len(posts)-1):
            s = '{"id":'+str(posts[i].p_id)+', "user":'+str(posts[i].user_id)+', "image":"'+app.config['POSTS_FOLDER']+posts[i].img+'", "caption":"'+posts[i].capt+'", "date":"'+posts[i].created+'"}'
            if i != len(posts)-2:
                s = s + ','
            json = json + s
        json = json + ']}'
        return jsonify(status="OK", msg=json)
    return '{status"":"OK", "msg":"user not found."}'

@app.route('/api/users/<int:users_id>/posts', methods=['POST'])
@login_required
def post(users_id):
    postf = postForm()
    if post.validate_on_submit():
        img = postf.photo.data
        capt = postf.capt.data
        filename = secure_filename(img.filename)
        img.save(app.config['POSTS_FOLDER']+filename)
        rows = db.session.query(Posts).count()
        cdate = datetime.now().strftime("%Y-%m-%d")
        post = Posts(pid=rows, uid=users_id, img=filename, cdate=cdate, caption=capt)
        db.session.add(post)
        db.session.commit()
        flash('Post made.', 'success')
        return '{"status":"OK", "msg":"success"}'
    return '{"status":"OK", "msg":"failed to validate form."}'

@app.route('/api/posts', methods=['GET'])
@login_required
def explore():
    posts = db.session.query(Posts).all()
    json = '{"status":"OK", ['
    for i in xrange(0, len(posts)-1):
        s = '{"id":'+str(posts[i].p_id)+', "user":'+str(posts[i].user_id)+', "image":"'+app.config['POSTS_FOLDER']+posts[i].img+'", "caption":"'+posts[i].capt+'", "date":"'+posts[i].created+'"}'
        if i != len(posts)-2:
            s = s + ','
        json = json + s
    json = json + ']}'
    return jsonify(status="OK", data=json)

@app.route('/api/auth/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        pw = form.password.data
        q = UserProfile.query.filter_by(username=name, passcode=pw).first()
        if q is None:
            return jsonify({"status":"OK", "msg":"failed to authenticate credentials"})
        login_user(q)
        flash('Login Successful', 'success')
        """n = request.args.get('next')
        if not is_safe_url(n):
            return jsonify({"status":"OK", "msg":"success"})"""
        session['logged_in'] = True
        session['uid'] = q.u_id
        return redirect(url_for('index'))
    return '{"status":"OK", "msg":"failed to validate form"}'

@login_manager.user_loader
def load_user(user):
    return UserProfile.query.filter_by(username=user).first()

@app.route('/api/auth/check')
def chec():
    auth = False
    id = -1
    if session.get('logged_in'):
        auth = session['logged_in']
    if session.get('uid'):
        id = session['uid']
    return jsonify(status="OK", auth=auth, id=id)

@app.route('/api/auth/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    session.pop('logged_in', None)
    session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/api/users/register', methods=['POST'])
def register():
    prof = registerForm()
    if prof.validate_on_submit():
        pw = prof.passcode.data
        if pw != request.form['passcodeC']:
            flash('Passwords do NOT match.', 'error')
            return redirect(url_for('index'))
        img = prof.img.data
        if img:
            filename = secure_filename(img.filename)
            img.save(app.config['UPLOAD_FOLDER']+filename)
        else:
            filename = "./static/default/default profile.jpg"
        fname = prof.fname.data
        lname = prof.lname.data
        uname = prof.username.data
        bio = prof.bio.data
        location = prof.location.data
        email = prof.email.data
        cdate = datetime.now().strftime("%Y-%m-%d")
        rows = db.session.query(UserProfile).count()
        profile = UserProfile(u_id=(rows + 1), username=uname, fname=fname, lname=lname, passcode=pw, email=email, loc=location, bio=bio, profImg=filename, joined=cdate)
        db.session.add(profile)
        db.session.commit()
        flash('Registration Successful', 'success')
        return jsonify({"msg":"registered"})
    else:
        flash_errors(prof)
        return jsonify({"errors": form_errors(prof)})

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/')
def index():
    """Render website's initial page and let VueJS take over."""
    return render_template('index.html')


# Here we define a function to collect form errors from Flask-WTF
# which we can later use

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
