from gantt.app import app, user

@app.route('/register')
def register():
    if user.is_authenticated():
        # Redirect to the homepage, they don't need to register.
        pass
    else:
        return render_template('auth/register.html')
