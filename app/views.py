"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

# added a bunch of imports for functionality
import os, datetime
from app import app, db, login_manager
from flask import render_template, request, redirect, flash, session, abort, url_for, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from forms import LoginForm, registerForm, postForm
from models import UserProfile, Posts, Likes, Follow

###
# Routing for your application.
###

@app.route('/api/users/register', methods=['POST'])
def register():
    prof = registerForm()
    if prof.validate_on_submit():
        flash('File Saved', 'success')
        img = prof.img.data
        filename = secure_filename(img.filename)
        fname = prof.fname.data
        lname = prof.lname.data
        uname = prof.username.data
        pw = prof.passcode.data
        bio = prof.bio.data
        location = prof.loc.data
        email = prof.email.data
        img.save(app.config['UPLOAD_FOLDER']+filename)
        rows = db.session.query(UserProfile).count()
        profile = UserProfile(u_id=(rows + 1), username=uname, fname=fname, lname=lname, passcode=pw, email=email, loc=location, bio=bio, profImg=filename, joined=now.strftime("%Y-%m-%d"))
        db.session.add(profile)
        db.session.commit()
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
