import random

def d3():
    x= int(random.uniform(1, 4))
    return x

def d4():
    x= int(random.uniform(1,5))
    return x

def d6():
    x= int(random.uniform(1, 7))
    return x

def d8():
   x= int(random.uniform(1, 9))
   return x

def d10():
    x= int(random.uniform(1, 11))
    return x

def d12():
    x= int(random.uniform(1, 13))
    return x

def d20():
    x= int(random.uniform(1, 21))
    return x

def dx(x):
    y= int(random.uniform(1, x + 1))
    return y