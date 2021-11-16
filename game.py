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
        while self.player_one.score < 2 and self.player_two.score < 2:
            print("Player One")
            player_one_gesture = self.player_one.choose_gesture()
            print("Player Two")
            player_two_gesture = self.player_two.choose_gesture()
            
            if player_one_gesture == player_two_gesture:
                    print("Tie")
            elif player_one_gesture == "Rock":
                if player_two_gesture == "Scissors":
                    print("Rock Breaks Scissors")
                    self.player_one.score += 1
                elif player_two_gesture == "Paper":
                    print("Paper Covers Rock")
                    self.player_two.score += 1
                elif player_two_gesture == "Lizard":
                    print("Rock Crushes Lizard!")
                    self.player_one.score += 1
                elif player_two_gesture == "Spock":
                    print("Spock Vaporizes Rock!")
                    self.player_two.score += 1
                    
            elif player_one_gesture == "Paper":
                if player_two_gesture == "Rock":
                    print("Paper Covers Rock!")
                    self.player_one.score += 1
                elif player_two_gesture == "Scissors":
                    print("Scissors Cuts Paper!")
                    self.player_two.score += 1
                elif player_two_gesture == "Spock":
                    print("Paper Disproves Spock")
                    self.player_one.score += 1
                elif player_two_gesture == "Lizard":
                    print("Lizard Eats Paper!")
                    self.player_two.score += 1
                
            elif player_one_gesture == "Scissors":
                if player_two_gesture == "Paper":
                    print("Scissors Cut Paper!")
                    self.player_one.score += 1
                elif player_two_gesture == "Rock":
                    print("Rock Crushes Scissors!")
                    self.player_two.score += 1
                elif player_two_gesture == "Lizard":
                    print("Scissors Decapitate Lizard!")
                    self.player_one.score += 1
                elif player_two_gesture == "Spock":
                    print("Spock Smashes Scissors")
                    self.player_two.score += 1       
        
            elif player_one_gesture == "Spock":
                if player_two_gesture == "Rock":
                    print("Spock Vaporizes Rock!")
                    self.player_one.score += 1
                elif player_two_gesture == "Paper":
                    print("Paper Disproves Spock!")
                    self.player_two.score += 1
                elif player_two_gesture == "Scissors":
                    print("Spock Smashes Scissors")
                    self.player_one.score += 1
                elif player_two_gesture == "Lizard":
                    print("Lizard Poisons Spock!")
                    self.player_two.score += 1       
        
            elif player_one_gesture == "Lizard":
                if player_two_gesture == "Paper":
                    print("Lizard Eats Paper!")
                    self.player_one.score += 1
                elif player_two_gesture == "Rock":
                    print("Rock Crushes Lizard!")
                    self.player_two.score += 1
                elif player_two_gesture == "Spock":
                    print("Lizard Poisons Spock")
                    self.player_one.score += 1
                elif player_two_gesture == "Scissors":
                    print("Scissors Decapitate Lizard!")
                    self.player_two.score += 1       
            
            print(f"Player One Score {self.player_one.score}, Player Two Score {self.player_two.score}")
        
        if self.player_one.score == 2:
            print("Player One Wins!")
        elif self.player_two.score == 2:
            print("Player Two Wins!")   

            
        
    
