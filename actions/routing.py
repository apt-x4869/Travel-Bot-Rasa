from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests,json
import os

class locate(Action):
    def name(self) -> Text:
        return "action_locate"
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
            dispatcher.utter_message("Please tell me the location you want to locate")
            return []
        if loc == None :
            place = city
        elif city == None:
            place = loc.replace(" ","%20")
        else:
            place = loc.replace(" ","%20") +"%20"+ city

        dispatcher.utter_message("https://www.google.com/maps?q=" + place)
        return[]



class route(Action):
    def name(self) -> Text:
        return "action_route"
    def run(self, dispatcher, tracker, domain):
        entity = tracker.latest_message['entities']
        entities = {}
        for c in entity:
            entities.__setitem__(c['entity'],c['value'])
        saddr = entities['saddr']
        if saddr == None :
            saddr = "My+Location"
        daddr = entities['daddr']    
        SlotSet('saddr',saddr)
        SlotSet('daddr',daddr)
        url = "https://www.google.com/maps?saddr="
        url2 = "&daddr="
        dispatcher.utter_message(url+ saddr + url2 +daddr)
        return []
        
