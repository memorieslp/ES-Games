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
    result2 = abs(number2 - number_to_predict)
    return compareResults(result2, result1) 

def highestSumOfNumbers(number1_a, number1_b, number2_a, number2_b):
    result1 = number1_a + number1_b
    result2 = number2_a + number2_b
    return compareResults(result1, result2) 

def main():
    game_to_play = int(input())
    if game_to_play == 1:
        number1 = randrange(20)
        number2 = randrange(20)
        print(higherNumber(number1, number2))
        
    elif game_to_play == 2:
        number1 = randrange(20)
        number2 = randrange(20)
        number_to_predict = randrange(20)
        print(predictNumber(number1, number2, number_to_predict))
    
    elif game_to_play == 3:
        number1_a = randrange(20)
        number1_b = randrange(20)
        number2_a = randrange(20)
        number2_b = randrange(20) 
        print(highestSumOfNumbers(number1_a, number1_b, number2_a, number2_b))
    
if __name__ == '__main__':
    main()