"""
Importing:
AppConfig base from Django apps module
"""
from django.apps import AppConfig


class CommunitiesConfig(AppConfig):
    """
    App Config for Communities
    default auto field: BigAutoField
    name: 'communities'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'communities'
