from flask import render_template,request,redirect,url_for
from app import main
from requests import views
from forms import ReviewForm
from models import Review





# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):

    form = ReviewForm()

   

        