from random import randrange

VICTORY = 2
DEFEAT = 1
DRAW = 0

def compareResults(result1, result2):
    if result1 > result2:
        return VICTORY
    elif result1 < result2:
        return DEFEAT
    else:
        return DRAW

def higherNumber(number1, number2):
    return compareResults(number1, number2)

def predictNumber(number1, number2, number_to_predict):
    result1 = abs(number1 - number_to_predict)
    resunt2 = abs(number2 - number_to_predict)
    return compareResults(resunt2, result1) 

def main():
    game_to_play = int(input())
    if game_to_play == 1:
        number1 = randrange(20)
        number2 = randrange(20)
        print(higherNumber(number1, number2))
    
if __name__ == '__main__':
    main()