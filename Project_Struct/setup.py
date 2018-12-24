try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = [
            'Project':'My Project',
            'Author': 'My Name',
            'url': 'url to get the project',
            'download_url': 'Where to download the project',
            'author_mail':'My email',
            'version': 'v0.1',
            'install_requires': ['node'],
            'packages':'NAME',
            'scripts': [],
            'name':'projectname'
            ]

    setup(**config)

