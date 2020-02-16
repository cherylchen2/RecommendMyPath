#import places as places
import PlacesAPI as placesApi
import userpref as userpref
import map

if __name__ == "__main__":
    #Get user input
    userSimInput = input("Simulate in home country or outside of home country?")
    if  userSimInput == "In":
        user = userpref.User([["Chinese",4],["Korean",4], ["Quiet",3], ["Mediterranean",1]],[["Fine arts",3],["Theatre",2]],[["Movie",8],["KTV",2]],[["Althetic",3],["Formal",2]], True)
    else:
        user = userpref.User([["Chinese",4],["Korean",4], ["Quiet",3], ["Mediterranean",1]],[["Fine arts",3],["Theatre",2]],[["Movie",8],["KTV",2]],[["Althetic",3],["Formal",2]], False)
    i = 0
    listCategory = {"Restaurant":0,"Arts & Culture":0,"Entertainment":0,"Shopping":0}

    if (user.in_home_country == False):
        done = 0
        newFoodPref = ""
        newArtPref = ""
        newEntInput = ""
        newShopInput = ""
        while done != 1:
            print("What do you want to try in this new country?\nCategories to add new prefereces for:\n0: Restaurant\n1: Arts & Culture\n2: Entertainment\n3: Shopping\nSeparated by commas. -1 to exit\n")
            userQuery = int(input())
            if (userQuery == 0):
                print("What do you want to try new in food?")
                newFoodPref = input()
            if (userQuery == 1):
                print("What do you want to try new in Arts & Culture?")
                newArtPref = input()
            if (userQuery == 2):
                print("What do you want to try new in the Entertainment?")
                newEntInput = input()
            if (userQuery == 3):
                print("What do you want to try new in the Shopping")
                newShopInput = input()
            if (userQuery == -1):
                done = 1
        user.otherCountryPref(newFoodPref, newArtPref, newEntInput, newShopInput)

        

    

    while i == 0:
        print("Select categories:\n0: Restaurant\n1: Arts & Culture\n2: Entertainment\n3: Shopping\n")
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
    '''
    for i in range(len(places)):
        print("{0}: {1}".format(i, places[i]))
        input_text = input("Would you like to remove any of these items?")
        #if input_text != 0 
        try:
            print(input_text)
            places.pop(int(input_text), None)
        except:
            print("Please input a number")
        if input_text == "":
            break
        '''
    if len(places) != 0:
        good = placesApi.find_route([place['place_id'] for place in places])
        lst_loc = []

        raw = good['origin_addresses']
        raw.reverse()
        for elements in raw:
            lst_loc.append(elements)
        raw2 = good['destination_addresses']
        for e2 in raw2:
            lst_loc.append(e2)
        if lst_loc == []:
            print("Sorry, the algorithm did not return any results.")
            print("Hint: Pack your day with more engaging activities by adding more preferences!")
        else:
            print("Here is your itinerary, a list of addresses in order.")
            print("Simply use this guide to fill your day with very engaging activities!")
            print(lst_loc)

    print("The Algorithm has finished running. Enjoy your trip!")




    print(placesApi.find_route([place['place_id'] for place in places]))
    print("Done")

            


    #Call api functions
    #coordinates = "2.230225,48.817716"
    #x = places.findPlaces(coordinates)
    #printall(x)

