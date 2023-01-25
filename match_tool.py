import click
from match_calculator import MatchCalculator
from tests.test_match_calculator import TestMatchCalculator as tmc

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--path', type=str, help='Path to match results file', default=None)
def file(path):
    if path is None:
        click.echo("matchcalc Error: Please input a file path with your match results.")
        click.echo(f"Path {path} is not a valid path.")

    try:
        file = open(path, "r")
        mc = MatchCalculator()
        mc.read(file)
        results = mc.get_match_results()
        click.echo(results)
        file.close()
    except:
        click.echo("No file with that name.")

@cli.command()
@click.option(help='One match result passed in as a cmd line input')
def line():
    mc = MatchCalculator()
    mc.line()
    results = mc.get_match_results()
    click.echo(results)

@cli.command()
@click.option('-r', '--run', type=str, help='Run tests for all functions',
              default='run')
def test(run):
    tmc.run()
