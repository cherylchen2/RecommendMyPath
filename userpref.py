# when user entered and exited a place.

# report duration after entry and exit
import main
from typing import List, Dict


class User:

    """
    data: {category(food): [specific(middle eastern), Time]}
    """

    food: Dict
    arts: Dict
    entertainment: Dict
    shopping: Dict
    in_home_country: bool

    def __init__(self, food, arts, entertainment, shopping, in_home_country):
        self.food = food
        self.arts = arts
        self.entertainment = entertainment
        self.shopping = shopping
        self.in_home_country = in_home_country

    def otherCountryPref(self, food, arts, entertainment, shopping):
        if food != "":
            foodList = food.split()
            for f in foodList:
                self.food[f] = ['T',0] 
        if arts != "":
            artsList = arts.split()
            for f in artsList:
                self.arts[f] = ['T',0] 
        if entertainment != "":
            entertainmentList = entertainment.split()
            for f in entertainmentList:
                self.entertainment[f] = ['T',0] 
        if shopping != "":
            shopList = shopping.split()
            for f in shopList:
                self.shopping[f] = ['T',0] 
        print(self.food)
        print(self.arts)
        print(self.entertainment)
        print(self.shopping)



