url = "https://www.google.com/travel/hotels/"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests,json
import os

class Hotel(Action):
    def name(self) -> Text:
        return "action_search_hotels"
    def run(self, dispatcher, tracker, domain):
        entity = tracker.latest_message['entities']
        entities = {}
        for c in entity:
            entities.__setitem__(c['entity'],c['value'])
        try:
            loc = entities['locality']
        except:
            loc = None
        try:
            city = entities['city']
        except:
            city = None    
        SlotSet('locality',loc)
        SlotSet('city',city)
        if loc == None and city == None :
            dispatcher.utter_message("Please tell me the location you want to search")
            return []
        if loc == None :
            place = city
        elif city == None:
            place = loc
        else:
            place = loc +"%20"+ city
        hotel_url = url + place
        dispatcher.utter_message(hotel_url)
        return []
