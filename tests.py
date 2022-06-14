import unittest

from games import DEFEAT, DRAW, VICTORY, compareResults, higherNumber, highestSumOfNumbers, predictNumber

class TestGames(unittest.TestCase):
    #TEST COMPARE RESULTS
    def test_compareResults_playerWin(self):
        self.assertEqual(compareResults(10, 5), VICTORY)
    
    def test_compareResults_playerLose(self):
        self.assertEqual(compareResults(5, 10), DEFEAT)
        
    def test_compareResults_Draw(self):
        self.assertEqual(compareResults(5, 5), DRAW)
    
    #TEST HIGH NUMBER            
    def test_highNumber_playerWin(self):
        self.assertEqual(higherNumber(10, 5), VICTORY)
    
    def test_highNumber_playerLose(self):
        self.assertEqual(higherNumber(5, 10), DEFEAT)
        
    def test_highNumber_Draw(self):
        self.assertEqual(higherNumber(5, 5), DRAW)

    #TEST PREDICT NUMBER 
    def test_predictNumber_playerWin(self):
        self.assertEqual(predictNumber(10, 5, 9), VICTORY)
    
    def test_predictNumber_playerLose(self):
        self.assertEqual(predictNumber(10, 5, 6), DEFEAT)
        
    def test_predictNumber_Draw(self):
        self.assertEqual(predictNumber(6, 4, 5), DRAW)
    
    #TEST HIGHEST SUM OF NUMBERS
    def test_highestSumOfNumbers_playerWin(self):
        self.assertEqual(highestSumOfNumbers(5, 5, 1, 1), VICTORY)
    
    def test_highestSumOfNumbers_playerLose(self):
        self.assertEqual(highestSumOfNumbers(1, 1, 5, 5), DEFEAT)
        
    def test_highestSumOfNumbers_Draw(self):
        self.assertEqual(highestSumOfNumbers(5, 5, 5, 5), DRAW)
        
if __name__ == "__main__":
    unittest.main()