from flask import Flask
from flask_peewee.db import Database

from .apps.auth.auth import Auth

app = Flask(__name__)
app.config.from_object('gantt.settings.Configuration')

db = Database(app)

# Import the views.
from .apps.auth.views import *
from .apps.site.views import *

from .apps.auth.auth import Auth
from .apps.auth.models import User

user = Auth(User)
