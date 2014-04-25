from gantt.app import db
from peewee import *

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


class Session(db.Model):

    user = ForeignKeyField(
        User,
    )

    value = CharField(

    )


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
