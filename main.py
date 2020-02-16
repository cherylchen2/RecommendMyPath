#import places as places
import PlacesAPI as placesApi
import userpref as userpref

if __name__ == "__main__":
    #Get user input
    user = userpref.User({"Chinese":4,"Korean": 4, "Quiet": 3, "Mediterranean": 1},{"Fine arts":3,"Theatre":2},{"Movie":8,"KTV":2},{"Althetic":3,"Formal":2})
    i = 0
    listCategory = {"Restaurant":0,"Arts & Culture":0,"Entertainment":0,"Shopping":0}
    while i == 0:
        print("Select preferences:\n0: Restaurant\n1: Arts & Culture\n2: Entertainment\n3: Shopping\n")
        userInput = int(input())
        if (userInput == 0):
            listCategory["Restaurant"] = 1
        if (userInput == 1):
            listCategory["Arts & Culture"] = 1
        if (userInput == 2):
            listCategory["Entertainment"] = 1
        if (userInput == 3):
            listCategory["Shopping"] = 1
        print("Do you want to add additional categories\n0:No\n1:Yes")
        print(listCategory)
        userInput = int(input())
        if (userInput == 0):
            i = 1
    inpute = ""
    places = []
    for c in listCategory.keys():
        if listCategory.get(c) == 1:
            if c == "Restaurant":
                for f in user.food:
                    result = placesApi.pull_data(f, "43.662127, -79.387779")
                    if result is not None:
                        places.append(result)
                        break
            elif c == "Arts & Culture":
                for f in user.arts:
                    result = placesApi.pull_data(f, "43.662127, -79.387779")
                    if result is not None:
                        places.append(result)
                        break
            elif c == "Entertainment":
                for f in user.entertainment:
                    result = placesApi.pull_data(f, "43.662127, -79.387779")
                    if result is not None:
                        places.append(result)
                        break
            elif c == "Shopping":
                for f in user.shopping:
                    result = placesApi.pull_data(f, "43.662127, -79.387779")
                    if result is not None:
                        places.append(result)
                        break

    # print(inpute)
    # places = placesApi.pull_data(inpute, "43.662127, -79.387779")
    # print(places)
    for i in range(len(places)):
        print("{0}: {1}".format(i, places[i]))
        input_text = input("Would you like to remove any of these items?")
        try:
            places.pop(int(input_text), None)
        except:
            print("Please input a number")
        if input_text == "":
            break
    if len(places) != 0:
        print(placesApi.find_route([place['place_id'] for place in places.values()]))
    print("Done")
            


    #Call api functions
    #coordinates = "2.230225,48.817716"
    #x = places.findPlaces(coordinates)
    #printall(x)

