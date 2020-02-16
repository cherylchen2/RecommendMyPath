# when user entered and exited a place.

# report duration after entry and exit
import main
from typing import List, Dict


class User:

    """
    data: {category(food): [specific(middle eastern), Time]}
    """

    preferences: List
    data: Dict
    in_home_country: bool

    def __init__(self, preferences):
        self.preferences = preferences
        self.data = {}


