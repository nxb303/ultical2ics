import requests
from ics import Calendar, Event
from ultical_event import UlticalEvent
import time

API_EVENTS = 'https://api.ultical.com/api/v2/event'
API_EVENT_SINGLE = 'https://api.ultical.com/api/v1/event/'
IMAGE_URL_PREFIX = 'https://ultical.s3.eu-west-2.amazonaws.com/events/'

if __name__ == '__main__':
    headers = {'Accept': 'application/json'}
    r = requests.get('https://api.ultical.com/api/v2/event', headers=headers)
    event_list = r.json().get('data')

    c = Calendar()
    ultical_events = []
    for event in event_list:
        e = Event()
        r2 = requests.get('https://api.ultical.com/api/v1/event/' + str(event.get('Id')))
        event_details = r2.json()
        ultical_event = UlticalEvent(event_details)
        ultical_events.append(ultical_event)

    ics_events = []
    for ultical_event in ultical_events:
        ics_events.append(ultical_event.to_ics_event())
    for ics_event in ics_events:
        c.events.add(ics_event)
    today = time.strftime("%Y-%m-%d")
    with open(f'events_{today}.ics', 'w') as events_file:
        events_file.writelines(c.serialize_iter())
