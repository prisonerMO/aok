"""
Importing:
admin base from Django contrib module
models from communities
"""
from django.contrib import admin
from communities.models import Community, Member, Rank, VRank



class CommunityAdmin(admin.ModelAdmin):
    """
    Admin for Community model
    """
    list_display = ['shortname', 'name']

admin.site.register(Community, CommunityAdmin)



class MemberAdmin(admin.ModelAdmin):
    """
    Admin for Member model
    """
    list_display = ['nickname', 'rank', 'lastname', 'communities', 'vrank', 'active']

    def communities(self, obj):
        """
        Returns all communities as a string separated with comma
        """
        return ", ".join([c.shortname for c in obj.community.all()])

admin.site.register(Member, MemberAdmin)



class RankAdmin(admin.ModelAdmin):
    """
    Admin for Rank model
    """
    list_display = ['rankname', 'rankappr', 'rankvalue']

admin.site.register(Rank, RankAdmin)



class VRankAdmin(admin.ModelAdmin):
    """
    Admin for Virtual Rank model
    """
    list_display = ['rankname', 'rankappr', 'rankvalue']

admin.site.register(VRank, VRankAdmin)
