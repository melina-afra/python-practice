import random

number_to_guess = random.randint(4,44)
true=random.randint(4,44)


while true:
    user_guess=int(input("enter ur guess between 4 to 44:"))
    if user_guess > number_to_guess:
       print('ur number is larger than main number')
    elif user_guess < number_to_guess:
       print('ur number ir lower than main number')
    else:
       print('I appreciate to u, u are a winner')
       continue