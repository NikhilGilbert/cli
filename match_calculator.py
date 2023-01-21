"""
This class is the central functionality of the Match Calculator cli.
It contains all the logic called by the click tool.
"""

"""
print(sorted(key_value.items(), key=lambda kv:
                 (kv[1], kv[0])))
"""

class MatchCalculator:
    """
    
    """
    match_table = {}
    league = None

    def __init__(self, league=""):
        """

        :param league:
        """
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

        self.calculate(file_input=match_list)

    def line(self, line: str):
        """

        :param line:
        :return:
        """
        self.calculate(line_input=line)

    def calculate_match_result(self, result: str):
        """

        :param result:
        :return:
        """
        in_scores = result.split(",")

        team_one_name = in_scores[0][0:-2]
        team_two_name = in_scores[1][0:-2]

        if team_one_name not in self.match_table.keys():
            self.match_table[team_one_name] = 0

        if team_two_name not in self.match_table.keys():
            self.match_table[team_two_name] = 0

        team_one_score = int(in_scores[0][:-1])
        team_two_score = int(in_scores[1][:-1])

        if team_one_score > team_two_score:
            self.match_table[team_one_name] += 3
        elif team_one_score < team_two_score:
            self.match_table[team_two_name] += 3
        else:
            self.match_table[team_one_name] += 1
            self.match_table[team_two_name] += 1

    def calculate(self, file_input: list, line_input: str):
        """

        :param file_input:
        :param line_input:
        :return:
        """
        if file_input:
            for match in file_input:
                self.calculate_match_result(match)
        else:
            self.calculate_match_result(line_input)

    def get_match_results(self) -> str:
        """

        :return:
        """
        for key in self.match_table.keys():
            self.match_table[key]
        return {}
