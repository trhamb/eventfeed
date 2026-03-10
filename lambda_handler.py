from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_json


def handler(event, context):
    return generate_json(build_speech(parse_response(fetch_events())))
