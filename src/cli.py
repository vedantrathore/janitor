import click

@click.command()
@click.option('--text', default="World", help="The greeting you want to see")
def hello(text):
  print "Hello {0}!".format(text)