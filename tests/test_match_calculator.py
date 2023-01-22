import unittest
from match_calculator import MatchCalculator

class TestRead(unittest.TestCase):

    def test_read(self):
        mc = MatchCalculator(league="one")
        mc.read("match_test_rev.txt")
        match_results = mc.get_match_results()
        self.assertEqual(match_results, "1. Lions, 6 pts\n"
                                        "1. Tarantulas, 6 pts\n"
                                        "3. FC Awesome, 1 pts\n"
                                        "3. Grouches, 1 pts\n"
                                        "3. Snakes, 1 pts")

    def test_line(self):
        mc = MatchCalculator()
        mc.line("Lions 3, Snakes 3")
        mc.line("Tarantulas 1, FC Awesome 0")
        mc.line("Lions 1, FC Awesome 1")
        mc.line("Tarantulas 3, Snakes 1")
        mc.line("Lions 4, Grouches 0")
        match_results = mc.get_match_results()
        self.assertEqual(match_results, "1. Tarantulas, 6 pts\n"
                                        "2. Lions, 5 pts\n"
                                        "3. FC Awesome, 1 pts\n"
                                        "3. Snakes, 1 pts\n"
                                        "5. Grouches, 0 pts")

if __name__ == '__main__':
    unittest.main()