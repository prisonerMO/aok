from django.shortcuts import render
from django.views import View
from .models import New



class News(View):
    template = 'news/templates/news.html'

    def get(self, request):
        context = {
            'news': New.objects.all(),
        }
        return render(request, self.template, context)
