from random import randrange

VICTORY = 2
DEFEAT = 1
DRAW = 0

def higherNumber():
    number1 = randrange(20)
    number2 = randrange(20)
    if number1 > number2:
        return VICTORY
    elif number1 < number2:
        return DEFEAT
    else:
        return DRAW

def main():
    game_to_play = int(input())
    if game_to_play == 1:
        higherNumber() 
    
if __name__ == '__main__':
    main()