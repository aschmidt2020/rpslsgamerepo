import random

class Utilities:
    
    gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    @staticmethod
    def display_rules():
        print('\nWelcome to Rock vs Paper vs Scissors vs Lizard vs Spock!'
                'You will begin by selecting if you would like to play with one or two players.'
                'If you select one player, you will play against a computer.'
                'Each player will choose a "gesture" from the following options: Rock, Paper, Scissors, Lizard, Spock.'
                'Make sure you input the capitalized version of your gesture choice (i.e. input Rock, not rock).'
                'Depending on you options, one player will win the game. See the list below for who would win.')
        print('Winners List:')
        print(' - Rock crushes Scissors')
        print(' - Scissors cuts Paper')
        print(' - Paper covers Rock')
        print(' - Rock crushes Lizard')
        print(' - Lizard poisons Spock')
        print(' - Spock smashes Scissors')
        print(' - Scissors decapitates Lizard')
        print(' - Lizard eats Paper')
        print(' - Paper disproves Spock')
        print(' - Spock vaporizes Rock')
        print('If you win a round, this will be added to your score.'
                'The game will go until someone reaches a score of two.'
                "Whichever player's score reaches two first, wins the game.")
        print("Let's begin!")
        print('***************************\n')
