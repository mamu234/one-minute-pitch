from flask import render_template,request,redirect,url_for, abort
from . import main ,Pitches
from ..models import Users


@main.route('/')
def index():
    pitches = Pitches.query.all()
    return render_template('index.html',pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = Users.query.filter_by(username = uname).first()
    # user_id = current_user._get_current_object().id
    # posts = Pitches.query.filter_by(user_id = user_id).all()

    if user is None:
        abort(404)

