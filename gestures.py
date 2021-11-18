class Gestures:
    
    #*changes player gesture to an index number used in function below
    
    @staticmethod
    def gesture_to_num(player_gesture):
        if player_gesture == 'Rock':
            player_gest_num = 0
        elif player_gesture == 'Paper':
            player_gest_num = 1
        elif player_gesture == 'Scissors':
            player_gest_num = 2
        elif player_gesture == 'Lizard':
            player_gest_num = 3
        elif player_gesture == 'Spock':
            player_gest_num = 4
        
        return player_gest_num
    #* Array reader method scans through an array of verbs then the numbered variables to determine the winner of each round
    
    @staticmethod    
    def array_reader(player_one_gesture, player_two_gesture):
        
        #^ First row in array is rock, Paper, Scissors, Lizard, Spock
        #& player_one is the x axis and player_two is y axis 
        
        rpsls_statements = [["Tie", "Covers", "Crushes", "Crushes", "Vaporizes"], 
                            ["Covers", "Tie", "Cuts", "Eats", "Disproves"], 
                            ["Crushes", "Cuts", "Tie", "Decapitates", "Smashes"], 
                            ["Crushes", "Eats", "Decapitates", "Tie", "Poisons"], 
                            ["Vaporizes", "Disproves", "Smashes", "Poisons", "Tie"]]
        
        rpsls_table = [[-1, 1, 0, 0, 4], 
                       [1, -1, 2, 3, 1], 
                       [0, 2, -1, 2, 4], 
                       [0, 3, 2, -1, 3], 
                       [4, 1, 4, 3, -1]]
        
        player_one = Gestures.gesture_to_num(player_one_gesture) #gets index number of player gesture
        player_two = Gestures.gesture_to_num(player_two_gesture)
            
        winner = rpsls_table[player_one][player_two] #compares against table to get winning player index number
        winner_verb = rpsls_statements[player_one][player_two] #compares against table to get winning player statement/verb
        
        #! Interpolates who wins and prints the results with the correct verbiage, while also ticking up the score.
        
        if winner == -1:
            print('This is a tie.')
        elif winner == player_one:
            print(f"   {player_one_gesture} {winner_verb} {player_two_gesture}")
            winner = 1
        elif winner == player_two:
            print(f"   {player_two_gesture} {winner_verb} {player_one_gesture}")
            winner = 2
            
        return winner