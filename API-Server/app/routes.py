from flask import render_template, flash, redirect

from app import app
from app.forms import LoginForm, ProfileForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'testerver'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'This is a test A!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'This is a test B!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process log in
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        # Process log in
        flash('User profile updated  Salutation={}, First={}, Last={}, DOB={}'.format(
            form.salutation.data, form.firstname.data, form.lastname.data, form.birthday.data))
        return redirect('/index')
    return render_template('profile.html', title='User Profile', form=form)
