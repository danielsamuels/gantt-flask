from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class RegistrationForm(Form):

    organisation_name = StringField(
        'Organisation name',
        validators=[
            DataRequired()
        ]
    )

    first_name = StringField(
        'First name',
        validators=[
            DataRequired()
        ]
    )

    last_name = StringField(
        'Last name',
        validators=[
            DataRequired()
        ]
    )

    email_address = StringField(
        'Email address',
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
