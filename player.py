class Player:
    def __init__(self):
        self.name = input('Please input your name: ')
        self.score = 0
    
    def choose_gesture(self):
        gesture = input('Please input gesture: ')
        gesture_valid = False
        
        while gesture_valid == False: 
            if gesture == 'Rock' or gesture == 'Paper' or gesture == 'Scissors' or gesture == 'Lizard' or gesture == 'Spock':
                gesture_valid = True
            else:
                gesture_valid = False

