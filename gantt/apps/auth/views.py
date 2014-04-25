from flask import render_template, request

from gantt.app import app
from gantt.auth import user

from .forms import RegistrationForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if user.is_authenticated():
        # Redirect to the homepage, they don't need to log in.
        pass
    else:
        return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if user.is_authenticated():
        # Redirect to the homepage, they don't need to register.
        pass
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            user.create_user(
                email_address=request.form['email_address'],
                password=request.form['password'],
            )

            user.login(request.form['email_address'], request.form['password'])
            return redirect('/')

        return render_template('auth/register.html', form=form)
