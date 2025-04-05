from django.utils.timezone import localtime
from datetime import timezone


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if not visit.leaved_at:
        delta_time = localtime(timezone.now()) - entered_at
    else:
        delta_time = localtime(visit.leaved_at) - entered_at
    return delta_time


def format_duration(duration):
    seconds_in_hours = 3600
    seconds_in_minutes = 60
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // seconds_in_hours
    minutes = (total_seconds % seconds_in_hours) // seconds_in_minutes
    secondsseconds = total_seconds % seconds_in_minutes
    return f"{hours}:{minutes}:{secondsseconds}"


def is_visit_long(duration, minutes=60):
    total_seconds = minutes * minutes
    long_visit = duration.total_seconds() > total_seconds
    return long_visit

