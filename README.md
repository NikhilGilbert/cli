
### Match CLI Tool

#### Description

This is a command line interface for calculating team rankings in a sports league.

#### Setup

You can install this in one of two ways:
<ol>
<li>In a virtual environment using pip: (Any env with pip installed) <br>
   <code>pip install -i https://test.pypi.org/simple/ match-tool-by-nikhilgilbertv2</code> </li>
<li>From source: (Recommend using linux) <br>
    <code>git clone https://github.com/NikhilGilbert/cli.git</code> and 
    run <code>python setup.py develop</code></li>
</ol>
   
#### Usage

Please confirm installation by calling the command `match`. <br>
You can use this tool in one of two ways:
<ol>
<li>By parsing a <code>.txt</code> file: <code>match file -p match_results.txt</code>
   Please see <a href="https://github.com/NikhilGilbert/cli/blob/master/tests/matches_original.txt">example</a> </li>
<li>By inputing the results line by line: Call <code>match line</code> from the command line <br>
   Input the match result when prompted using the format: <br>
    <code>team_1:str score:int, team_2:str score:int</code></li>
</ol>

#### Tests

Run the following command for unit tests if you installed from source: <br>
From source folder: <code>python -m unittest tests.test_match_calculator.TestMatchCalculator.test_read</code>
