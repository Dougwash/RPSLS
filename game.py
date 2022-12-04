import time
from human import Human
from ai import AI


class Game:
    def __init__(self):
    #    self.game_rules()
    #    self.run_game(self)
       self.player_1_name = ''
       self.player_1_gesture = ''
       self.player_2_name = ''
       self.player_2_gesture = ''
    #    self.gestuer_lisset = self.gestuer_lisset
    #    self.player_1g = Human(self.player_1_gesture)
       self.player_1 = Human(self.player_1_name,self.player_1_gesture)
    #    self.player_2 = self.player_2_name,self.player_2_gesture
    #    self.player_2 = None  # might need human or Ai class
        
    def game_rules(self):
        
        print("Welcome to RPSLS\n a game where two opponens pick a gesture to see who will win.\n")
        print('below is a list of gesters for you to choose from and how they are defeated\n choose your gester wisly....\n')
        print('Rock crushes Scissors')
        print('Scissors cut Paper')
        print('Paper cuts Rock')
        print('Rock crushes Lizard')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock\n')
        time.sleep(1)
        
    def find_name(self):
        user_name = input("what is player ones name? ")
        self.player_1_name = user_name
        return self.player_1_name



    def ai_or_human(self):  # moved from human, needs refactor
        player_choose = input('Enter 1 to play with a human buddy or 2 for the computer?\n')     
        if player_choose == '1':
            player_2_name = input('Player 2 \nplease enter your name: ')
            print(f"{player_2_name} has been selected as player 2")
            self.player_2_name = player_2_name #Human(player_2_name, player_choose) #added _name to self.payer_2
            self.player_2_gesture = Human.choose_gesture(self)
            return self.player_2_name, self.player_2_gesture

        elif player_choose == '2':
            player_2_name = "AI"
            # self.Payer_2 = AI.select_gesture(self)
            print (f'{player_2_name} has been selected as player two')
            self.player_2_name = player_2_name
            player_2_gesture = AI.choose_gesture(self)
            self.player_2_gesture = player_2_gesture
            return self.player_2_name,self.player_2_gesture
        else:
            print("try again\n")
            return self.ai_or_human(self)
    

    def choose_gesture(self):
        
        p1g = Human.pick_gesture(self)
        self.player_1_gesture = p1g

        # chosen_gesture = input('what gesutre would you like to choose? ')
        return self.player_1_gesture


    def run_game(self):
        self.game_rules()
        self.find_name()
        self.choose_gesture()       
        self.ai_or_human()
        print(self.player_1_name)
        print(self.player_1_gesture)
        print(self.player_2_name)
        print(self.player_2_gesture)
        

    def battle(self):
        if self.player_1_gesture != self.player_2_gesture :
            return self.battle()

        elif self.player_1_gesture == "Rock":
            "Rock" > "Scissors"
            'Rock' < 'Paper'
            "Rock" > "Lizard"
            "Rock" < 'Spock'
        elif self.player_1_gesture == "Scissors":
            'Scissors' > "Paper"
            'Scissors' < "Spock"
            'Scissors' > "Lizard"
            'Scissors' > "Paper"
        elif self.player_1_gesture == "Paper":
            
        elif self.player_1_gesture == "Lizard":
        elif self.player_1_gesture == "Spock":
            
        # create a function to play the hands , test p1 and p2 ability to pick a gesture
        # using if, elif and else to check for win conditions looking at each players chosen gesture self.player_1.chosen_gesures 








