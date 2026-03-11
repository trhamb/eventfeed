from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_event_json, skill_launch

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


def handler(event, context):
    # if event["request"]["type"] == "LaunchRequest":
    #     skill_launch()
    # else:
    #     if event["request"]["intent"]["name"] == "ThisWeekIntent":
    #         print("This week")
    #     elif event["request"]["intent"]["name"] == "ThisMonthIntent":
    #         print("This Month")

    return generate_event_json(build_speech(parse_response(fetch_events())))


print(handler({}, None))
