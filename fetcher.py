# Fetcher grabs events from sswcharity.org.uk via the Event Calendar URLS
# The response is simply returned from the function.


import requests
import calendar
import datetime as dt

start = dt.date.today()
# end = start + dt.timedelta(days=6)
dotm = calendar.monthrange(start.year, start.month)[1]
end = start + dt.timedelta(days=(dotm - start.day))


url = f"https://sswcharity.org.uk/wp-json/tribe/events/v1/events"

params = {"start_date": start, "end_date": end}


def fetch_events():
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers, params=params)

    print("REQUEST DETAILS")
    print(f"Response status: {r.status_code}")
    print(f"Start: {start}, End: {end}")
    print(f"Requested URL: {r.url}")
    print(
        "------------------------------------------------------------------------------------------------------------------"
    )
    return r
