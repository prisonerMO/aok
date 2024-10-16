"""
Importing:
models base from django
models from communities
aok app model base from aok.common
"""
from django.db import models
from communities.models import Member
from aok.common import BaseModelAOK



class New(BaseModelAOK):
    """
    Model for News. Columns:
    datetime (DateTime): When new is added
    member (FK Member): Name who added the new
    new (TextField): Text content of the new
    """
    datetime =              models.DateTimeField(verbose_name="Lisätty")
    member =                models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="Lisääjä")
    new =                   models.TextField(verbose_name="Sisältö")
