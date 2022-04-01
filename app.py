import click

@click.command()
@click.option('--count', prompt='Greeting times', default=1, help='Number of greetings. Default value for count is 1')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()