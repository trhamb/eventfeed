# Speech takes parsed data and builds out lines of speech
# to be converted to SSML and submited to Echo Devices.

from datetime import datetime

test_data = [
    {
        "name": "Coffee Morning",
        "start": "2026-03-09 10:00:00",
        "end": "2026-03-09 12:00:00",
    },
    {
        "name": "Chess Club",
        "start": "2026-03-09 11:00:00",
        "end": "2026-03-09 12:30:00",
    },
    {
        "name": "Monday Bus Trip: Squires",
        "start": "2026-03-09 11:00:00",
        "end": "2026-03-09 13:00:00",
    },
    {
        "name": "Showdown for Beginners",
        "start": "2026-03-09 13:00:00",
        "end": "2026-03-09 15:00:00",
    },
]


def date_suffix(d):
    if d == 11 | 12 | 13:
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

    # Loop through events and get date and time parts
    for i in range(0, len(data)):
        start_date_text = datetime.strptime(data[i]["start"], "%Y-%m-%d %H:%M:%S")
        end_date_text = datetime.strptime(data[i]["end"], "%Y-%m-%d %H:%M:%S")

        day = start_date_text.strftime("%A")
        s_date = start_date_text.strftime("%d")
        suffix = date_suffix("%d")
        suffixed = f"{s_date}{suffix}"
        month = start_date_text.strftime("%B")
        s_time = start_date_text.strftime("%I:%M %p")
        e_time = end_date_text.strftime("%I:%M %p")

        # Build each events date and time speech line
        date_string = f"{day} the {suffixed} of {month}. {s_time} to {e_time}"

        # Append the event and timings to the speech_parts list
        speech_parts.append(f"{data[i]["name"]}, {date_string}")
    return speech_parts


print(build_speech(test_data))
