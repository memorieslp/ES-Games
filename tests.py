import unittest

from games import VICTORY, higherNumber

class TestGames(unittest.TestCase):       
    def test_highNumber(self):
        number1 = 10
        number2 = 5
        self.assertEqual(higherNumber(number1, number2), VICTORY)

if __name__ == "__main__":
    unittest.main()