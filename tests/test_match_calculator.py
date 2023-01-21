import unittest
from match_calculator import MatchCalculator

class TestMatchCalculator(unittest.TestCase):

    def test_read_file(self):
        mc = MatchCalculator()
        file = mc.read("match_test.txt")
        self.assertIsInstance(file, str)

if __name__ == '__main__':
    unittest.main()