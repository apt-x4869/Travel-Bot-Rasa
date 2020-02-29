## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* weather
    - action_weather
    - slot{"city": null}

## interactive_story_1
* weather{"city": "Kolkata"}
    - slot{"city": "Kolkata"}
    - action_weather
    - slot{"city": "Kolkata"}
* weather
    - action_weather
    - slot{"city": "Kolkata"}
* weather{"city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_weather
    - slot{"city": "Ranchi"}

## interactive_story_1
* weather{"city": "Lucknow"}
    - slot{"city": "Lucknow"}
    - action_weather
    - slot{"city": "Lucknow"}
* weather{"city": "Bokaro"}
    - slot{"city": "Bokaro"}
    - action_weather
    - slot{"city": "Bokaro"}
* stop

## interactive_story_1
* greet
    - utter_greet
* weather
    - action_weather
    - slot{"city": null}
* weather{"city": "jamshedpur"}
    - slot{"city": "jamshedpur"}
    - action_weather
    - slot{"city": "jamshedpur"}
* current_time
    - action_time
* mood_great

## interactive_story_1
* weather{"city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_weather
    - slot{"city": "Ranchi"}

## New Story

* greet
    - utter_greet
* deny
    - utter_happy
* weather{"city":"Mumbai","unit":"celcius"}
    - slot{"city":"Mumbai"}
    - slot{"unit":"celcius"}
    - action_weather
    - slot{"city":"Mumbai"}

## New Story

* greet
    - utter_greet
* weather
    - action_weather
    - slot{"city":null}
* weather{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_weather
    - slot{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"city":"jamshedpur"}

## New Story

* weather

## interactive_story_1
* weather
    - action_weather
    - slot{"city": null}
* weather{"city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_weather
    - slot{"city": "Ranchi"}
* affirm{"city": "Jamshedpur"}
    - slot{"city": "Jamshedpur"}
    - action_weather
    - slot{"city": "Jamshedpur"}

## New Story

* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
* greet
    - utter_greet
* greet

## New Story

* greet
    - utter_greet
* greet
* greet
    - utter_greet
* greet
    - utter_greet
* greet
* greet
    - utter_greet
* current_time
    - action_time

## New Story

* weather
* weather{"weather":"forecast","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_weather
    - slot{"city":"Ranchi"}
* weather

## New Story

* weather{"weather":"climate"}

## New Story

* weather{"weather":"climate"}
    - action_weather
    - slot{"city":null}
* weather{"weather":"climate","city":"panji"}
    - slot{"city":"panji"}
    - action_weather
    - slot{"city":"panji"}
* weather{"weather":"climate"}
    - action_weather
    - slot{"city":"panaji"}

## New Story

* weather{"weather":"climate"}
    - action_weather
    - slot{"city":null}

## New Story

* weather{"weather":"forecast","city":"Panaji"}
    - slot{"city":"Panaji"}
    - action_weather
    - slot{"city":"Panaji"}
    - slot{"city":"Panaji"}
    - slot{"city":"mumbai"}
* weather{"weather":"forecast","city":"delhi"}
    - slot{"city":"delhi"}
    - action_weather
    - slot{"city":"delhi"}
* weather{"weather":"forecast","city":"Bhopal"}
    - slot{"city":"Bhopal"}
    - action_weather
    - slot{"city":"Bhopal"}
* weather{"weather":"forecast","city":"Gorakhpur"}
    - slot{"city":"Gorakhpur"}
    - action_weather
    - slot{"city":"Gorakhpur"}
* weather{"weather":"forecast","city":"Shimla"}
    - slot{"city":"Shimla"}
    - action_weather
    - slot{"city":"Shimla"}

## New Story

* weather{"weather":"forecast"}
    - action_weather
    - slot{"city":null}
* weather{"weather":"forecast"}
    - action_weather
    - slot{"city":null}
* weather
    - action_weather
    - slot{"city":null}

## New Story

* weather{"city":"mexico city"}
    - slot{"city":"mexico city"}
    - action_weather
    - slot{"city":"mexico city"}
* weather{"sys_time":"tommorow"}
    - action_weather
    - slot{"city":"mexico city"}
* weather{"city":"london"}
    - slot{"city":"london"}
    - action_weather
    - slot{"city":"london"}
* weather{"city":"Varanasi"}
    - slot{"city":"Varanasi"}
    - action_weather
    - slot{"city":"Varanasi"}
* weather{"city":"Chennai"}
    - slot{"city":"Chennai"}
    - action_weather
    - slot{"city":"Chennai"}
* weather{"city":"Berlin"}
    - slot{"city":"Berlin"}
    - action_weather
    - slot{"city":"Berlin"}

## New Story

* current_time
    - action_time
* current_time
    - action_time
* current_time
    - action_time

## New Story

* greet
    - utter_greet
* greet
    - action_pincode

## New Story

* greet
    - action_pincode
* greet
    - action_pincode

## New Story

* pincode{"pincode":"400703"}
    - slot{"pincode":"400703"}
    - action_pincode
* pincode
    - action_pincode
* pincode
    - action_pincode
* pincode
    - action_pincode

## New Story

* pincode{"pincode":"211004"}
    - slot{"pincode":"211004"}
    - action_pincode
* pincode{"pincode":"211004"}
    - slot{"pincode":"211004"}
    - action_pincode
    - slot{"pincode":"211004"}
* pincode{"pincode":"400705"}
    - slot{"pincode":"400705"}
    - action_pincode
    - slot{"pincode":"400705"}
* pincode{"pincode":"400703"}
    - slot{"pincode":"400703"}
    - action_pincode
    - slot{"pincode":"400703"}
* weather{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_weather
    - slot{"city":"Ranchi"}

## New Story

* pincode{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_city_pincode
    - slot{"city":"Ranchi"}

## New Story

* pincode
    - action_city_pincode

## New Story

* pincode{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_city_pincode
    - slot{"city":"Ranchi"}
* pincode{"city":"Namkum"}
    - slot{"city":"Namkum"}
    - action_city_pincode
    - slot{"city":"Namkum"}
* pincode{"city":"Adityapur"}
    - slot{"city":"Adityapur"}
    - action_city_pincode
    - slot{"city":"Adityapur"}
* pincode{"city":"Adityapur, Jamshedpur"}
    - slot{"city":"Adityapur, Jamshedpur"}
    - action_city_pincode
    - slot{"city":"Adityapur"}
* pincode{"city":"Gobindpur"}
    - slot{"city":"Gobindpur"}
    - action_city_pincode
    - slot{"city":"Gobindpur"}

## New Story

* pincode{"city":"vashi"}
    - slot{"city":"vashi"}
    - action_city_pincode
    - slot{"city":"vashi"}

## New Story

* pincode
    - action_city_pincode

## New Story

* pincode

## New Story

* pincode
    - action_city_pincode

## New Story

* pincode{"locality":"Chembur"}
    - slot{"locality":"Chembur"}
    - action_city_pincode
* pincode{"locality":"Vashi"}
    - slot{"locality":"Vashi"}
    - action_city_pincode
* pincode{"locality":"Adityapur"}
    - slot{"locality":"Adityapur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"locality":"Namkum","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Namkum"}
    - action_city_pincode
    - slot{"locality":"Namkum"}
* pincode{"locality":"Adityapur","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Adityapur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}

## New Story

* greet
    - utter_greet
* pincode{"locality":"Namkum","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Namkum"}
    - action_city_pincode
    - slot{"locality":"Namkum"}
* weather{"city":"London"}
    - slot{"city":"London"}
    - action_weather
    - slot{"city":"London"}
* weather{"city":"Melborne"}
    - slot{"city":"Melborne"}
    - action_weather
    - slot{"city":"Melborne"}
* weather{"city":"Melbourne"}
    - slot{"city":"Melbourne"}
    - action_weather
    - slot{"city":"Melbourne"}
* pincode{"city":"Vashi"}
    - slot{"city":"Vashi"}
    - action_city_pincode
    - slot{"locality":"Namkum"}

## New Story

* greet
    - utter_greet
* affirm
    - utter_happy
* place_info{"city":"jamshedpur"}
    - slot{"city":"jamshedpur"}
    - action_place_info
* place_info
    - action_place_info

## New Story

* place_info{"city":"Kolkata"}
    - slot{"city":"Kolkata"}
    - action_place_info
* place_info{"city":"New Delhi"}
    - slot{"city":"New Delhi"}
    - action_place_info

## New Story

* place_info{"city":"Bodh gaya"}
    - slot{"city":"Bodh gaya"}
    - action_place_info
    - slot{"city":"Bodh gaya"}
    - slot{"city":"Navi Mumbai"}

## New Story

* place_reach
    - action_place_reach_info
* place_reach{"city":"jamshedpur"}
    - slot{"city":"jamshedpur"}
    - action_place_reach_info
    - action_place_reach_info
* place_reach{"city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_place_reach_info
* place_reach{"city":"Mumbai"}
    - slot{"city":"Mumbai"}
    - action_place_reach_info

## New Story

* best_time_info{"city":"Mumbai"}
    - slot{"city":"Mumbai"}
    - action_best_time_info

## New Story

* best_time_info{"city":"Mumbai"}
    - slot{"city":"Mumbai"}
    - action_best_time_info
* best_time_info{"city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - action_best_time_info

## New Story

* best_time_info{"city":"Lucknow"}
    - slot{"city":"Lucknow"}
    - action_best_time_info
* best_time_info{"city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_best_time_info

## New Story

* best_time_info
    - action_best_time_info

## Story from conversation with ccdcbd96-baed-48e7-a1e2-e4f018644912 on January 3rd 2020

* greet
    - utter_greet
* affirm
    - utter_happy
* best_time_info
    - action_best_time_info
* best_time_info
    - action_best_time_info

## New Story

* best_time_info
    - action_best_time_info

## Story from conversation with ccdcbd96-baed-48e7-a1e2-e4f018644912 on January 3rd 2020

* greet
    - utter_greet
* affirm
    - utter_happy
* best_time_info{"city":"Goa"}
    - slot{"city":"Goa"}
    - action_best_time_info

## New Story

* search_place{"locality":"vashi","city":"navi mumbai"}
    - slot{"city":"navi mumbai"}
    - slot{"locality":"vashi"}
    - action_search_place

## New Story

* search_place{"city":"Mumbai"}
    - slot{"city":"Mumbai"}

## New Story

* search_place{"locality":"Vashi","city":"Navi Mumbai"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Vashi"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Vashi"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Sanpada"}

## New Story

* search_place{"searchplace":"search","locality":"Vashi","city":"Navi Mumbai"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Vashi"}

## New Story

* search_place{"searchplace":"search","locality":"Sanpada","city":"Mumbai"}
    - slot{"city":"Mumbai"}
    - slot{"locality":"Sanpada"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Vashi","city":"Navi Mumbai"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Vashi"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Vashi","city":"Navi Mumbai"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Vashi"}
    - action_search_place
* search_place{"searchplace":"search","city":"Srinagar"}
    - slot{"city":"Srinagar"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Sanpada","city":"Navi Mumbai"}
    - slot{"city":"Navi Mumbai"}
    - slot{"locality":"Sanpada"}
    - action_search_place

## New Story

* greet
    - utter_greet
* affirm
    - utter_happy
* search_place{"searchplace":"search","city":"Chennai"}
    - slot{"city":"Chennai"}
    - action_search_place
* search_place{"searchplace":"search","city":"Chennai"}
    - slot{"city":"Chennai"}
    - action_search_place
* search_place{"searchplace":"search","city":"Ahemdabad"}
    - slot{"city":"Ahemdabad"}
    - action_search_place
* search_place{"searchplace":"search","city":"Panaji"}
    - slot{"city":"Panaji"}
    - action_search_place
* search_place{"searchplace":"search","city":"Nagpur"}
    - slot{"city":"Nagpur"}
    - action_search_place
* search_place{"searchplace":"search","city":"Chandigarh"}
    - slot{"city":"Chandigarh"}
    - action_search_place
* search_place{"searchplace":"search","city":"Chandigarh"}
    - slot{"city":"Chandigarh"}
    - action_search_place

## New Story

* search_place{"searchplace":"search","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_search_place
* search_place{"searchplace":"search","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_search_place

## New Story

* search_place{"searchplace":"search","city":"Ahemdabad"}
    - slot{"city":"Ahemdabad"}
    - action_search_place

## New Story

* greet
    - utter_greet
* affirm
    - utter_happy
* weather{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_weather
    - slot{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"city":"adityapur"}
    - slot{"locality":"adityapur"}
    - action_city_pincode
    - slot{"locality":"adityapur"}
* place_reach{"reachinfo":"how to reach","city":"Katra"}
    - slot{"city":"Katra"}
    - action_place_reach_info
* best_time_info{"besttimeinfo":"best time","city":"Katra"}
    - slot{"city":"Katra"}
    - action_best_time_info
* pincode{"locality":"Adityapur","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Adityapur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"city":"vanarasi"}
    - slot{"city":"vanarasi"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"city":"Kanpur"}
    - slot{"city":"Kanpur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"city":"Kanpur"}
    - slot{"city":"Kanpur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"city":"jamshedpur"}
    - slot{"city":"jamshedpur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}

## New Story

* search_place{"searchplace":"search","locality":"Kadma","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Kadma"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Kadma","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Kadma"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Anand"}
    - slot{"locality":"Anand"}
    - action_search_place
* search_place{"searchplace":"search","city":"AnandBhawan"}
    - slot{"city":"AnandBhawan"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Anand","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - slot{"locality":"Anand"}
    - action_search_place

## New Story

* greet
    - utter_greet
* affirm
    - utter_happy
* search_place{"searchplace":"search","locality":"Saltlake","city":"Kolkata"}
    - slot{"city":"Kolkata"}
    - slot{"locality":"Saltlake"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Baghbazar","city":"Kolkata"}
    - slot{"city":"Kolkata"}
    - slot{"locality":"Baghbazar"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Mirganj","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - slot{"locality":"Mirganj"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Taj","city":"Mahal"}
    - slot{"city":"Mahal"}
    - slot{"locality":"Taj"}
    - action_search_place
* search_place{"searchplace":"search","city":"banglore"}
    - slot{"city":"banglore"}
    - action_search_place

## interactive_story_1
* search_place{"searchplace": "search", "locality": "Leaning Tower of Pisa"}
    - slot{"locality": "Leaning Tower of Pisa"}
    - action_search_place

## New Story

* greet
    - utter_greet
* affirm
    - utter_happy
* search_place{"searchplace":"search","locality":"Telco","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Telco"}
    - action_search_place

## New Story

* weather{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - action_weather
    - slot{"city":"Delhi"}
* search_place{"searchplace":"search","city":"Banglore"}
    - slot{"city":"Banglore"}
    - action_search_place
* place_info{"city":"banglore"}
    - slot{"city":"banglore"}
    - action_place_info
* place_info
    - action_place_info
* place_info{"city":"Bengaluru"}
    - slot{"city":"Bengaluru"}
    - action_place_info
* place_reach{"reachinfo":"reach","city":"Bengaluru"}
    - slot{"city":"Bengaluru"}
    - action_place_reach_info
* best_time_info{"besttimeinfo":"best time to visit","city":"Bengaluru"}
    - slot{"city":"Bengaluru"}
    - action_best_time_info

## New Story

* search_place{"searchplace":"search","city":"England"}
    - slot{"city":"England"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Anand Bhawan"}
    - slot{"locality":"Anand Bhawan"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Anand Bhawan"}
    - slot{"locality":"Anand Bhawan"}
    - action_search_place
* search_place{"searchplace":"search","locality":"Anand Bhawan","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - slot{"locality":"Anand Bhawan"}
    - action_search_place
* search_place{"searchplace":"search","locality":"swaraj"}
    - slot{"locality":"swaraj"}
    - action_search_place
* search_place{"searchplace":"search","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_search_place

## interactive_story_1
* search_place{"searchplace": "search", "locality": "Swaraj Bhawan", "city": "Allahabad"}
    - slot{"city": "Allahabad"}
    - slot{"locality": "Swaraj Bhawan"}
    - action_search_place

## interactive_story_1
* search_place{"searchplace": "search", "locality": "Swaraj bhawan", "city": "Allahabad"}
    - slot{"city": "Allahabad"}
    - slot{"locality": "Swaraj bhawan"}
    - action_search_place
* search_place{"searchplace": "search", "locality": "parliament"}
    - slot{"locality": "parliament"}
    - action_search_place
* search_place{"searchplace": "search", "city": "allahabad"}
    - slot{"city": "allahabad"}
    - action_search_place
* search_place{"searchplace": "search", "city": "Allahabad"}
    - slot{"city": "Allahabad"}
    - action_search_place
* search_place{"searchplace": "search", "city": "rome"}
    - slot{"city": "rome"}
    - action_search_place
* search_place{"searchplace": "search", "city": "Delhi"}
    - slot{"city": "Delhi"}
    - action_search_place
* search_place{"searchplace": "search", "locality": "Rashtrapati Bhavan"}
    - slot{"locality": "Rashtrapati Bhavan"}
    - action_search_place

## interactive_story_1
* search_hotels{"city": "Ranchi"}
    - slot{"city": "Ranchi"}

## interactive_story_2
* search_hotels{"city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_search_hotels

## interactive_story_3
* search_hotels{"city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_search_hotels

## interactive_story_1
* action_locate{"locality": "Anand Bhawan", "city": "Allahabad"}
    - slot{"city": "Allahabad"}
    - slot{"locality": "Anand Bhawan"}
    - action_locate

## interactive_story_1
* route{"saddr": "Ranchi", "daddr": "Jamshedpur"}
    - slot{"daddr": "Jamshedpur"}
    - slot{"saddr": "Ranchi"}
    - action_route
* route{"saddr": "jamshedpur", "daddr": "ranchi"}
    - slot{"daddr": "ranchi"}
    - slot{"saddr": "jamshedpur"}
    - action_route
* route{"saddr": "Kolkata", "daddr": "jamshedpur"}
    - slot{"daddr": "jamshedpur"}
    - slot{"saddr": "Kolkata"}
    - action_route
* route{"saddr": "Lucknow", "daddr": "Allahabad"}
    - slot{"daddr": "Allahabad"}
    - slot{"saddr": "Lucknow"}
    - action_route
* route{"saddr": "Ranchi", "daddr": "Jamshedpur"}
    - slot{"daddr": "Jamshedpur"}
    - slot{"saddr": "Ranchi"}
    - action_route
* route{"saddr": "Bokaro", "daddr": "Ranchi"}
    - slot{"daddr": "Ranchi"}
    - slot{"saddr": "Bokaro"}
    - action_route

## interactive_story_1
* search_flights{"saddr": "Ranchi", "daddr": "Mumbai"}
    - slot{"daddr": "Mumbai"}
    - slot{"saddr": "Ranchi"}
    - action_search_flights
* search_flights{"saddr": "Ranchi", "daddr": "Mumbai", "date": "2020-03-01"}
    - slot{"daddr": "Mumbai"}
    - slot{"date": "2020-03-01"}
    - slot{"saddr": "Ranchi"}
    - action_search_flights
* search_flights{"saddr": "Ranchi", "daddr": "Mumbai", "date": "2020-03-07"}
    - slot{"daddr": "Mumbai"}
    - slot{"date": "2020-03-07"}
    - slot{"saddr": "Ranchi"}
    - action_search_flights
* search_flights{"saddr": "Kolkata", "daddr": "Mumbai", "date": "2020-03-07"}
    - slot{"daddr": "Mumbai"}
    - slot{"date": "2020-03-07"}
    - slot{"saddr": "Kolkata"}
    - action_search_flights
* search_flights{"saddr": "Delhi", "daddr": "Mumbai", "date": "2020-03-07"}
    - slot{"daddr": "Mumbai"}
    - slot{"date": "2020-03-07"}
    - slot{"saddr": "Delhi"}
    - action_search_flights
* search_flights{"saddr": "Ranchi", "daddr": "Delhi", "date": "2020-03-07"}
    - slot{"daddr": "Delhi"}
    - slot{"date": "2020-03-07"}
    - slot{"saddr": "Ranchi"}
    - action_search_flights

## interactive_story_1
* search_flights{"saddr": "allahabad", "daddr": "delhi"}
    - slot{"daddr": "delhi"}
    - slot{"saddr": "allahabad"}
    - action_search_flights
    - action_search_flights
* search_flights{"saddr": "Ranchi", "daddr": "delhi", "date": "2020-02-03"}
    - slot{"daddr": "delhi"}
    - slot{"date": "2020-02-03"}
    - slot{"saddr": "Ranchi"}
    - action_search_flights
* search_nearby{"keyword": "museum"}
    - action_search_nearby
* search_nearby{"keyword": "museum", "city": "Ranchi"}
    - slot{"city": "Ranchi"}
    - action_search_nearby

## New Story

* weather{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_weather
    - slot{"city":"Ranchi"}
* search_place{"searchplace":"search","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_search_place
* pincode
    - action_city_pincode
* pincode
    - action_city_pincode
* pincode
    - action_city_pincode
* pincode{"city":"Adityapur"}
    - slot{"city":"Adityapur"}
    - action_city_pincode
* pincode{"locality":"Adityapur","city":"jamshedpur"}
    - slot{"city":"jamshedpur"}
    - slot{"locality":"Adityapur"}
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode
    - action_city_pincode
    - slot{"locality":"Adityapur"}
* pincode{"pincode":"211004"}
    - slot{"pincode":"211004"}
    - action_pincode
    - slot{"pincode":"211004"}
* best_time_info{"besttimeinfo":"best time info","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_best_time_info
* place_reach{"reachinfo":"how to reach","city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_place_reach_info
* action_locate{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_locate
* action_locate{"city":"Namkum"}
    - slot{"city":"Namkum"}
    - action_locate
* action_locate{"locality":"Namkum","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Namkum"}
    - action_locate
* action_locate{"locality":"Adityapur","city":"Jamshedpur"}
    - slot{"city":"Jamshedpur"}
    - slot{"locality":"Adityapur"}
    - action_locate
* action_locate{"locality":"Taj Mahal","city":"Agra"}
    - slot{"city":"Agra"}
    - slot{"locality":"Taj Mahal"}
    - action_locate
* action_locate{"city":"fort,delhi"}
    - slot{"city":"fort,delhi"}
    - action_locate

## New Story

* current_time
    - action_time
* current_time
    - action_time
* current_time
    - action_time
* place_info{"placeinfo":"tell me about","city":"agra"}
    - slot{"city":"agra"}
    - action_place_info
* place_reach{"reachinfo":"how to reach","city":"Nagpur"}
    - slot{"city":"Nagpur"}
    - action_place_reach_info
* place_reach{"reachinfo":"reach","city":"Pune"}
    - slot{"city":"Pune"}
    - action_place_reach_info
* route{"saddr":"Ranchi","daddr":"Nagpur"}
    - slot{"daddr":"Nagpur"}
    - slot{"saddr":"Ranchi"}
    - action_route
* route{"saddr":"namkum","daddr":"katatoli"}
    - slot{"daddr":"katatoli"}
    - slot{"saddr":"namkum"}
    - action_route
* route{"saddr":"jamshedpur","daddr":"Ranchi"}
    - slot{"daddr":"Ranchi"}
    - slot{"saddr":"jamshedpur"}
    - action_route

## New Story

* action_locate
    - action_locate
* action_locate{"locality":"Taj Mahal","city":"Agra"}
    - slot{"city":"Agra"}
    - slot{"locality":"Taj Mahal"}
    - action_locate
* route{"saddr":"Taj","daddr":"Red","city":"Fort"}
    - slot{"city":"Fort"}
    - slot{"daddr":"Red"}
    - slot{"saddr":"Taj"}
    - action_route
* action_locate{"locality":"Red Fort","city":"Agra"}
    - slot{"city":"Agra"}
    - slot{"locality":"Red Fort"}
    - action_locate
* action_locate{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - action_locate
* action_locate{"locality":"Statue","city":"Unity,Gujrat"}
    - slot{"city":"Unity,Gujrat"}
    - slot{"locality":"Statue"}
    - action_locate
* action_locate{"locality":"Gateway of India","city":"delhi"}
    - slot{"city":"delhi"}
    - slot{"locality":"Gateway of India"}
    - action_locate
* action_locate
    - action_locate
* action_locate
    - action_locate
* action_locate
    - action_locate
* action_locate{"city":"Howrah,Kolkata"}
    - slot{"city":"Howrah,Kolkata"}
    - action_locate
* action_locate
    - action_locate
* action_locate{"locality":"Howrah Bridge","city":"Kolkata"}
    - slot{"city":"Kolkata"}
    - slot{"locality":"Howrah Bridge"}
    - action_locate

## New Story

* search_hotels{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"city":"Gorakhpur"}
    - slot{"city":"Kolkata"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Namkum"}
    - slot{"city":"mesra,ranchi"}
    - action_search_hotels

## New Story

* search_hotels{"city":"Kolkata"}
    - slot{"city":"Kolkata"}
    - action_search_hotels
* search_hotels{"city":"Namkum"}
    - slot{"city":"Namkum"}
    - action_search_hotels

## New Story

* pincode{"locality":"Namkum","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Namkum"}
    - action_city_pincode
    - slot{"locality":"Namkum"}
* pincode{"locality":"Katatoli","city":"Ranchi"}
    - slot{"city":"Ranchi"}
    - slot{"locality":"Katatoli"}
    - action_city_pincode
    - slot{"locality":"Katatoli"}
* pincode{"locality":"Kailash Nagar","city":"Delhi"}
    - slot{"city":"Delhi"}
    - slot{"locality":"Kailash Nagar"}
    - action_city_pincode
    - slot{"locality":"Kailash"}
* best_time_info{"besttimeinfo":"best time to visit","city":"Chennai"}
    - slot{"city":"Chennai"}
    - action_best_time_info
* place_info{"city":"Kanpur"}
    - slot{"city":"Kanpur"}
    - action_place_info
* best_time_info{"besttimeinfo":"best time info","city":"Agra"}
    - slot{"city":"Agra"}
    - action_best_time_info
* search_flights{"saddr":"Mumbai","daddr":"Ranchi"}
    - slot{"daddr":"Ranchi"}
    - slot{"saddr":"Mumbai"}
    - action_search_flights
    - action_search_flights
* search_flights{"saddr":"Mumbai","daddr":"Ranchi","date":"2020-03-01"}
    - slot{"daddr":"Ranchi"}
    - slot{"date":"2020-03-01"}
    - slot{"saddr":"Mumbai"}
    - action_search_flights
* place_info{"city":"Rampur"}
    - slot{"city":"Rampur"}
    - action_place_info
* place_info{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - action_place_info
* place_info{"city":"Allahabad"}
    - slot{"city":"Allahabad"}
    - action_place_info
