from flask.ext.wtf import Form, fields, validators, widgets
from flask.ext.wtf import Required, Email, ValidationError
from models import User
from app import db

def validate_login(form, field):
    user = form.get_user()
    
    if user is None:
        raise validators.ValidationError('Invalid user')

    # if user.consent is False:
    #     raise validators.ValidationError('Registration cannot be completed withouth consent')

    if user.password != form.password.data:
        raise validators.ValidationError('Invalid password')

class LoginForm(Form):
    name = fields.TextField(validators=[Required(), Email()])
    password = fields.PasswordField(validators=[Required(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()

class RegistrationForm(Form):
    name = fields.TextField('Email Address', validators=[Required(), Email()])
    password = fields.PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])

    def validate_name(self, field):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise validators.ValidationError('Duplicate name')

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')

