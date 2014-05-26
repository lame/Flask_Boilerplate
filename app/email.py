from app import mail
from flask.ext.mail import Message
from decorators import async
from flask import render_template
from config import ADMINS

def user_notification(user):
    send_email("Email for Flask Boilerplate" % user.name,
        ADMINS[0],
        [user.name],
        render_template("new_user_email.txt", 
            user = user))

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    send_async_email(msg)
