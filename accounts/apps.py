from django.apps import AppConfig
import os

class AccountsConfig(AppConfig):
    name = 'accounts'



def ready(self):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    if email and not User.objects.filter(email=email).exists():
        User.objects.create_superuser(
            username="admin",
            email=email,
            password=password
        )