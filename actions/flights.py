from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests, json
import csv
import sys
import re


csv_file = csv.reader(open("/root/Desktop/SIH/actions/iata_code.csv","r+"), delimiter=",", quotechar='"')
lines = list(csv_file)

class SearchFlights(Action):
    def name(self) -> Text:
        return "action_search_flights"
    def run(self, dispatcher, tracker, domain):
        entity = tracker.latest_message['entities']
        entities = {}
        for c in entity:
            entities.__setitem__(c['entity'],c['value'])
        saddr = entities['saddr']
        if saddr == None :
            saddr = "My+Location"
        daddr = entities['daddr']
        date = entities['date']
        SlotSet('saddr',saddr)
        SlotSet('daddr',daddr)
        src = ""
        dst = ""
        for x in lines:
            if x[0] == saddr.capitalize():
                src = x[1]
            if x[0] == daddr.capitalize():
                dst = x[1]
        url = "https://www.google.com/flights?lite=0#flt="+src+"."+dst+"."+date+";c:INR;e:1;sd:1;t:f;tt:o"
        dispatcher.utter_message(url)
        return[]

