from django.db import models
from communities.models import Community, Member
from datetime import timedelta



class BaseModel(models.Model):
    """
    For future abstraction.
    """
    class Meta:
        abstract=True # specify this model as an Abstract Model
        app_label = 'aok'



class Radio(BaseModel):
    name =                  models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

#class MemberPerRole(BaseModel):
#    player =                models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name = "Pelaaja")

class OpRole(BaseModel):
    rolename =              models.CharField(max_length=40, verbose_name="Rooli")
    radio =                 models.ForeignKey(Radio, on_delete=models.DO_NOTHING, verbose_name = "Radio")
    radionick =             models.CharField(max_length=20, blank=True, verbose_name="Radiokutsu")
    player =                models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="Pelaaja")

    def __str__(self):
        return str(self.rolename) + " " + str(self.radionick)



class OpRoleBox(BaseModel):
    """ Main level of unit "boxes". 
    There can be multiple SL's in multiple units... """
    name =                  models.CharField(max_length=40, verbose_name="Yksikkö")
    oprole =                models.ManyToManyField(OpRole, blank=True, verbose_name="Roolit")

    def __str__(self):
        return f"{self.name}"



class Event(BaseModel):
    """ Event data. Uses models: community.Community, OpRoleBox    """
    published =             models.BooleanField(verbose_name="Julkaistu")
    op_name =               models.CharField(max_length=100, blank=True, null=True, verbose_name="Operaation nimi")
    op_organizer =          models.ForeignKey(Community, on_delete=models.DO_NOTHING, verbose_name = "Järjestäjä")
    op_map =                models.CharField(max_length=40, blank=True, null=True, verbose_name="Kartan nimi")
    op_startdatetime =      models.DateTimeField(blank=True, null=True, verbose_name="Tehtävän aloitus")
    op_duration =           models.TimeField(blank=True, null=True, verbose_name="Tehtävän kesto")
    op_slotopendatetime =   models.DateTimeField(blank=True, null=True, verbose_name="Slottaus aukeaa")
    op_slottingcheckdatetime = models.DateTimeField(blank=True, null=True, verbose_name="Slottaus tarkastus")
    plandatetime =          models.DateTimeField(blank=True, null=True, verbose_name="Suunnittelun aloitus")
    planduration =          models.TimeField(blank=True, null=True, verbose_name="Suunnittelun kesto")
    op_modpreset =          models.TextField(blank=True, null=True, verbose_name="Modpreset")
    server_a3address =      models.CharField(max_length=100, blank=True, null=True, verbose_name="Arma3 palvelin")
    server_a3port =         models.CharField(max_length=100, blank=True, null=True, verbose_name="Arma3 portti")
    server_a3pwd =          models.CharField(max_length=100, blank=True, null=True, verbose_name="Arma3 salasana")
    server_tsaddress =      models.CharField(max_length=100, blank=True, null=True, verbose_name="TeamSpeak palvelin")
    server_tsport =         models.CharField(max_length=100, blank=True, null=True, verbose_name="TeamSpeak portti")
    server_tspwd =          models.CharField(max_length=100, blank=True, null=True, verbose_name="TeamSpeak salasana")
    op_rolebox =            models.ManyToManyField(OpRoleBox, blank=True, verbose_name="Yksikkö")
    op_minplayers =         models.IntegerField(blank=True, null=True, verbose_name="Pelaajamäärä minimi")
    op_maxplayers =         models.IntegerField(blank=True, null=True, verbose_name="Pelaajamäärä maksimi")
    op_spec_datetime =      models.DateTimeField(blank=True, null=True, verbose_name="Tehtävän ajankohta")
    op_spec_weather =       models.TextField(blank=True, null=True, verbose_name="Sää")
    op_rules =              models.TextField(blank=True, null=True, verbose_name="Säännöt")
    op_situation =          models.TextField(blank=True, null=True, verbose_name="Tilanne")
    op_spec_friedlies =     models.TextField(blank=True, null=True, verbose_name="Omat joukot")
    op_spec_enemies =       models.TextField(blank=True, null=True, verbose_name="Viholliset")
    op_spec_civilians =     models.TextField(blank=True, null=True, verbose_name="Siviilit")
    op_spec_roe =           models.TextField(blank=True, null=True, verbose_name="Tulenavaussäännöt")
    op_spec_assets =        models.TextField(blank=True, null=True, verbose_name="Oma kalusto")
    op_spec_mission =       models.TextField(blank=True, null=True, verbose_name="Tehtävä")
    op_spec_proceeding =    models.TextField(blank=True, null=True, verbose_name="Toteutus")
    op_spec_supports =      models.TextField(blank=True, null=True, verbose_name="Huolto")
    op_spec_comms =         models.TextField(blank=True, null=True, verbose_name="Johto ja viestintä")

    def __str__(self):
        return f"{self.op_name}"

    def op_startdate(self):
        if(self.op_startdatetime):
            return str(self.op_startdatetime.strftime("%d.%m.%Y"))
        return ""

    def op_starttime(self):
        if(self.op_startdatetime):
            return str(self.op_startdatetime.strftime("%H:%M"))
        return ""

    def op_endtime(self):
        if(self.op_startdatetime and self.op_duration):
            return str((self.op_startdatetime + timedelta(hours=int(self.op_duration.strftime("%H")),minutes=int(self.op_duration.strftime("%M")))).strftime("%H:%M"))
        return ""

    def planstarttime(self):
        if(self.plandatetime):
            return str(self.plandatetime.strftime("%H:%M"))
        return ""

    def planendtime(self):
        if(self.plandatetime and self.planduration):
            return str((self.plandatetime + timedelta(hours=int(self.planduration.strftime("%H")),minutes=int(self.planduration.strftime("%M")))).strftime("%H:%M"))
        return ""

    def orderend(self):
        if(self.op_startdatetime):
            return str((self.op_startdatetime + timedelta(minutes=10)).strftime("%H:%M"))
        return ""



"""
    TODO: Slottaus
    TODO: Tehtäväkuvat
    TODO: ?
"""


