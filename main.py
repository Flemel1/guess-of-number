import random

def guess(n):
    random_number = random.randint(1,n)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter your number 1 - {n}: "))

        if guess > random_number:
            print('Your guess too high!!')
        elif guess < random_number:
            print('Your guess too low!!')

    print(f'Your guess is correctly random number = {random_number}')

guess(10)