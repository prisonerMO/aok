from django.db import models
from communities.models import Member


class New(models.Model):
    datetime =              models.DateTimeField(verbose_name="Lisätty")
    member =                models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="Lisääjä")
    new =                   models.TextField(verbose_name="Sisältö")
