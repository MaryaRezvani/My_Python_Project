from src. constants import UNDER_TWENTY, ABOVE_100, TENS


def num_to_word(num: int) -> str:
    """Convert a number to its word representation.
    Note:this function only works for numbers less than 10^15
    and greather than.

    :param num: the number to convert.
    :return: the word representation of the number.

    >>> num_to_word(0)
    'Zero'
    >>> num_to_word(1)
    'One'
    >>> num_to_word(10)
    'Ten'
    >>> num_to_word(1234)
    'Twelve thousand three hundred forty five'
    """
    if num < 20:
        return UNDER_TWENTY[num]
    elif num < 100:
        reminder = num % 10
        if reminder == 0:
            return TENS[num // 10]
        return TENS[num // 10] + " " + UNDER_TWENTY[reminder]
    
    pivot = max([key for key in ABOVE_100 if key <= num])
    p1 = num_to_word(num // pivot)
    p2 =  ABOVE_100[pivot]

    if num % pivot == 0:
        return f'{p1} {p2}'

    return f'{p1} {p2} {num_to_word(num % pivot)}'


if __name__ == '__main__':
    print(num_to_word(2128))
