# Parser takes fetched data and strips out the required
# information to be used when producing speech lines.


def parse_response(response):
    event_list = []

    response_json = response.json()

    for r in range(0, len(response_json["events"])):
        event = {
            "name": response_json["events"][r]["title"],
            "start": response_json["events"][r]["start_date"],
            "end": response_json["events"][r]["end_date"],
        }
        event_list.append(event)

    return event_list
