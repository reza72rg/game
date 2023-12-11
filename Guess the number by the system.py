import random
i=0
y=100
javab='k'
answer=int(input("What is your number: "))
if answer >=0 and answer <=100:
    num=random.randint(i,y)
    while javab=='small' or javab=='big' or javab=='correct':
        print("The number guess by computer is: ",num)
        javab=input("Your answer is k or b or d :")
        if javab=='small':
            y=num
        if javab=='big':
            i=num
        if javab=='correct':
            print("Your number is right: ",num)
            break
        num=random.randint(i,y)
else:
    print("The number is wrong")

