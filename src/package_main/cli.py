import click

@click.command()
def tc():
    click.echo('Hello Time Machine')

if __name__ == "__main__":
    tc()
