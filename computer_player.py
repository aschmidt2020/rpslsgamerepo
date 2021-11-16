from player import Player
from utilities import Utilities
import random

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.set_computer_name()
    
    def set_computer_name(self):
        comp_name_list = ['Harry', 'Ron', 'Hermione', 'Crookshanks']
        self.name = random.choice(comp_name_list)
        
    def choose_gesture(self):
        gesture = random.choice(Utilities.list_of_choices)
        print(gesture)
        return gesture

computer_one = ComputerPlayer()
print(computer_one.name)

computer_one.choose_gesture()