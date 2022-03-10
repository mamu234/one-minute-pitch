from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import Users



class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')