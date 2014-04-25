from gantt.app import app

@app.route('/')
def homepage():
    if user.is_authenticated():
        return render_template('homepage.html')
    else:
        return render_template('auth/login.html')
