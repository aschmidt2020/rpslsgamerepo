from _typeshed import Self
from computer_player import ComputerPlayer
from human_player import HumanPlayer
from utilities import Utilities


class PlayGame:
    def __init__(self):
        Utilities.display_rules()
        self.player_one = ''
        self.player_two = ''
        self.get_players()
    
    def get_players(self):
        num_players_valid = False
        
        while num_players_valid == False:
            num_players = int(input('How many players? (1 or 2): '))
        
            if num_players == 2:
                self.player_one = HumanPlayer()
                print(f'Player One Name: {self.player_one.name}')
                self.player_two = HumanPlayer()
                print(f'Player Two Name: {self.player_two.name}')
                num_players_valid = True
                
            elif num_players == 1:
                self.player_one = HumanPlayer()
                print(f'Player One Name: {self.player_one.name}')
                self.player_two = ComputerPlayer()
                print(f'Player Two Name: {self.player_two.name}')
                num_players_valid = True
        
    def play_game(self):
        pass
        #for round in range(3):
            
        
    
