from django.shortcuts import render
from django.views import View
from .models import Event
from django.utils import timezone
from datetime import timedelta


class Events(View):
    template = 'events/templates/events.html'

    def get(self, request):
        context = {
            'events': Event.objects.all(),
        }
        return render(request, self.template, context)



class Slots(View):
    template = 'events/templates/slots.html'

    def get(self, request, id):
        event = Event.objects.filter(pk=id).get()
        now = timezone.now()
        opend = event.op_slotopendatetime + timedelta(
                        hours=int(event.op_duration.strftime("%H")),
                        minutes=int(event.op_duration.strftime("%M"))
                        )
        slots_active = " SLOTTAUS KIINNI "
        if(now > event.op_slotopendatetime and now < opend):
            slots_active = " SLOTTAUS AUKI "

        roleboxes = event.op_rolebox.all()
        rolebox = roleboxes.filter(pk=id).get()
        slots = rolebox.oprole.all()

        context = {
            'id': id,
            'event': event,
            'op_date': event.op_startdate,
            'op_start': event.op_starttime,
            'op_end': event.op_endtime,
            'planstart': event.planstarttime,
            'planend': event.planendtime,
            'orderstart': event.op_starttime,
            'orderend': event.orderend,
            'slots_active': slots_active,
            'roleboxes': roleboxes,
            'slots': slots,
        }
        return render(request, self.template, context)



def frontpage(request):
    return render(request, 'events/templates/events.html')
