from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.helpfunction import get_duration, format_duration, is_visit_long
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in passcard_visits:
        entered_at = localtime(visit.entered_at)
        duration = get_duration(visit)
        visit_time = format_duration(duration)
        is_strange = is_visit_long(duration)
        this_passcard_visits.append(
            {
                "entered_at": entered_at,
                "duration": visit_time,
                "is_strange": is_strange,
            },
        )
    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
