try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A project to analyze documents.',
    'author': 'John Doherty',
    'url': 'github.com/not-a-bot',
    #'download_url': 'Where to download it.',
    'version': '0.1',
    'install_requires': ['nose'],
    #folder named NAME in the basic folder
	'packages': ['ANALYZE'],
    'name': 'Analyze Documents'

}

setup(**config)
