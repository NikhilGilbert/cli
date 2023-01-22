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
    def get_match_results(self) -> str: Get formatted match results
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

        file.close()

    def line(self, line: str):
        """
        This function is called in the cli when someone passes and input through the cmd line
        :param line: A string input that
        """
        self._calculate(line_input=line)

    def _calculate_match_result(self, result: str):
        """
        Core logic of match result calculations
        :param result: the string results containing the match score
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

    def _sort_match_table(self) -> list:
        """
        Return a list of team tuples sorted by their score then name
        :return: list that is a sorted version of match table
        """
        sorted_match_table = sorted(self._match_table.items(), key=lambda kv: (-kv[1], kv[0]))

        return sorted_match_table


    def get_match_results(self) -> str:
        """
        This file takes the match_table dict and orders the team based on performance,
        then alphabetically and displays it in the form of a string
        :return: String formatted to contain the correct match table score output
        """
        sorted_match_table = self._sort_match_table()
        position_count = 0
        carry = 1
        current_score = -1
        match_results = ""

        for i in range(len(sorted_match_table)):
            if current_score != sorted_match_table[i][1]:
                current_score = sorted_match_table[i][1]
                position_count += carry
                carry = 0
            if i+1 == len(sorted_match_table):
                match_results += f'{position_count}. {sorted_match_table[i][0]}, {sorted_match_table[i][1]} pts'
            else:
                match_results += f'{position_count}. {sorted_match_table[i][0]}, {sorted_match_table[i][1]} pts\n'
                carry += 1

        return match_results
