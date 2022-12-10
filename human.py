from player import Player

class Human(Player):
    def __init__(self, name,gesture) -> None:
        super().__init__(name,gesture)
       
        

    def player1_name(self):
        player_1_name = input('Player 1 \nplease enter your name: ')
        # print(f"{player_1_name} has been selected as player 1")
        
    # human will inharet the choose gesture function from the parent



    # def pick_gesture (self):
    #     user_choice = input("press ")
    #     player_1_gesture = Player.choose_gesture(self)
    #     player_1_gesture = self.chosen_gesture
    #     # print(f'{self.chosen_gesture} was chosen for player 1\n')
    #     return player_1_gesture
  

       
    
# Human(None,None)
