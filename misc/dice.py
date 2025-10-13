import random


def d3():
    return int(random.uniform(1, 4))


def d4():
    return int(random.uniform(1, 5))


def d6():
    return int(random.uniform(1, 7))


def d8():
    return int(random.uniform(1, 9))


def d10():
    return int(random.uniform(1, 11))


def d12():
    return int(random.uniform(1, 13))


def d20():
    return int(random.uniform(1, 21))


def dx(x):
    return int(random.uniform(1, x + 1))
