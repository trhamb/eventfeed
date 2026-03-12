# Fetcher grabs events from sswcharity.org.uk via the Event Calendar URLS
# The response is simply returned from the function.


import requests
import calendar
import datetime as dt

# start = dt.date.today()
# # end = start + dt.timedelta(days=6)
# dotm = calendar.monthrange(start.year, start.month)[1]
# end = start + dt.timedelta(days=(dotm - start.day))


url = f"https://sswcharity.org.uk/wp-json/tribe/events/v1/events"


def fetch_events(q_start, q_end):
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"start_date": q_start, "end_date": q_end}

    r = requests.get(url, headers=headers, params=params)

    print("REQUEST DETAILS")
    print(f"Response status: {r.status_code}")
    print(f"Start: {q_start}, End: {q_end}")
    print(f"Requested URL: {r.url}")
    print(
        "------------------------------------------------------------------------------------------------------------------"
    )
    return r
