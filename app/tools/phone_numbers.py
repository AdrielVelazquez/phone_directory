import random


def get_random_start_n():
    return random.randrange(2, 10)


def get_random_other_digits():
    return random.randrange(0, 10)

def get_phone_number(state=None):
    return False