from django.db import models
from communities.models import Member



class BaseModel(models.Model):
    """
    For future abstraction.
    """
    class Meta:
        abstract=True # specify this model as an Abstract Model
        app_label = 'aok'



class New(BaseModel):
    datetime =              models.DateTimeField(verbose_name="Lisätty")
    member =                models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="Lisääjä")
    new =                   models.TextField(verbose_name="Sisältö")

    class Meta:
        app_label = "aok"
