def provide_hint(guess, actual_number):
    if guess < actual_number:
        print('your guess is too low.')
    elif guess > actual_number:
        print('your guess is too high.')
            