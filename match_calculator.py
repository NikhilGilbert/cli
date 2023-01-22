"""
This class is the core functionality of the Match Calculator cli.
"""

class MatchCalculator:
    """
    Match Calculator contains all the logic called by the click tool.

    def __init__(self, league=""): Declare a league name (Optional)
    def read(self, file_path: str): Read in multiple match results using a file
    def line(self, line: str): Read in a single match result using cmd line input
    def _calculate_match_result(self, result: str): Method that performs scoring logic
    def _calculate(self, file_input: list, line_input: str): Calls _calculate_match_result for both line and file input
    def get_match_results(self) -> str:
    """

    _match_table = {}
    league = None

    def __init__(self, league="generic"):
        """
        Initialise Match Calculator class
        :param league: The name of the league
        """
        self.league = league

    def read(self, file_path: str):
        """
        This function is used to read in matches stored in a file
        :param file_path: str (path to .txt file containing match results)
        """
        file = open(file_path, "r")
        match_list = []

        for line in file:
            match_list.append(line)

        self._calculate(file_input=match_list)

    def line(self, line: str):
        """
        This function is called in the cli when someone passes and input through the cmd line
        :param line: A string input that
        """
        self._calculate(line_input=line)

    def _calculate_match_result(self, result: str):
        """

        :param result:
        :return:
        """
        in_scores = result.strip().split(",")

        team_one_name = in_scores[0][0:-2]
        team_two_name = in_scores[1][1:-2]

        if team_one_name not in self._match_table.keys():
            self._match_table[team_one_name] = 0

        if team_two_name not in self._match_table.keys():
            self._match_table[team_two_name] = 0

        team_one_score = int(in_scores[0][-1])
        team_two_score = int(in_scores[1][-1])

        if team_one_score > team_two_score:
            self._match_table[team_one_name] += 3
        elif team_one_score < team_two_score:
            self._match_table[team_two_name] += 3
        else:
            self._match_table[team_one_name] += 1
            self._match_table[team_two_name] += 1

    def _calculate(self, file_input=[], line_input=""):
        """
        This function process the input and passes it to the score calculation logic
        :param file_input: Input that is a list of matches drawn from a file
        :param line_input: cmd line input
        :return:
        """
        if file_input:
            for match in file_input:
                self._calculate_match_result(match)
        else:
            self._calculate_match_result(line_input)

    def get_match_results(self) -> str:
        """
        This file takes the match_table dict and orders the team based on performance,
        then alphabetically and displays it in the form of a string
        :return: String formatted to contain the correct match table score output
        """
        sorted_match_table = sorted(self._match_table.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
        position_count = 1
        match_results = ""
        print(sorted_match_table)
        # for key in sorted_match_table.keys():
        #     match_results += f'{position_count}. {key}, {self.match_table[key]} pts + \n'

        return match_results
