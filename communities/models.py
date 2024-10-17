"""
Importing:
models base from django
aok app model base from aok.common
"""
from django.db import models
from aok.common import BaseModelAOK

#Rank levels for members. Used by classes Rank and VRank.
RANK_CLASSES = {
    20: 'Alokas',
    40: 'Miehistö',
    60: 'Aliupseeri',
    80: 'Upseeri',
    200: 'Kenraali',
}



class Rank(BaseModelAOK):
    """ Ranks for members. Used by class Members """
    rankname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Arvo")
    rankappr = models.CharField(max_length=20, blank=True, null=True, verbose_name="Lyhenne")
    rankvalue = models.IntegerField(choices=RANK_CLASSES, blank=True, verbose_name="Luokka")

    def __str__(self):
        return f"{self.rankappr}"

    class Meta:
        db_table = 'aok.rank'



class VRank(BaseModelAOK):
    """ Virtual ranks for Members. Used by class Members """
    rankname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Nimike")
    rankappr = models.CharField(max_length=20, blank=True, null=True, verbose_name="Lyhenne")
    rankvalue = models.IntegerField(choices=RANK_CLASSES, blank=True, verbose_name="Luokka")

    def __str__(self):
        return f"{self.rankappr}"

    class Meta:
        db_table = 'aok.vrank'



class Community(BaseModelAOK):
    """ Communities. Used by class Members """
    name = models.CharField(max_length=30, verbose_name="Yhteisö")
    shortname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Lyhyt nimi")
    description = models.TextField(blank=True, null=True, verbose_name="Kuvaus")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'aok.community'



class Member(BaseModelAOK):
    """ Members. Uses classes Rank, VRank, Community """
    nickname = models.CharField(max_length=30, verbose_name="Nimimerkki")
    firstname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Etunimi")
    lastname = models.CharField(max_length=30, blank=True, null=True, verbose_name="Sukunimi")
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Arvo")
    vrank = models.ForeignKey(VRank, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Virt.arvo")
    community = models.ManyToManyField(Community)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nickname}"

    class Meta:
        db_table =  'aok.member'
