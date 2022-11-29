from ai import AI

class Human:
    def __init__(self, player_1_name,player_2_name) -> None:
        self.player_1= player_1_name
        self.player_2 = player_2_name
        self.player1_name()
        self.ai_or_human()

        pass

    def player1_name(self):
        self.player_1_name = input('Player 1 \nplease enter your name:')
        print(f"{self.player_1_name} has been selected as player 1")
        

    def ai_or_human(self):
        print ('do you want to play with a buddy or the computer?\n')
        player_2_choose =  input('enter 1 for human player\nenter 2 for AI/Computer:')
               
        if player_2_choose == '1':
            self.player_2_name = input('Player 2 \nplease enter your name: ')
            print(f"{self.player_2_name} has been selected as player 2")

        elif player_2_choose == '2':
            self.player_2_name = AI(None).ai_player_2_name
            # self.Payer_2 = AI.select_gesture(self)
            print (f'{self.player_2_name} has been selected as player two')

        else:
            print("try again\n")
            self.ai_or_human()
    
Human(None,None)
