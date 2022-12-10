
class Player:
    def __init__(self, name,gesture):
        self.name = name
        self.chosen_gesture = gesture
        self.list_of_gestures=['','Rock','Paper','Scissors','Lizard','Spock'] # made emplty spot [0] to make 1-5 options line up with index position
        self.wins = 0


    
    def choose_gesture(self):  # should be good for user
        self.list_of_gestures=['','Rock','Paper','Scissors','Lizard','Spock'] # made emplty spot [0] to make 1-5 options line up with index position
        p1g = input('pick your gesture\n 1 for Rock\n 2 for Paper\n 3 for Scissors\n 4 for Lizard \n 5 Spock \n:  ')

        if p1g == '1':
            self.chosen_gesture = self.list_of_gestures[1]
            self.chosen_gesture
        elif p1g == '2':
            self.chosen_gesture = self.list_of_gestures[2]
            self.chosen_gesture
        elif p1g == '3':
            self.chosen_gesture = self.list_of_gestures[3]
            self.chosen_gesture
        elif p1g == '4':
            self.chosen_gesture = self.list_of_gestures[4]
            self.chosen_gesture
        elif p1g == '5':
            self.chosen_gesture = self.list_of_gestures[5]
            return self.chosen_gesture
        else:
            print('please try again')
            return self.choose_gesture()

        
            
    # def human_gesture_pick(self):    
    #     p2g =  input('pick your gesture\n 1 for Rock \n2 for Paper \n 3 for Scissors \n 4 for Lizard \n5 Spock \n:  ')
    #     if p2g == 1:
    #         self.player1_geture = self.list_of_gestures[1]
    #     elif p2g == 2:
    #         self.player1_geture = self.list_of_gestures[2]
    #     elif p2g == 3:
    #         self.player1_geture = self.list_of_gestures[3]
    #     elif p2g == 4:
    #         self.player1_geture = self.list_of_gestures[4]
    #     elif p2g == 5:
    #         self.player1_geture = self.list_of_gestures[5]
    #     else:
    #         print('please try again')
    #         self.player1_gesture()


# Player(None,None,None,None)
# # d=Player(None,None,None,None)
# print (player_1_name)
# print (d.player1_geture)
# print (d.player_2_name)
# print(d.player2_geture)

        # return super().player1_name()

  