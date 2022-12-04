import random
from player import Player



class AI(Player):
    def __init__ (self,name,gesture) -> None:
        super().__init__(name,gesture)
   
    def choose_gesture(self):  # using method overide to give custom AI logic
        chosen_gesture = random.choice(self.list_of_gestures)
        self.gesture = chosen_gesture
        print(f'AI choose {self.gesture}')
        return self.gesture

# AI(None)

# name = AI(None)
# print (name.ai_player_2)
