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

    def __init__(self, food, arts, entertainment, shopping):
        self.food = food
        self.arts = arts
        self.entertainment = entertainment
        self.shopping = shopping



