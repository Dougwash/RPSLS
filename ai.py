import random
from player import Player



class AI(Player):
    def __init__ (self,name, gesture) -> None:
        super().__init__(name, gesture)
   
    def choose_gesture(self):  # using method overide to give custom AI logic
        self.chosen_gesture = random.choice(self.list_of_gestures)
        if self.chosen_gesture == '': # added 'if' so random choice can compensate for "" in position [0] of list 
            self.choose_gesture()
