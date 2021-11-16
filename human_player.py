from player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.set_player_name()
    
    def set_player_name(self):
        self.name = input('Please input your name: ')

    def choose_gesture(self):
        gesture_valid = False
        
        while gesture_valid == False:
            gesture = input('Please input gesture: ')
            if gesture == 'Rock' or gesture == 'Paper' or gesture == 'Scissors' or gesture == 'Lizard' or gesture == 'Spock':
                gesture_valid = True
            else:
                gesture_valid = False
        
        print(gesture) 
        return gesture

player_one = HumanPlayer()
print(player_one.name)

player_one.choose_gesture()


