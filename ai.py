import random



class AI:
    def __init__(self, player_2g) -> None:
        self.ai_player_2_name = "AI"
        self.player_2g = player_2g
        self.list_of_gestures=['Rock','Paper','Scissors','Lizard','Spock']
        self.select_gesture()
        pass

    def select_gesture(self):
        self.player_2g = random.choice(self.list_of_gestures)

        print(self.player_2g)

# AI(None)

# name = AI(None)
# print (name.ai_player_2)
