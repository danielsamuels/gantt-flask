from gantt.app import db
from peewee import *

from .helpers import get_random_string

import datetime


class Organisation(db.Model):

    name = CharField()


class User(db.Model):

    organisation = ForeignKeyField(
        Organisation,
    )

    first_name = CharField()

    last_name = CharField()

    email_address = CharField(
        unique=True,
        index=True,
        primary_key=True,
    )

    password = CharField()

    join_date = DateTimeField(
        default=datetime.datetime.now
    )

    def new_session(self):
        return Session.create(
            user=self,
            key=get_random_string(64)
        )


class Session(db.Model):

    user = ForeignKeyField(
        User,
    )

    key = CharField(

    )

    def get_user(self):
        return self.user

class Project(db.Model):

    organisation = ForeignKeyField(
        Organisation,
    )

    name = CharField()


class TimelineItem(db.Model):

    organisation = ForeignKeyField(
        Organisation,
    )

    user = ForeignKeyField(
        User,
    )

    project = ForeignKeyField(
        Project,
    )

    start_date = DateField()

    end_date = DateField()

    description = TextField(
        null=True,
    )
