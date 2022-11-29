from human import Human


class Player(Human):
    def __init__(self, player_1_name, player1_gesture, player_2_name, player2_gesture ) -> None:
        super().__init__(player_1_name, player_2_name)
        self.player1_geture = player1_gesture
        self.list_of_gestures=['','Rock','Paper','Scissors','Lizard','Spock']
        self.player2_geture = player2_gesture


    def player1_gesture(self,p1g):

        print (self.list_of_gestures)
        p1g = input('pick your gesture\n 1 for Rock \n2 for Paper \n 3 for Scissors \n 4 for Lizard \n5 Spock \n:  ')
        if p1g == 1:
            self.player1_geture = self.list_of_gestures[1]
        elif p1g == 2:
            self.player1_geture = self.list_of_gestures[2]
        elif p1g == 3:
            self.player1_geture = self.list_of_gestures[3]
        elif p1g == 4:
            self.player1_geture = self.list_of_gestures[4]
        elif p1g == 5:
            self.player1_geture = self.list_of_gestures[5]
        else:
            print('please try again')
            self.player1_gesture()

    def player2_gesture (self):
        if self.player_2_name == "AI" :
            return  
        
        else:
            self.human_gesture_pick()
            
    def human_gesture_pick(self):    
        p2g =  input('pick your gesture\n 1 for Rock \n2 for Paper \n 3 for Scissors \n 4 for Lizard \n5 Spock \n:  ')
        if p2g == 1:
            self.player1_geture = self.list_of_gestures[1]
        elif p2g == 2:
            self.player1_geture = self.list_of_gestures[2]
        elif p2g == 3:
            self.player1_geture = self.list_of_gestures[3]
        elif p2g == 4:
            self.player1_geture = self.list_of_gestures[4]
        elif p2g == 5:
            self.player1_geture = self.list_of_gestures[5]
        else:
            print('please try again')
            self.player1_gesture()


        # return super().player1_name()

  