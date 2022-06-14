import unittest

from games import DEFEAT, DRAW, VICTORY, compareResults, higherNumber, predictNumber

class TestGames(unittest.TestCase):
    #TEST COMPARE RESULTS
    def test_compareResults_playerWin(self):
        result1 = 10
        result2 = 5
        self.assertEqual(compareResults(result1, result2), VICTORY)
    
    def test_compareResults_playerLose(self):
        result1 = 5
        result2 = 10
        self.assertEqual(compareResults(result1, result2), DEFEAT)
        
    def test_compareResults_Draw(self):
        result1 = 5
        result2 = 5
        self.assertEqual(compareResults(result1, result2), DRAW)
    
    #TEST HIGH NUMBER            
    def test_highNumber_playerWin(self):
        number1 = 10
        number2 = 5
        self.assertEqual(higherNumber(number1, number2), VICTORY)
    
    def test_highNumber_playerLose(self):
        number1 = 5
        number2 = 10
        self.assertEqual(higherNumber(number1, number2), DEFEAT)
        
    def test_highNumber_Draw(self):
        number1 = 5
        number2 = 5
        self.assertEqual(higherNumber(number1, number2), DRAW)

    #TEST PREDICT NUMBER 
    def test_predictNumber_playerWin(self):
        number1 = 10
        number2 = 5
        number_to_predict = 9
        self.assertEqual(predictNumber(number1, number2, number_to_predict), VICTORY)
    
    def test_predictNumber_playerLose(self):
        number1 = 10
        number2 = 5
        number_to_predict = 6
        self.assertEqual(predictNumber(number1, number2, number_to_predict), DEFEAT)
        
    def test_predictNumber_Draw(self):
        number1 = 6
        number2 = 4
        number_to_predict = 5
        self.assertEqual(predictNumber(number1, number2, number_to_predict), DRAW)
        
if __name__ == "__main__":
    unittest.main()