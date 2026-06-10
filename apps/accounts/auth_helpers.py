from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

MODEL_BACKEND = 'django.contrib.auth.backends.ModelBackend'


def authenticate_user(identifier, password, request=None):
    """Authentifie par identifiant ou email."""
    user = authenticate(request, username=identifier, password=password)
    if user is None and '@' in identifier:
        try:
            account = User.objects.get(email__iexact=identifier.strip())
            user = authenticate(request, username=account.username, password=password)
        except User.DoesNotExist:
            pass
    return user


def is_staff_account(user):
    return user.is_authenticated and user.is_staff


def login_account(request, user):
    """Connexion session avec le backend Django standard."""
    login(request, user, backend=MODEL_BACKEND)
