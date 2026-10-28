from django.contrib.auth import get_user_model
from django.db.models import Q


def is_email_taken(email: str) -> bool:
    """Emails are the login username, so they must be unique across all roles."""
    User = get_user_model()
    return User.objects.filter(Q(email__iexact=email) | Q(username__iexact=email)).exists()
