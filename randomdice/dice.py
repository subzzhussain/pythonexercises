import random

def dice():
    first_roll = random.randint(1,6)
    second_roll = random.randint(1,6)

    return first_roll + second_roll

final_roll = dice(first_roll, second_roll)
print(final_roll)