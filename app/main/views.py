from flask import render_template,request,redirect,url_for
from . import main
from ..models import Users


@main.route('/')
def index():

 return render_template('index.html')

