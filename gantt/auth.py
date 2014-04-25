# Import auth modules.
from .apps.auth.auth import Auth
from .apps.auth.models import User

user = Auth(User)

