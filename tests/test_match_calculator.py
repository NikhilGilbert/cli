import unittest
from match_calculator import MatchCalculator

class TestMatchCalculator(unittest.TestCase):

    def test_read(self):
        mc = MatchCalculator()
        mc.read("tests/matches_diff.txt")
        match_results = mc.get_match_results()
        self.assertEqual(match_results, "1. Lions, 6 pts\n"
                                        "1. Tarantulas, 6 pts\n"
                                        "3. FC Awesome, 1 pts\n"
                                        "3. Grouches, 1 pts\n"
                                        "3. Snakes, 1 pts")
if __name__ == '__main__':
    unittest.main()