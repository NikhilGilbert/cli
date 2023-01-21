"""
This class is the central functionality of the Match Calculator cli.
It contains all the logic called by the click tool.
"""

class MatchCalculator:

    match_matrix = {}
    league = None

    def __init__(self, league=""):
        self.league = league

    def read(self, file_path: str):
        """
        This function is used to read in matches stored in a file
        :param file_path: str (path to .txt file containing match results)
        :return: None
        """
        file = open(file_path, "r")
        match_list = []

        for line in file:
            match_list.append(line)

        self.calculate_score(file_input=match_list)

    def line(self, line: str):
        self.calculate_score(line_input=line)
        print(line)

    def calculate_score(self, file_input: list, line_input: str):
        print(file_input)
        print(line_input)


