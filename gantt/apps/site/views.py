from flask import render_template, redirect, url_for

from gantt.app import app
from gantt.auth import user


@app.route('/')
def homepage():
    if not user.is_authenticated():
        # Redirect to the login page.
        return redirect(url_for('login'))

    return render_template('homepage.html')
