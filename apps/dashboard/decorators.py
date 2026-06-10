from functools import wraps

from django.contrib.auth.views import redirect_to_login

DASHBOARD_LOGIN_URL = '/dashboard/connexion/'


def manager_required(view_func):
    """Accès réservé aux comptes staff (gérants)."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return redirect_to_login(request.get_full_path(), login_url=DASHBOARD_LOGIN_URL)
    return wrapper
