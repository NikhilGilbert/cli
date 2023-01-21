import click
from match_calculator import MatchCalculator as mc

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
        results = mc.calculate(file)
        click.echo(results)
    except:
        click.echo("No file with that name.")


@cli.command()
@click.option('-n', '--name', type=str, help='One match result', default=None)
def string(name):
    click.echo(f'Hello {name}')