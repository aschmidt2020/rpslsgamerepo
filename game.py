from computer_player import ComputerPlayer
from human_player import HumanPlayer
from utilities import Utilities
from gestures import Gestures

#^ This class holds the gameplay, which runs through a large loop to determine the winner

class PlayGame:
    def __init__(self):
        Utilities.display_rules()
        self.player_one = ''
        self.player_two = ''
        self.get_players()
    
    #! Takes the user input for either one or two players and runs the loops accordingly
        
    def get_players(self):
        num_players_valid = False
        
        while num_players_valid == False:
            num_players = int(input('How many players? (1 or 2): '))
        
            if num_players == 2:
                print('\nPlayer One -->')
                self.player_one = HumanPlayer()
                
                print('Player Two -->')
                self.player_two = HumanPlayer()
                
                print('\nCurrent players: ')
                print(f'Player One Name: {self.player_one.name}')
                print(f'Player Two Name: {self.player_two.name}')
                
                num_players_valid = True
                
            elif num_players == 1:
                print('\nPlayer One -->')
                self.player_one = HumanPlayer()
                
                #computer picking name
                self.player_two = ComputerPlayer()
                
                print('\nCurrent players: ')
                print(f'Player One Name: {self.player_one.name}')
                print(f'Player Two Name: {self.player_two.name}')
                
                num_players_valid = True
        
    #& A very large and somewhat redundant loop that will be cleaned up, but for the moment functions in printing the correct results for each input possibility
        
    def play_game(self):
        round = 1
        
        print('\n*******STARTING GAME*******')
        
        while self.player_one.score < 2 and self.player_two.score < 2:
            print(f'\nRound {round}***')
            
            print(f'{self.player_one.name} --> ')
            player_one_gesture = self.player_one.choose_gesture()
            print(f'{self.player_two.name} --> ')
            player_two_gesture = self.player_two.choose_gesture()
            
            print('\nRound Result: ')
            
            round_winner = Gestures.gesture_win_or_lose(player_one_gesture, player_two_gesture)
            
            if round_winner == 'Player 1':
                self.player_one.score +=1
            elif round_winner == 'Player 2':
                self.player_two.score += 1
            elif round_winner == 'No one wins':
                continue
                  
            print(f"   {self.player_one.name}'s score: {self.player_one.score}, {self.player_two.name}'s score: {self.player_two.score}")
            round = round + 1
       
       #* Best two out of three wins
        
        if self.player_one.score == 2:
            print(f'\n{self.player_one.name} WINS!!!\n')
            round = 1
        elif self.player_two.score == 2:
            print(f'\n{self.player_two.name} WINS!!!\n')
            round = 1
