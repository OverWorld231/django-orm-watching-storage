from django.utils.timezone import localtime
from datetime import datetime, timezone


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if not visit.leaved_at:
        delta_time = localtime(datetime.now(timezone.utc)) - entered_at
    else:
        delta_time = localtime(visit.leaved_at) - entered_at
    return delta_time


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes}:{seconds}"


def is_vising_long(duration, minutes=60):
    seconds = minutes * minutes
    long_visit = duration.total_seconds() > seconds
    return long_visit

