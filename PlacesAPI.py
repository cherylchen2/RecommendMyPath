import requests
import json
import time
import random as random


SEARCH_ENDPOINT = "https://maps.googleapis.com/maps/api/place/textsearch/json"
DETAILS_ENDPOINT = "https://maps.googleapis.com/maps/api/place/details/json"
ROUTE_ENDPOINT = "https://maps.googleapis.com/maps/api/distancematrix/json"
API_KEY = "AIzaSyBYhkmFKfz745tUYWf5CskwslxKan6M_-E"  # MUST CHANGE API KEY
RADAR_API_KEY = "prj_test_sk_5e80f86e68d87ab6840de34f8d3ff00f93e476b9"

#This is just some safe default headers to make sure our connection doesnt somehow get dropped! Ignore these for now
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

#The API to get details about a place given a place id!
def api_details(id):
    parameters = {"place_id":id, "key":API_KEY}

    response = requests.get(url=DETAILS_ENDPOINT,params=parameters, headers=headers)

    return response.json()

#The API to search for a place given some query text
def api_search(text, userLocation):
    parameters = {"query": text, "key": API_KEY, "location":"43.662127,-79.387779", "radius":2000}

    response = requests.get(url=SEARCH_ENDPOINT,params=parameters, headers=headers)
    #print(response.json())
    return response.json()


def pull_data(input_text, userLocation):
    #print("Called pulldata")
    data = {}

    for result in api_search(input_text, userLocation)['results']:
        #print("Called apisearch")
        #print(result)
        name = result['name']
        data[name] = result
        data[name]["descr"] = ""

        details = api_details(result['place_id'])
       # print("BHours: ")

        if 'result' not in details: continue

        #These if statements check if the key is actually in the JSON object, AKA they check if the place actually
        # has opening hours, or has reviews before trying to access them! This is a safe practice
        if 'opening_hours' in details['result'] and 'weekday_text' in details['result']['opening_hours']:
            for open_day in details['result']['opening_hours']['weekday_text']:
                #print("  "+open_day)
                data[name]["descr"] += open_day + "|| "
        #print(data)
        #print("pull_data done")
    if data is None:
        return None
    else :
        print(len(data))
        randomNum = random.randint(0,len(data))
        x = 0
        for k in data.keys():
            if x != randomNum:
                x = x + 1
            else:
                output = data.get(k)
                return output
 #       if data.keys is not None:
  #          output = random.choice(list(data.keys()))



def find_route(place_ids, mode="transit", departure_time=0):
    if departure_time == 0:
        departure_time = time.time() // 1
    parameters = {
        "key": API_KEY, 
        "origins": "|".join(["place_id:"+place_id for place_id in place_ids[1:]]), "destinations": "place_id:" + place_ids[0],
        "mode": mode#,
        #"departure_time": departure_time
    }
    response = requests.get(url=ROUTE_ENDPOINT, params=parameters, headers=headers)
    return response.json()




def radar_events():
    h = headers
    h['Authorization']=RADAR_API_KEY

    result = requests.get("https://api.radar.io/v1/events", headers = h)
    print(result.json())
    return result.json()


'''
if __name__ == "__main__":

    #Main program loop
    while True:
        try:
            input_text = input("Enter your query text: ")
            if (input_text == "quit"): exit(0)
            places = pull_data(input_text)
            # while True:
            #     for i in range(len(places)):
            #         print("{0}: {1}".format(i, places[i]))
            #     input_text = input("Would you like to remove any of these items?")
            #     try:
            #         places.pop(int(input_text), None)

            #     except:
            #         print("Please input a number")
            #     if input_text == "":
            #         break
            # print(find_route([place['place_id'] for place in places.values()]))
            radar_events()
            
        #Exit on ctrl+c
        except KeyboardInterrupt:
            print("Exiting program")
            exit(0)
'''