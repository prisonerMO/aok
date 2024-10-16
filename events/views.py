"""
Importing:
views base from django
render from Django shortcuts module to render views
timezone from Django utils module to calculate timezones
timedelta from datetime to calculate time differences
model for Event
"""
from datetime import timedelta
from django.views import View
from django.shortcuts import render
from django.utils import timezone
from .models import Event



class Events(View):
    """
    View for Events using html template.
    Return rendered view with all event objects.
    """
    template = 'events/templates/events.html'

    def get(self, request):
        """
        Return rendered view with all event objects
        """
        context = {
            'events': Event.objects.all(),
        }
        return render(request, self.template, context)



class Slots(View):
    """
    View for Event Slots using html template.
    Return rendered view with context:
    id, event, op_date, op_start, op_end, planstart, planend,
    orderstart, orderend, slots_active, roleboxes, slots.
    """
    template = 'events/templates/slots.html'

    def get(self, request):
        """
        Return rendered view with context:
        event, op_date, op_start, op_end, planstart, planend,
        orderstart, orderend, slots_active, roleboxes, slots
        """
        event = Event.objects.filter(pk=id).get()
        now = timezone.now()
        opend = event.op_slotopendatetime + timedelta(
                        hours=int(event.op_duration.strftime("%H")),
                        minutes=int(event.op_duration.strftime("%M"))
                        )
        slots_active = " SLOTTAUS KIINNI "
        if opend < now > event.op_slotopendatetime:
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
    """
    Return rendered front page for events.
    """
    return render(request, 'events/templates/events.html')
