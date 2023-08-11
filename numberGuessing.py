import random

numbers = []
for i in range(100):
    numbers = numbers + [i]

rand_number = random.choice(numbers)

def user_input():
    try:
        guess = int(input('Write a number from 0 to 100: '))
        num_processing(guess)        
    except:
        print('Your entry must be a number')
        user_input()

def num_processing(guess):
    if guess == rand_number:
        print(f'Congratulations! \n"{guess}" is the correct guess.')
        return
    elif guess < rand_number:
        print('Your guess is lower than the correct number. \n')
        user_input()
    else:
        print('Your guess is higher than the correct number.\n')
        user_input()
        
user_input()