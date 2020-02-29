# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import wikipedia
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")
        return []



import datetime
import time
class ActionTime(Action):
    def name(self) -> Text:
        return "action_time"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        txt = str(time.asctime( time.localtime(time.time()) ))
        dispatcher.utter_message(txt)
        return []


from rasa_sdk.events import SlotSet
import requests, json
class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('city')
        if (loc == None):
            dispatcher.utter_message("Please tell me the location of which you need weather report")
            return []
        api_key = "7fa2f3ab99eafedc592b7690bba5d54d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = str(loc).capitalize()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the current pressure is {} hpa.""".format(weather_description, city_name, current_temperature, current_humidiy, current_pressure)
            dispatcher.utter_message(response)
        else:
            dispatcher.utter_message("City Not found")
        return [SlotSet('city',loc)]

import csv
import sys
import re
class ActionPincode(Action):
    def name(self) -> Text:
        return "action_pincode"
    def run(self,dispatcher,tracker,domain):
        pincode = tracker.get_slot('pincode')
        if pincode== None:
            dispatcher.utter_message("Please enter the pincode")
        csv_file = csv.reader(open('/root/Desktop/SIH/actions/pincodes.csv', "r"), delimiter=",")
        for row in csv_file:
            if pincode == str(row[1]):
                dispatcher.utter_message(str(row[0])+","+str(row[2])+","+str(row[3])+" "+str(row[1]))
                flag = 1
        if(flag==0):
            dispatcher.utter_message("Invalid Pincode / Not Found in Database")
        return [SlotSet('pincode',pincode)]

class ActionCityPincode(Action):
    def name(self) -> Text:
        return "action_city_pincode"
    def run(self,dispatcher,tracker,domain):
        locality = tracker.get_slot('locality')
        if locality== None:
            dispatcher.utter_message("Please Enter the locality, city to know pincode")
            return []
        csv_file = csv.reader(open('/root/Desktop/SIH/actions/pincodes.csv', "r"), delimiter=",")
        locality = re.findall(r"[\w']+",locality)[0]
        for row in csv_file:
            if locality == str(row[0]):
                dispatcher.utter_message(str(row[0])+","+str(row[2])+","+str(row[1]))
        return [SlotSet('locality',locality)]


import requests
from bs4 import BeautifulSoup
url="https://www.yatra.com/india-tourism/city-travel-guide"
headers = {'User-agent': 'Mozilla/5.0'}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
all_places=[]
places = soup.findAll('figure',{"class":"prel full"})
for i in range(len(places)):
    all_places.append(places[i].text.split('\n')[3].replace(" ","-"))
    
class ActionPlaceInfo(Action):
    def name(self) -> Text:
        return "action_place_info"
    def run(self,dispatcher,tracker,domain):
        loc = tracker.get_slot('city')
        if (loc == None):
            dispatcher.utter_message("Please tell me the City you want to know about")
            return []
        loc = loc.lower().replace(" ","-")
        if loc not in all_places :
            dispatcher.utter_message("Please re-enter city name correctly ")
            return []
        url2 = "https://www.yatra.com/india-tourism/"+loc+"-travel-guide"
        page = requests.get(url2,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_place=soup.find('div',{'class':'p25-0 fs13 content conDiv lh25 fl'})
        place_info = "".join(text_place.find('p').text.split('var _cf')[0].split('\n')[4].strip().split("\\r\\n\\r\\n"))
        dispatcher.utter_message(place_info)
        return[]

class ActionPlaceReachInfo(Action):
    def name(self) -> Text:
        return "action_place_reach_info"
    def run(self,dispatcher,tracker,domain):
        loc = tracker.get_slot('city')
        if (loc == None):
            dispatcher.utter_message("Please tell me the City you want to travel")
            return []
        loc = loc.lower().replace(" ","-")
        if loc not in all_places :
            dispatcher.utter_message("Please re-enter city name correctly ")
            return []
        url2 = "https://www.yatra.com/india-tourism/"+loc+"/how-to-reach"
        page = requests.get(url2,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        reach_place=soup.find('div',{'class':'my-wrap p25-0 fs13 content lh25'})
        reach_place="".join("".join(reach_place.text.split("\t")).split("\n"))
        dispatcher.utter_message(reach_place)
        return[]


class ActionBesTimeInfo(Action):
    def name(self) -> Text:
        return "action_best_time_info"
    def run(self,dispatcher,tracker,domain):
        loc = tracker.get_slot('city')
        if (loc == None):
            dispatcher.utter_message("Please tell me the City you want to know about to get the best visiting time")
            return []
        loc = loc.lower().replace(" ","-")
        if loc not in all_places :
            dispatcher.utter_message("Please re-enter city name correctly ")
            return []
        url2 = "https://www.yatra.com/india-tourism/"+loc+"/best-time-to-visit"
        page = requests.get(url2,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        reach_place=soup.find('div',{'class':'my-wrap p25-0 fs13 content lh25 fl conDiv'})
        best_time_info="".join("".join(reach_place.text.split("\t")).split("\n")).split("var _cf ")[0].strip()
        dispatcher.utter_message(best_time_info)
        return[]


import requests,json
import os

base_url = "https://maps.googleapis.com/maps/api/place/"
base_url_photos = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
api_key = os.environ['API_KEY']
def search(place):
    url1 = "findplacefromtext/json?input="
    url2 = "&inputtype=textquery&fields=photos,formatted_address,name,geometry,place_id&key="
    place = place.replace(' ',"%20")
    url = base_url + url1 + place + url2 + str(api_key)
    response = requests.get(url)
    return response.json()

class ActionSearchPlace(Action):
    def name(self) -> Text:
        return "action_search_place"
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
        x = search(place)
        y = x['candidates']
        dispatcher.utter_message("Searching..., Found :")
        for c in y:
            photo_ref = c['photos'][0]['photo_reference']
            image = base_url_photos + photo_ref + "&key=" + str(api_key)
            img = requests.get(image)
            dispatcher.utter_message(template="utter_image", image=img.url)
            dispatcher.utter_message(c['formatted_address'])
        txt = wikipedia.summary(place)
        dispatcher.utter_message(txt)
        return []
        
class ActionSearchNearby(Action):
    def name(self) -> Text:
        return "action_search_nearby"
    def run(self, dispatcher, tracker, domain):
        entity = tracker.latest_message['entities']
        entities = {}
        for c in entity:
            entities.__setitem__(c['entity'],c['value'])
        keyword = entities['keyword']
        url = "https://maps.googleapis.com/maps/api/place/textsearch/xml?query="+keyword+"&key="+api_key
        response = requests.get(url)
        x = response.json()
        y = x['results']
        dispatcher.utter_message("Searching..., Found :")
        for c in y:
            photo_ref = c['photos'][0]['photo_reference']
            image = base_url_photos + photo_ref + "&key=" + str(api_key)
            img = requests.get(image)
            dispatcher.utter_message(template="utter_image", image=img.url)
            dispatcher.utter_message(c['name'])       
        
        return[]

