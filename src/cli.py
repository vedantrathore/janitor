import os
import click
import logging
import click_spinner
import click_log
from janitor import Janitor
from hurry.filesize import size


logger = logging.getLogger(__name__)
click_log.basic_config(logger)

@click.group()
def main():
	"""	A simple command line tool to clean and analyse your file system """
	pass

@main.command()
@click.option('--length', '-l',  default=10, help="The number of files you want to see after analysis")
@click.option('--sort', '-s', default='size', help="The field you want to sort the results with")
@click.argument('path', type=click.Path(exists=True), default=".")
@click_log.simple_verbosity_option(logger)
def analyse(path, length, sort):
	""" Analyse the directory """
	click.clear()
	click.secho('Your top {0} files occupying the most disk space are: '.format(length), fg='white')
	click.secho('Name'.ljust(30) + 'Size'.ljust(15) + 'Path'.ljust(40) + 'Extension'.ljust(10), fg='white', bold=True)
	cleaner = Janitor(path)
	with click_spinner.spinner():
		files = cleaner.analyse()
	files = sorted(files, key=lambda k:k[sort], reverse=(True if sort == 'size' else False))
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


@main.command()
@click.option('--out_dir','-od', type=click.Path(exists=True), default='~/Documents/Janitor', help="The path to directory where you want to save your cleaned files")
@click.option('--in_dir','-id', type=click.Path(exists=True), default='.', help="The directory you wish to clean")
def clean(out_dir, in_dir):
	""" Clean your unwanted files to a secure location"""
	files = [f for f in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, f))]
	click.secho('The following files will be moved from {0} to {1}: '.format(in_dir, out_dir),fg='white')
	for file in files:
		click.secho(file, fg='white')
	if click.confirm('Are you sure you want to continue?', abort=True):
		cleaner = Janitor(in_dir)
		cleaner.clean(out_dir)
		click.secho('Done!', fg='white', bold=True)