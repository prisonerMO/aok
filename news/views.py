"""
Importing:
views base from django
render from Django shortcuts module to render views
model for New
"""
from django.views import View
from django.shortcuts import render
from .models import New



class News(View):
    """
    View for News using html template.
    Return rendered view with all new objects.
    """
    template = 'news/templates/news.html'

    def get(self, request):
        """
        Return rendered view with all new objects
        """
        context = {
            'news': New.objects.all(),
        }
        return render(request, self.template, context)
