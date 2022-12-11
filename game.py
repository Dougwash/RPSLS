import time
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_1_name = ''
        self.player_1_gesture = ''
        self.player_2_name = ''
        self.player_2_gesture = ''
        self.player_1 = Human(self.player_1_name,self.player_1_gesture)
        self.player_2 = None
        self.counter = 0  
        self.hand = ['' '']      
    def game_rules(self):
        print("                Welcome to RPSLS\na game where two opponens pick a gesture to see who will win.\n")
        time.sleep(2)
        print('\nbelow is a list of gesters for you to choose from and how they are defeated\nchoose your gester wisly....\n')
        time.sleep(1)
        print('Rock crushes Scissors')
        time.sleep(1)
        print('Scissors cut Paper')
        time.sleep(1)
        print('Paper cuts Rock')
        time.sleep(1)
        print('Rock crushes Lizard')
        time.sleep(1)
        print('Spock smashes Scissors')
        time.sleep(1)
        print('Scissors decapitates Lizard')
        time.sleep(1)
        print('Lizard eats Paper')
        time.sleep(1)
        print('Paper disproves Spock')
        time.sleep(1)
        print('Spock vaporizes Rock')
        time.sleep(1)

    def find_name(self):
        self.player_1_name =input("\nWhat is player ones name? ")
        time.sleep(2)
        print(f'\nHi {self.player_1_name} Welcome to RPSLS \n')

    def ai_or_human(self):  # moved from human, needs refactor
        player_choose = input('Please enter 1 to play with a human buddy or 2 for the computer AI?\n')     
        if player_choose == '1':
            player_2_name = input('\nPlayer 2 \nplease enter your name: ')
            time.sleep(1)
            print(f"\n{player_2_name} Welcome to RPSLS you have been selected as player 2")
            self.player_2 = Human(player_2_name, player_choose) #added _name to self.payer_2

        elif player_choose == '2':
            player_2_name = "AI"
            time.sleep(2)
            print (f'{player_2_name} has been selected as player two')
            self.player_2_name = player_2_name
            self.player_2 = AI(player_2_name, player_choose)
        
        else:
            print("try again\n")
            return self.ai_or_human()
    



    def battle(self):
        while self.player_1.wins < 3 and self.player_2.wins < 3:
            time.sleep(1)
            print("\nplayer 1")
            self.player_1.choose_gesture()
            time.sleep(1)
            print(f'\n{self.player_1_name} choose {self.player_1.chosen_gesture}')
            time.sleep(1)
            print('\nplayer 2')
            self.player_2.choose_gesture()
            print(f'{self.player_2.name} choose {self.player_2.chosen_gesture}')

            if self.player_1.chosen_gesture == "Rock": 
                w_hand =['Lizard',"Scissors"] #>
                l_hand = ['Paper','Spock'] # <
                if self.player_2.chosen_gesture in w_hand:
                    self.player_1.wins += 1 
                    time.sleep(1)
                    print (f'\n{self.player_1_name} wins current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')
                elif self.player_2.chosen_gesture in l_hand:
                    self.player_2.wins += 1
                    time.sleep(1)
                    print (f'\n{self.player_2.name} wins, current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')    
                else:
                    print(f"{self.player_2_name} picked {self.player_2_gesture} which is the same gesture as player 1, please try again")
            
    
            elif self.player_1.chosen_gesture == "Scissors":
                w_hand =['Lizard','Paper'] #>
                l_hand = ['Rock','Spock'] # <
                if self.player_2.chosen_gesture in w_hand:
                    self.player_1.wins += 1 
                    time.sleep(1)
                    print (f'\n{self.player_1_name} wins current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')
                elif self.player_2.chosen_gesture in l_hand:
                    self.player_2.wins += 1
                    time.sleep(1)
                    print (f'\n{self.player_2.name} wins, current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')    
                else:
                    time.sleep(1)
                    print("player 2 picked the same gesture as player 1, please try again")

            elif self.player_1.chosen_gesture == "Paper":
                w_hand =['Rock','Spock'] #>
                l_hand = ['Lizard',"Scissors"] # <
                if self.player_2.chosen_gesture in w_hand:
                    self.player_1.wins += 1 
                    time.sleep(1)
                    print (f'\n{self.player_1_name} wins current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')
                elif self.player_2.chosen_gesture in l_hand:
                    self.player_2.wins += 1
                    time.sleep(1)
                    print (f'\n{self.player_2.name} wins, current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')    
                else:
                    time.sleep(1)
                    print("player 2 picked the same gesture as player 1, please try again")

            elif self.player_1.chosen_gesture == "Lizard":
                w_hand =['Paper','Spock'] #>
                l_hand = ['Rock',"Scissors"] # <
                if self.player_2.chosen_gesture in w_hand:
                    self.player_1.wins += 1 
                    time.sleep(1)
                    print (f'\n{self.player_1_name} wins current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')
                elif self.player_2.chosen_gesture in l_hand:
                    self.player_2.wins += 1
                    time.sleep(1)
                    print (f'\n{self.player_2.name} wins, current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')    
                else:
                    time.sleep(1)
                    print("player 2 picked the same gesture as player 1, please try again")

            elif self.player_1.chosen_gesture == "Spock":
                w_hand =['Rock',"Scissors"] #>
                l_hand = ['Lizard','Paper'] # <
                if self.player_2.chosen_gesture in w_hand:
                    self.player_1.wins += 1 
                    time.sleep(1)
                    print (f'\n{self.player_1_name} wins current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')
                elif self.player_2.chosen_gesture in l_hand:
                    self.player_2.wins += 1
                    time.sleep(1)
                    print (f'\n{self.player_2.name} wins, current score: P1:{self.player_1.wins}, P2:{self.player_2.wins}')    
                else:
                    time.sleep(1)
                    print("player 2 picked the same gesture as player 1, please try again")

    def winner(self): # if self.player_1.wins == 3       next line would just be a print saying print(F'{self.player_1.name} wins the game')
        if self.player_1.wins == 3:
            print (f'{self.player_1_name} wins the game')
            again = input ('Would you like to play again? Y/N ')
            if again == 'Y' or 'y':
                self.player_1.wins = 0
                self.player_2.wins = 0
                self.battle()
        elif self.player_2.wins == 3:
            print(f'{self.player_2.name} wins the game')
            if again == 'Y' or 'y':
                self.player_1.wins = 0
                self.player_2.wins = 0
                self.battle()
        else:
            return
             
 

        
            
            
    def run_game(self):
        self.game_rules()
        self.find_name()       
        self.ai_or_human()
        self.battle()
        self.winner()









