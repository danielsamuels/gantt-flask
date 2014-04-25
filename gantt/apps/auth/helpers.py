def create_tables():
    from .models import Organisation, Project, User, TimelineItem, Session

    Organisation.create_table()
    Project.create_table()
    User.create_table()
    Session.create_table()
    TimelineItem.create_table()


# Originally taken from django.utils.crypto
def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    from gantt import app

    import random
    import time

    random.seed(
        hashlib.sha256(
            ("%s%s%s" % (
                random.getstate(),
                time.time(),
                app.config['SECRET_KEY'])
            ).encode('utf-8')
        ).digest()
    )

    return ''.join([random.choice(allowed_chars) for i in range(length)])
