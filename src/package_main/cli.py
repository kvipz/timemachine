import click

@click.command()
def tm():
    click.echo('Hello Time Machine')

if __name__ == "__main__":
    tm()
