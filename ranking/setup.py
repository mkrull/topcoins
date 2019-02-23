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
    name='top-coins-ranking',
    version='0.0.1',
    author='Matthias Krull',
    author_email='m.krull@uninets.eu',
    description=(
        'List the top crypto coins by rank'
    ),
    install_requires=dependencies,
    extras_require={'test': test_dependencies},
    packages=['ranking.client', 'ranking.api'],
    entry_points={
        'console_scripts':[
            'ranking-api = ranking.api:run',
        ]
    },
    url='https://github.com/mkrull/topcoins/ranking'
)
