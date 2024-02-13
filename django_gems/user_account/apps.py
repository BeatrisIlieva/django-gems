from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_gems.user_account'

    def ready(self):
        import django_gems.user_account.signals
        result = super().ready()
        return result
