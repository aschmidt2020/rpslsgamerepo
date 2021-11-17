from game import PlayGame

game = PlayGame()
game.play_game()

# Created a branch for feature research and coding using a Gesture Class
gesture_list = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3: 'Lizard', 4: 'Spock'}
rpsls_table = [[-1, 1, 0, 0, 4], 
               [1,-1, 2, 3, 1], 
               [0,2,-1,2,4], 
               [0, 3, 2, -1, 3], 
               [4, 1, 4, 3, -1]]

# beats = {'Rock': "Scissors" and "Lizard", 'Scissors': "Lizard" and "Paper", 'Paper': "Rock" and "Spock", "Lizard": "Spock" and "Paper", "Spock": "Rock" and "Scissors"}