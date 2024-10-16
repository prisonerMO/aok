"""
Importing:
AppConfig base from Django apps module
"""
from django.apps import AppConfig


class NewsConfig(AppConfig):
    """
    App Config for News
    default auto field: BigAutoField
    name: 'news'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
