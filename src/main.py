from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_number_random
from src.game_logic.hint_generator import provide_hint


def main():
    score = 100
    actual_number = generate_number_random(1, 100)

    while True:
        user_input = get_valid_input(1, 100)
        if user_input == actual_number:
            print('you guessed a number correctly')
            print(f'your score is: {score}')
            break
        else:
            provide_hint(user_input, actual_number)
            score -= 10
            score = max(0, score)



if __name__ == '__main__':
    main()

