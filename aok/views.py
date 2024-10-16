"""
Importing:
views base from django
render from Django shortcuts module to render views
models from communities
"""
from django.views import View
from django.shortcuts import render
from communities.models import Community, Member



class Main(View):
    """
    The main page class
    """
    template = 'aok/templates/main.html'

    def get(self, request):
        """
        Return rendered view with defined template
        """
        context = {
        }
        return render(request, self.template, context)



class Members(View):
    """
    Members page class
    """
    template = 'aok/templates/members.html'

    def get(self, request):
        """
        Return rendered view with defined template and contexts:
        communities: all objects
        members: all objects
        """
        context = {
            'communities': Community.objects.all(),
            'members': Member.objects.all(),
        }
        return render(request, self.template, context)



def frontpage(request):
    """
    Return rendered front page for main page.
    """
    return render(request, 'aok/templates/main.html')
