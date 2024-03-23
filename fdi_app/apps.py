from django.apps import AppConfig


class FdiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fdi_app'

    def ready(self):
        import fdi_app.signals
