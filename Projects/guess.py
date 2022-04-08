# thing i made after trying to find something to make in python
# 👍

from cmath import isnan
from random import randint

def checkGuessed(table, guess):
    for num in table:
        if num == guess:
            return True
    return False

computerguess = randint(1,10)
guessednumbers = []
guessed = False

while guessed == False:
    answer = input("What's the number: ")

    try:
        if isnan(int(answer)):
            print('Valid Number')
    except Exception:
        print('Not a valid number!')
        continue

    myguess = int(answer)

    if checkGuessed(guessednumbers, myguess) == True:
        print('You already guessed this!')
    elif myguess == computerguess:
        guessed = True
        break
    elif myguess > computerguess:
        guessednumbers.insert(len(guessednumbers)+1,myguess)
        print('Lower')
    elif myguess < computerguess:
        guessednumbers.insert(len(guessednumbers)+1,myguess)
        print("Higher")

print('You guessed the number!!')
