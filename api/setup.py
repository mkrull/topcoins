from setuptools import setup

dependencies = [
    'requests>=2'
]

test_dependencies = [
    'pytest',
    'pytest-cov',
    'responses'
]

setup(
    name='top-coins-api',
    version='0.0.1',
    author='Matthias Krull',
    author_email='m.krull@uninets.eu',
    description=(
        'List the top crypto coins'
    ),
    install_requires=dependencies,
    extras_require={'test': test_dependencies},
    packages=['topcoins.client', 'topcoins.api'],
    entry_points={
        'console_scripts':[
            'topcoins-api = topcoins.api:run',
            'topcoins-cli = topcoins.client:cli',
        ]
    },
    url='https://github.com/mkrull/topcoins'
)
