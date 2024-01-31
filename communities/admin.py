from django.contrib import admin
from communities.models import Community, Member, Rank, VRank



class CommunityAdmin(admin.ModelAdmin):
    list_display = ['shortname', 'name']

admin.site.register(Community, CommunityAdmin)



class MemberAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'rank', 'lastname', 'communities', 'vrank', 'active']
    
    def communities(self, obj):
        return ", ".join([c.shortname for c in obj.community.all()])

admin.site.register(Member, MemberAdmin)



class RankAdmin(admin.ModelAdmin):
    list_display = ['rankname', 'rankappr', 'rankvalue']

admin.site.register(Rank, RankAdmin)



class VRankAdmin(admin.ModelAdmin):
    list_display = ['rankname', 'rankappr', 'rankvalue']

admin.site.register(VRank, VRankAdmin)



