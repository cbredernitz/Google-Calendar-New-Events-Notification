from __future__ import print_function
import quickstart as quick
import requests
import json
import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import unittest
import datetime

__author__ = 'Chris Bredernitz'

# cd to working directory inorder to activate env106final.
# Path for the virtual enviornment 'source env106final/bin/activate' which is located in the 106_final_project directory

use_live_data = True
cache_data = True

cred = quick.get_credentials()

credentials = cred
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)

# Below is the v3 google API for calendars

class Calendars_Event():
    def __init__(self, event):
        self.title = event['summary']
        self.organizer = event['organizer']['displayName']
        self.organizer_email = event['organizer']['email']
        try:
            self.description = event['description']
        except:
            self.description = None
        self.get_attendees_email(event)
        self.start_time = event['start']['dateTime']
        self.end_time = event['end']['dateTime']
    def get_attendees_email(self, event):
        try:
            attendees_lst = []
            for a in event['attendees']:
                attendees_lst.append(a['email'])
            self.attendees = attendees_lst
        except:
            self.attendees = None
        return attendees_lst

    def __str__(self):
        return("Your event titled '{}' is starting at {}.  More information about the event, if available, is '{}'.  This is event is scheduled to end on {}. The event is lead by {}, who can be reached at {}, with {} in attendance.\n").format(self.title, self.start_time, self.description, self.end_time, self.organizer, self.organizer_email, self.attendees)

F_Name = 'previous_cache.txt'

# This trys to open the 'previous_cache.txt file'. However, if there hasn't been any information cached yet it it will set the CACHE_DICTION veriable to an empty dictionary.
try:
    cache_file = open(F_Name, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

# This below gets the new data from the Google API and also set the time to not contain past events.

# If you want to set the code to show more than your next 15 events, change the 'maxResults' = to the desired amount.

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
eventsResult = service.events().list(
    calendarId='primary', timeMin=now, maxResults=15, singleEvents=True,
    orderBy='startTime').execute()

# This function prints the full calendar information of each event printing out the __str__() of the Calendars_Event() class.
def full_calendar(events):
    print("----Below is your full calendar----\n")
    for x in events:
        print(Calendars_Event(x))
        print("----------")

# The function below creates a list of instances from each separate event in your calendar.
def get_lst_instances(events):
    instance_lst = []
    for x in events:
        instance_lst.append(Calendars_Event(x))
    return instance_lst

# The function below creates a list of your live data event titles and appends them to a list. Return is sorted in alphabetical order.
def get_live(event):
    live_data_names = []
    for live in event:
        live_data_names.append(live.title)
    return sorted(live_data_names, key = lambda x: x.lower())

# The function below creates a list of your cache data event titles and appends them to a list. Return is sorted in alphabetical order.
def get_cache(event):
    cache_data_names = []
    for cache in event:
        cache_data_names.append(cache.title)
    return sorted(cache_data_names, key = lambda x: x.lower())

# This is the main function by passing live data and cache data into the above functions.  It then takes the sorted lists and checks to see whether the cache data is still in the live data and vise versa.
def compare_dictionaries(cache_data, live_data):
    if cache_data == {}:
        raise Exception
    else:
        cache_file = get_lst_instances(cache_data)
        live_data_file = get_lst_instances(live_data)
        live = get_live(live_data_file)
        cache = get_cache(cache_file)
        for l in live:
            if l not in cache:
                print(l + " is a new event")
                print("----------")

        for c in cache:
            if c not in live:
                print(c + " is no longer in your calendar")
                print("----------")

# The below checks to see if the user wants to solely fetch live data or to compare to old data and see changes.
if use_live_data == True:
    events = eventsResult.get('items', [])
    if cache_data == True:
        try:
            compare_dictionaries(CACHE_DICTION,events)
            c = json.dumps(events)
            cache_file = open(F_Name, 'w')
            cache_file.write(c)
            cache_file.close()
        except:
            c = json.dumps(events)
            cache_file = open(F_Name, 'w')
            cache_file.write(c)
            cache_file.close()
else:
    events = CACHE_DICTION

print(full_calendar(events))

class Tests(unittest.TestCase):
    def test_live_data(self):
        self.assertEqual(use_live_data, True, "Check to see if you are allowing new data being fetched")
    def test_Cache(self):
        self.assertEqual(type(CACHE_DICTION), type([]), "Check to see if CACHE_DICTION is a list")
    def test_get_cred(self):
        self.assertTrue(quick, "Check to see that quickstart.py is in your working folder")
    def test_events(self):
        self.assertEqual(type(events), type([]), "Check to see that events is a list")
    def test_json_file(self):
        self.assertEqual(quick.CLIENT_SECRET_FILE,'client_secret.json', "Checking to see that your client ID's recieved from Google is named 'client_secret.json'")
    def test_results(self):
        self.assertEqual(type(eventsResult), type({}), "Check to see that eventResults is a dictionary.  If error make sure internet is availible")

unittest.main(verbosity=2)
