import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyBYhkmFKfz745tUYWf5CskwslxKan6M_-E")


# Request directions via public transit

def return_dir(locations):
    now = datetime.now()
    concat = ""
    for loc in locations[1:-2]:
        concat += loc + '|'
    concat = concat[:-1]
    directions_result = gmaps.directions(
        locations[0],locations[-1],mode="walking",departure_time=now,waypoints=concat)
    return directions_result


"""
if __name__ == '__main__':
    print(return_dir(['Bahen Center', 'Myhal Center', 'Leslie Dan']))
    acc = return_dir(['Bahen Center', 'Myhal Center', 'Leslie Dan'])
    for legs in acc['legs']:
        print(acc[legs]["html_instructions"])
        """
