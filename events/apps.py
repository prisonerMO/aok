"""
Importing:
AppConfig base from Django apps module
"""
from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    App Config for Events
    default auto field: BigAutoField
    name: 'events'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
