from setuptools import setup

setup(
	name='janitor',
	version='0.1',
	description='Clean your disk drives with ease',
	url='http://github.com/vedantrathore/janitor',
	author='Vedant Rathore',
	author_email='vedantr1998@gmail.com',
	license='MIT',
	zip_safe=False,
	install_requires=[
		'Click'
	],
	entry_points={
		'console_scripts':['janitor=src.cli:hello']
	}
)