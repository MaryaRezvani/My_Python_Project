import random
random.choice([1, 2, 3])


class Rock_Paper_Scissors():
    """Main class for Rock Paper Scissor Game."""
    #get player choice
    #get computer choice
    #Decide winner
    #play
    def __init__(self, name:str):
        self.choices = ['rock', 'paper', 'scissor']
        self.player_name = name

    def get_player_choice(self, ):
        user_choice = input(f'Enter your choice({self.choices}):')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f'Invalid Choices, you must select from{self.choices}')
        return self.get_player_choice()
    def get_computer_choice(self):
        """get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choices)
        
    
    def decide_winner(self, user_choice:str, computer_choice:str):
        """Decide the winner of the game based on user and computer choices. 

        :param user_choice: the choice of the user.
        :type user_choice:str
        :param computer_choice: the choice of the computer.
        :type computer_choice: str
        :return: the result of the game(who won?)
        :rtype: str
        """

        if user_choice == computer_choice:
            return "It's a Tie!"
        win_combination = [('rock','scissor'),('paper', 'rock'), ('scissor', 'papar')]
        for win_comb in win_combination:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congratulations! You Won!!"
            
            return 'Oh No! the computer Won!'
        


    def play(self):
        """play the game
        - get user choice
        - get computer choice
        - decide the winner
        - print the result
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'computer choice:{computer_choice}')
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(winner_msg)

if __name__ == '__main__':
    game = Rock_Paper_Scissors('maryam')
    # game.play()

    while True:
        game.play()

        continue_game = input('Do you want to play again?(Enter any key to pay again, enter q/Q to exit!)')
        if continue_game.lower() == 'q':
            break
