from player import Player
from utilities import Utilities
import random

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.set_computer_name()
    
    def set_computer_name(self):
        self.name = Utilities.choose_computer_name()
        
    def choose_gesture(self):
        gesture = input('Please input gesture: ')
        gesture_valid = False
        
