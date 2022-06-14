import unittest

from games import DEFEAT, DRAW, VICTORY, compareResults, higherNumber, highestSumOfNumbers, predictNumber, tournament, tournamentPoints, updateTournamentPoints

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
        
    #TEST TOURNAMENT POINTS
    def test_tournamentPoints_playerWin(self):
        self.assertEqual(tournamentPoints(VICTORY), (1, -1))
    
    def test_tournamentPoints_playerLose(self):
        self.assertEqual(tournamentPoints(DEFEAT), (-1, 1))
        
    def test_tournamentPoints_Draw(self):
        self.assertEqual(tournamentPoints(DRAW), (0, 0))
        
    #TEST UPDATE TOURNAMENT POINTS
    def test_updateTournamentPoints(self):
        self.assertEqual(updateTournamentPoints(1, 2, VICTORY), (2, 1))
        
    #TEST TOURNAMENT
    def test_tournament_playerWin(self):
        numbers1 = [10, 10, 5, 5]
        numbers2 = [9, 5, 2, 2]
        self.assertEqual(tournament(numbers1, numbers2, 9), VICTORY)
    
    def test_tournament_playerLose(self):
        numbers1 = [1, 10, 3, 3]
        numbers2 = [9, 5, 8, 2]
        self.assertEqual(tournament(numbers1, numbers2, 1), DEFEAT)
        
    def test_tournament_Draw(self):
        numbers1 = [1, 10, 4, 4]
        numbers2 = [9, 5, 4, 4]
        self.assertEqual(tournament(numbers1, numbers2, 9), DRAW)
        
if __name__ == "__main__":
    unittest.main()