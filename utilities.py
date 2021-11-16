import random

class Utilities:
    
    @staticmethod
    def list_of_choices():
        choice_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        return choice_list
        
    @staticmethod
    def choose_computer_name():
        comp_name_list = ['Harry', 'Ron', 'Hermione', 'Crookshanks']
        comp_name = random.choice(comp_name_list)
        return comp_name