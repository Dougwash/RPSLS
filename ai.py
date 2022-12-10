import random
from player import Player



class AI(Player):
    def __init__ (self,name, gesture) -> None:
        super().__init__(name, gesture)
   
    def choose_gesture(self):  # using method overide to give custom AI logic
        self.chosen_gesture = random.choice(self.list_of_gestures)
