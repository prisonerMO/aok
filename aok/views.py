from django.shortcuts import render
from django.views import View
from communities.models import Community, Member



class Main(View):
    template = 'aok/templates/main.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template, context)



class Members(View):
    template = 'aok/templates/members.html'

    def get(self, request):
        context = {
            'communities': Community.objects.all(),
            'members': Member.objects.all(),
        }
        return render(request, self.template, context)



def frontpage(request):
    return render(request, 'aok/templates/main.html')