# Speech takes parsed data and builds out lines of speech
# to be converted to SSML and submited to Echo Devices.

from datetime import datetime


def date_suffix(d):
    if d in (11, 12, 13):
        return "th"
    elif d % 10 == 1:
        return "st"
    elif d % 10 == 2:
        return "nd"
    elif d % 10 == 3:
        return "rd"
    else:
        return "th"


def build_speech(data):
    # List of speech lines to be joined.
    speech_parts = []

    # If the list is empty
    if len(data) == 0:
        return ["<speak>There are no events listed</speak>"]

    # Loop through events and get date and time parts
    for i in range(0, len(data)):
        start_date_text = datetime.strptime(data[i]["start"], "%Y-%m-%d %H:%M:%S")
        end_date_text = datetime.strptime(data[i]["end"], "%Y-%m-%d %H:%M:%S")

        day = start_date_text.strftime("%A")
        s_date = start_date_text.strftime("%d")
        suffix = date_suffix(int(s_date))
        suffixed = f"{s_date}{suffix}"
        month = start_date_text.strftime("%B")
        s_time = start_date_text.strftime("%I:%M %p")
        e_time = end_date_text.strftime("%I:%M %p")

        # Build each events date and time speech line
        date_string = f"{day} the {suffixed} of {month}. {s_time} to {e_time}"

        # Append the event and timings to the speech_parts list
        speech_parts.append(f"{data[i]["name"]}, {date_string}")
    return speech_parts


def skill_launch():
    speech = "<speak>Welcome to the Sight Support Alexa Hub. <break time='250ms'>For this week's events, say: this week. <break time='250ms'>For this month's events, say: this month</speak>"

    json_output = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": speech,
            },
            "shouldEndSession": False,
        },
    }
    return json_output


def generate_event_ssml(list):
    open_tag = "<speak>"
    intro = "Welcome to the Sight Support Hub. Here are this week's upcoming events:"
    close_tag = "</speak>"
    separator = '<break time="1000ms"/>'

    body = separator.join(list)

    return open_tag + intro + body + close_tag


def generate_event_json(speech_list):
    speech = generate_event_ssml(speech_list)

    json_output = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": speech,
            },
            "shouldEndSession": True,
        },
    }

    return json_output
