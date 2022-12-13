from flask import render_template # invokes jinja2 template engine
from flask import flash, redirect, url_for
from app import app
from app.forms import ContactForm

@app.route('/')
@app.route('/index') # decorators
def index(): # decorators will call this function
    user = {'username': 'Mario Incandenza'} # mock user
    posts = [
        {
            'author': {'username': 'Schitt'},
            'body': 'Beautiful day to be alive!'
        },
        {
            'author': {'username': 'Lyle'},
            'body': 'The sweat is dense in this one.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)        

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Contact data submitted for {} {}'.format(
            form.first_name.data, form.last_name.data))
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact Us', form=form)