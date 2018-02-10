from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ProfileForm(FlaskForm):
    myChoices = [('', ''), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Mis.', 'Mis.')]
    salutation = SelectField('Salutation', choices=myChoices)
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    birthday = DateField('Date of Birth', format='%m/%d/%Y')
    submit = SubmitField('Submit')
