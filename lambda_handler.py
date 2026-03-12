from ast import parse
from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_event_json, skill_launch
import datetime as dt
import calendar as cal


# Get day/month info
start = dt.date.today()
week_day = start.weekday()
days_of_the_month = cal.monthrange(start.year, start.month)[1]
month_end = start + dt.timedelta(days=(days_of_the_month - start.day))
days_til_end = 6 - week_day
week_end = start + dt.timedelta(days=days_til_end)
tomorrow = start + dt.timedelta(days=1)


def handler(event, context):
    if event["request"]["type"] == "LaunchRequest":
        return skill_launch()
    else:
        if event["request"]["intent"]["name"] == "ThisWeekIntent":
            return generate_event_json(
                build_speech(parse_response(fetch_events(start, week_end))), "week"
            )
        elif event["request"]["intent"]["name"] == "ThisMonthIntent":
            return generate_event_json(
                build_speech(parse_response(fetch_events(start, month_end))), "month"
            )
        elif event["request"]["intent"]["name"] == "TomorrowIntent":
            return generate_event_json(
                build_speech(parse_response(fetch_events(tomorrow, tomorrow))),
                "tomorrow",
            )
