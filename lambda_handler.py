from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_event_json, skill_launch
import datetime as dt
import calendar as cal

testLaunch = {
    "version": "1.0",
    "session": {
        "new": True,
        "sessionId": "amzn1.echo-api.session.test123",
        "application": {"applicationId": "amzn1.ask.skill.test-skill-id"},
        "user": {"userId": "amzn1.ask.account.test-user-id"},
    },
    "context": {},
    "request": {
        "type": "LaunchRequest",
        "requestId": "amzn1.echo-api.request.test-launch",
        "timestamp": "2026-03-10T12:00:00Z",
        "locale": "en-GB",
    },
}

testIntent = {
    "version": "1.0",
    "session": {
        "new": False,
        "sessionId": "amzn1.echo-api.session.test123",
        "application": {"applicationId": "amzn1.ask.skill.test-skill-id"},
        "user": {"userId": "amzn1.ask.account.test-user-id"},
    },
    "context": {},
    "request": {
        "type": "IntentRequest",
        "requestId": "amzn1.echo-api.request.test-intent",
        "timestamp": "2026-03-10T12:00:01Z",
        "locale": "en-GB",
        "intent": {
            "name": "ThisMonthIntent",
            "confirmationStatus": "NONE",
            "slots": {},
        },
    },
}

# Get day/month info
start = dt.date.today()
week_day = start.weekday()
days_of_the_month = cal.monthrange(start.year, start.month)[1]
month_end = start + dt.timedelta(days=(days_of_the_month - start.day))
days_til_end = 6 - week_day
week_end = start + dt.timedelta(days=days_til_end)


def handler(event, context):
    if event["request"]["type"] == "LaunchRequest":
        skill_launch()
    else:
        if event["request"]["intent"]["name"] == "ThisWeekIntent":
            generate_event_json(
                build_speech(parse_response(fetch_events(start, week_end)))
            )
        elif event["request"]["intent"]["name"] == "ThisMonthIntent":
            # Generate JSON using start and end dates.
            generate_event_json(
                build_speech(parse_response(fetch_events(start, month_end)))
            )

    return generate_event_json(build_speech(parse_response(fetch_events())))
