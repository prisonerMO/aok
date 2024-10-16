"""
Importing:
models base from django
"""
from django.db import models



class BaseModelAOK(models.Model):
    """
    For future abstraction.
    Used as base for aok app models.
    app_label: aok
    db_table: aok.table_name
    """
    class Meta:
        abstract = True # specify this model as an Abstract Model
        app_label = 'aok'
#        db_table = 'aok.' + str(__name__.split('.', 1)[1]).lower()
