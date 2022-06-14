import unittest

from games import DEFEAT, DRAW, VICTORY, higherNumber

class TestGames(unittest.TestCase):       
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

if __name__ == "__main__":
    unittest.main()