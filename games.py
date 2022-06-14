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

def tournamentPoints(result):
    if result == VICTORY:
        return 1, -1
    elif result == DEFEAT:
        return -1, 1
    elif result == DRAW:
        return 0, 0

def updateTournamentPoints(player_points, enemy_points, result):
    points1, points2 = tournamentPoints(result) 
    player_points += points1
    enemy_points += points2
    return player_points, enemy_points

def tournament(numbers1, numbers2, number_to_predict):
    player_points = 0
    enemy_points = 0
    
    result = higherNumber(numbers1[0], numbers2[0])
    player_points, enemy_points = updateTournamentPoints(player_points, enemy_points, result)

    result = predictNumber(numbers1[1], numbers2[1], number_to_predict)
    player_points, enemy_points = updateTournamentPoints(player_points, enemy_points, result) 

    result = highestSumOfNumbers(numbers1[2], numbers2[2], numbers1[3], numbers2[3])
    player_points, enemy_points = updateTournamentPoints(player_points, enemy_points, result) 

    return compareResults(player_points, enemy_points)

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
        
    elif game_to_play == 4:
        number1_a = randrange(20)
        number1_b = randrange(20)
        number2_a = randrange(20)
        number2_b = randrange(20) 
        number_to_predict = randrange(20)
        print(tournament(number1_a, number1_b, number2_a, number2_b, number_to_predict))
    
if __name__ == '__main__':
    main()