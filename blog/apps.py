from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Creates the configuration for the blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
