import click
from janitor import Janitor
from hurry.filesize import size
import click_spinner

@click.group()
def main():
	pass

@main.command()
@click.option('--length', '-l',  default=10, help="The number of files you want to see after analysis")
@click.argument('path', type=click.Path(), default=".")
def analyse(path, length):
	click.clear()
	click.secho('Your top {0} files occupying the most disk space are: '.format(length), fg='white')
	click.secho('Name'.ljust(30) + 'Size'.ljust(15) + 'Path'.ljust(40) + 'Extension'.ljust(10), fg='white', bold=True)
	cleaner = Janitor(path)
	with click_spinner.spinner():
		files = cleaner.analyse()
	for index, file in enumerate(files):
		if index > length:
			break
		if len(file['name']) > 28:
			name = file['name'][:20] + '...'
		else:
			name = file['name']
		if len(file['path']) > 35:
			path = file['path'][:32] + '...'
		else:
			path = file['path']
		click.secho(name.ljust(30) + str(size(file['size'])).ljust(15) + path.ljust(40) + file['extension'].ljust(10))
