from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.helpfunction import get_duration, format_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in active_visits:
        entered_at = localtime(visit.entered_at)
        duration = get_duration(visit)
        visit_time = format_duration(duration)
        person = visit.passcard

        non_closed_visits.append(
            {
                "who_entered": person,
                "entered_at": entered_at,
                "duration": visit_time,
            },
        )
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
