# when user entered and exited a place.

# report duration after entry and exit
import main
from typing import List, Dict


class User:

    """
    data: {category(food): [specific(middle eastern), Time]}
    """

    food: list
    arts: list
    entertainment: list
    shopping: list
    in_home_country: bool

    def __init__(self, food, arts, entertainment, shopping, in_home_country):
        self.food = food
        self.arts = arts
        self.entertainment = entertainment
        self.shopping = shopping
        self.in_home_country = in_home_country

    def listExtender(self, oldlist):
        newList = []
        for x in oldlist:
            newList.insert(0,[x,0])
        return newList

    def otherCountryPref(self, food, arts, entertainment, shopping):
        if food != "":
            foodList = self.listExtender(food.split(","))
            self.food.insert(0,foodList)
        if arts != "":
            artsList = self.listExtender(arts.split(","))
            self.arts.insert(0,artsList)
        if entertainment != "":
            entertainmentList = self.listExtender(entertainment.split(","))
            self.entertainment.insert(0,entertainmentList)
        if shopping != "":
            shopList = self.listExtender(shopping.split(","))
            self.shopping.insert(0,shopList)
        print(self.food)
        print(self.arts)
        print(self.entertainment)
        print(self.shopping)



