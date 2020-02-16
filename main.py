#import places as places

def main():
    #Get user input
    i = 0
    listPreferences = {"Restaurant":0,"Arts & Culture":0,"Entertainment":0,"Shopping":0}
    while i == 0:
        print("Select preferences:\n0: Restaurant\n1: Arts & Culture\n2: Entertainment\n3: Shopping\n")
        userInput = int(input())
        if (userInput == 0):
            listPreferences["Restaurant"] = 1
        if (userInput == 1):
            listPreferences["Arts & Culture"] = 1
        if (userInput == 2):
            listPreferences["Entertainment"] = 1
        if (userInput == 3):
            listPreferences["Shopping"] = 1
        print("Do you want to add additional preferences\n0:No\n1:Yes")
        print(listPreferences)
        userInput = int(input())
        if (userInput == 0):
            i = 1
    #Call api functions
    #coordinates = "2.230225,48.817716"
    #x = places.findPlaces(coordinates)
    #printall(x)




if __name__ == "__main__":
    main()
