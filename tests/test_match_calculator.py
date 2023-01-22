import unittest
from match_calculator import MatchCalculator

class TestMatchCalculator(unittest.TestCase):

    def test_calculate_score(self):
        mc = MatchCalculator()
        mc.read("match_test.txt")
        match_results = mc.get_match_results()
        self.assertEqual(match_results, "")

if __name__ == '__main__':
    unittest.main()