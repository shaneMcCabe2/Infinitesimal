from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email, Length
#from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    phone = StringField('Phone number', validators=[DataRequired()])
    body = TextAreaField('How can we help you?', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit')