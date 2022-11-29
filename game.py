list_of_gestures=['Rock','Scissors','Paper','Lizard','Spock']
class Game:
    def __init__(self, player_1,player_2) -> None:
       self.game_rules() 
       self.payer_1 = player_1
       self.payer_2 = player_2
       self.list()
    #    self.list_of_gestures=['Rock','Scissors']
    #    self.list=
    #    self.list_of_gestures=[]
        
    pass
    def list(self):
        for list in list_of_gestures:
            # print(list)
            print(len(list_of_gestures))



    def game_rules(self):
        print("Welcome to RPSLS")
        print('below are a list of gesters for you to choose and how they are defeated\n choose your gester wisly....\n')
        print('Rock crushes Scissors')
        print('Scissors cut Paper')
        print('Paper cuts Rock')
        print('Rock crushes Lizard')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock\n')
        


    



Game(None, None)
print(list_of_gestures.index('Paper'))

# while 






# Game()