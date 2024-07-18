import random
from typing import Tuple


def monty_hall_game(switch_doors: bool)-> bool:
    """Simulate a single Monty Hall game.

    :param switch_doors:If True, the contestant will switch their choice after a goat door is revealed.

    :return: True if the contestant won the car, False otherwise.
    :rtype: bool
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'

def simulate_game(num_games:int)-> Tuple[float, float]:
    """simulate a number of Monty Hall games and print the statistics.

    :param int num_games:the number of games to simulate. Defaults to 1000.
    """
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])

    return num_wins_without_switching, num_wins_with_switching
    
# win_counter = 0
# for _ in range(100000):
#     if monty_hall_game(False):
#         win_counter += 1

if __name__ == '__main__':
    num_games = 1000
    win_percent_without_switching, win_percent_with_switching = simulate_game(num_games)

    time.sleep(0.01)
     
    


