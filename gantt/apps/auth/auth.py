from flask import session

"""
We handle user authentication state with session keys.  When a user authenticates
on the system we generate a session and assign it to their User object.  This session
ID is stored in a cookie and checked when the user requests a page.
"""

SESSION_KEY = 'sessionid'

class Auth(object):

    def __init__(self, model=None):
        if not model:
            raise Exception('You need to supply a model to the Auth library.')
        self.model = model

    # Create a new user with the given parameters.
    def create_user(self, **kwargs):
        return self.model.create(**kwargs)

    # Given an email address and password, attempt to log in the user.
    def login(self, email_address, password):
        pass

    # Get the user object (or None if they are not authenticated)
    def get_user(self):
        pass

    # Check the session token for validity. Returns boolean.
    def is_authenticated(self):
        if session.get(SESSION_KEY):
            # Check the session ID in the database.
            print True
        else:
            print False
