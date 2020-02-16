#import places as places
import PlacesAPI as placesApi
import userpref as userpref

if __name__ == "__main__":
    #Get user input
    user = userpref.User({"Chinese":3,"Korean": 4, "Quiet": 1, "Mediterranean": 3},{"Fine arts":3,"Theatre":2},{"Movie":8,"KTV":2},{"Althetic":3,"Formal":2})
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
    input = ""
    for c in listCategory:
        if c == 1:
            if c == "Restaurant":
                if len(user.food) > 5:
                    for f in user.food:
                        input = input + f
                else:
                    for f in user.food:
                        input = input + f
            if c == "Arts & Culture":
                if len(user.arts) > 5:
                    for a in user.arts:
                        input = input + a
                else:
                    for a in user.arts:
                        input = input + a
            if c == "Entertainment":
                if len(user.entertainment) > 5:
                    for f in user.entertainment:
                        input = input + f
                else:
                    for f in user.entertainment:
                        input = input + f
            else:
                if len(user.shopping) > 5:
                    for f in user.shopping:
                        input = input + f
                else:
                    for f in user.shopping:
                        input = input + f
    places = placesApi.pull_data(input)
    print(places)
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

