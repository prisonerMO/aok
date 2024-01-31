from django.contrib import admin
from events.models import OpRole, OpRoleBox, Event, Radio



class EventAdmin(admin.ModelAdmin):
    list_display = [
        'op_name', 'op_organizer', 'op_map', 'op_startdatetime', 'op_duration', 'op_slotopendatetime',
        'plandatetime', 'planduration', 'op_modpreset',
        'server_a3address', 'server_a3port', 'server_a3pwd',
        'server_tsaddress', 'server_tsport', 'server_tspwd',
        'op_rolebox', 'op_minplayers', 'op_maxplayers', 'op_spec_datetime', 'op_spec_weather', 'op_rules',
        'op_spec_friedlies', 'op_spec_enemies', 'op_spec_civilians', 'op_spec_roe', 'op_spec_assets',
        'op_spec_mission', 'op_spec_proceeding', 'op_spec_supports', 'op_spec_comms',
    ]
    
    def op_rolebox(self, obj):
        return ", ".join([c.shortname for c in obj.op_rolebox.all()])

admin.site.register(Event, EventAdmin)



class OpRoleAdmin(admin.ModelAdmin):
    list_display = [ 'rolename', ]

admin.site.register(OpRole, OpRoleAdmin)



class OpRoleBoxAdmin(admin.ModelAdmin):
    list_display = [ 'name', ]

admin.site.register(OpRoleBox, OpRoleBoxAdmin)



class RadioAdmin(admin.ModelAdmin):
    list_display = [ 'name', ]

admin.site.register(Radio, RadioAdmin)


