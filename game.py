from random import randint


def number_big(start, stop):
    print('I am sorry... your guess is too big!!!\n')
    number = int(input(f'Please enter a number between {start} or {stop}:  '))
    return number

def number_small(start, stop):
    print('I am sorry... your guess is too small!!!\n')
    number = int(input(f'Please enter a number between {start} or {stop}:  '))
    return number

num = randint(0,100)
start = 0
stop = 100
counter = 0
name = input('What is your name?  ')
number = int(input('Enter a number between 0 and 100:  '))

while num != number:
    if number > num and number > start and number <= stop:
        stop = number
        number = number_big(start, stop)
    elif number < num and number > start and number <= stop:
        start = number
        number = number_small(start, stop)
    else:
        number = int(input(f'Your number is wrong \nPlease enter a number between {start} and {stop}:  '))
    counter += 1    

else:
    print(f'\nGood job {name}! You guessed the number after {counter} tries!')
