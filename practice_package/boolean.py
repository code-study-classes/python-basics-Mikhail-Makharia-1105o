# pylint: disable-all

def check_between_numbers = lambda A, B, C: (A < B < C) or (C < B < A)

def check_odd_three = lambda number: (abs(number) >= 100) and (abs(number) <= 999) and (number % 2 != 0)

def check_unique_digits = lambda number: len(set(str(abs(number)))) == 3 if 100 <= abs(number) <= 999 else False


def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]


def check_ascending_digits = lambda number: (100 <= abs(number) <= 999) and (str(abs(number)) in '123456789')