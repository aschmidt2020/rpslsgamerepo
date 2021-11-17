from utilities import Utilities
class Gestures:
    
    @staticmethod    
    #^ First row in array is rock, Paper, Scissors, Liard, Spock
    def array_reader(player_one_gesture, player_two_gesture):
        
        rpsls_table = [[-1, 1, 0, 0, 4], 
                       [1, -1, 2, 3, 1], 
                       [0, 2, -1, 2, 4], 
                       [0, 3, 2, -1, 3], 
                       [4, 1, 4, 3, -1]]
        
        player_one = Utilities.gesture_list.index(player_one_gesture)
        player_two = Utilities.gesture_list.index(player_two_gesture)
        rpsls_table[player_one] [player_two]
        
        if rpsls_table[player_one] [player_two] == -1:
            print("Tie")
        elif rpsls_table[player_one] [player_two] == 1:
            print("Win")
        elif rpsls_table[player_one] [player_two] == 0:
            print("Loss")
        elif rpsls_table[player_one] [player_two] == :
            pass
        elif rpsls_table[player_one] [player_two] == :
            pass
    
    
    @staticmethod
    def gesture_win_or_lose(player_one_gesture, player_two_gesture):
        winner = ''
        
        if player_one_gesture == player_two_gesture:
            print("   Tie")
            winner = 'No one wins'
            
        elif player_one_gesture == "Rock":
            if player_two_gesture == "Scissors":
                print("   Rock Breaks Scissors")
                winner = 'Player 1'
            elif player_two_gesture == "Paper":
                print("   Paper Covers Rock")
                winner = 'Player 2'
            elif player_two_gesture == "Lizard":
                print("   Rock Crushes Lizard!")
                winner = 'Player 1'
            elif player_two_gesture == "Spock":
                print("   Spock Vaporizes Rock!")
                winner = 'Player 2'
                
        elif player_one_gesture == "Paper":
            if player_two_gesture == "Rock":
                print("   Paper Covers Rock!")
                winner = 'Player 1'
            elif player_two_gesture == "Scissors":
                print("   Scissors Cuts Paper!")
                winner = 'Player 2'
            elif player_two_gesture == "Spock":
                print("   Paper Disproves Spock")
                winner = 'Player 1'
            elif player_two_gesture == "Lizard":
                print("   Lizard Eats Paper!")
                winner = 'Player 2'
            
        elif player_one_gesture == "Scissors":
            if player_two_gesture == "Paper":
                print("   Scissors Cut Paper!")
                winner = 'Player 1'
            elif player_two_gesture == "Rock":
                print("   Rock Crushes Scissors!")
                winner = 'Player 2'
            elif player_two_gesture == "Lizard":
                print("   Scissors Decapitate Lizard!")
                winner = 'Player 1'
            elif player_two_gesture == "Spock":
                print("   Spock Smashes Scissors")
                winner = 'Player 2'      
    
        elif player_one_gesture == "Spock":
            if player_two_gesture == "Rock":
                print("   Spock Vaporizes Rock!")
                winner = 'Player 1'
            elif player_two_gesture == "Paper":
                print("   Paper Disproves Spock!")
                winner = 'Player 2'
            elif player_two_gesture == "Scissors":
                print("   Spock Smashes Scissors")
                winner = 'Player 1'
            elif player_two_gesture == "Lizard":
                print("   Lizard Poisons Spock!")
                winner = 'Player 2'     
    
        elif player_one_gesture == "Lizard":
            if player_two_gesture == "Paper":
                print("   Lizard Eats Paper!")
                winner = 'Player 1'
            elif player_two_gesture == "Rock":
                print("   Rock Crushes Lizard!")
                winner = 'Player 2'
            elif player_two_gesture == "Spock":
                print("   Lizard Poisons Spock")
                winner = 'Player 1'
            elif player_two_gesture == "Scissors":
                print("   Scissors Decapitate Lizard!")
                winner = 'Player 2'
    
        return winner