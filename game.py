from random import randint
def number_big(start,stop):
    print('I am sory ... your guess is big!!!')
    number=int(input(f'Please Enter number between {start} or {stop}='))
    return number
def number_small(start,stop):
    print('I am sory ... your guess is small!!!')
    number=int(input(f'Please Enter number between {start} or {stop}='))
    return number
num=randint(0,100)
start=0
stop=100
counter=0
name=input('What is your name? ')
number=int(input('Enter a number betwin 0 to 100 :'))
while num!=number:
    if number>num and number>start and number<=stop:
        stop=number
        number=number_big(start,stop)
    elif number<num and number>start and number<=stop:
        start=number
        number=number_small(start,stop)
    else:
        number=int(input(f'Your number is wrong \nPlease Enter number betwin {start} or {stop}='))
    counter+=1    
else:
    print(f'{name} you very look your can guess this number after {counter} tried . I congratulate you')
