import click
from match_calculator import MatchCalculator

@click.group()
def cli():
    pass

@cli.command()
@click.option('-p', '--path', type=str, help='Input path to match results file')
def file(path):
    if path is None:
        click.echo("matchcalc Error: Please input a file path with your match results.")
        click.echo(f"Path {path} is not a valid path.")

    try:
        mc = MatchCalculator()
        mc.read(path)
        results = mc.get_match_results()
        click.echo(results)
    except Exception as e:
        click.echo(e)
        click.echo("Please enter valid file path!")

@cli.command()
@click.option('--option', help='Input a series of match results line by line')
def line(option):
    mc = MatchCalculator()
    mc.line()
    results = mc.get_match_results()
    click.echo(results)
