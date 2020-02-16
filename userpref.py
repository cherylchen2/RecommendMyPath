# when user entered and exited a place.

# report duration after entry and exit
import main

class User:

    """
    data: {category(food): [specific(middle eastern), Time]}
    """

    preferences: list
    data: dict

    def __init__(self, preferences):
        self.preferences = preferences
        
