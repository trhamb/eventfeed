from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_event_json


def handler(event, context):
    return generate_event_json(build_speech(parse_response(fetch_events())))


print(handler({}, None))
