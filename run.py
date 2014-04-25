from gantt.app import app

if __name__ == "__main__":
    # Import the views.
    from gantt.apps.auth.views import *
    from gantt.apps.site.views import *

    app.run()
