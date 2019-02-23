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
    name='top-coins-pricing',
    version='0.0.1',
    author='Matthias Krull',
    author_email='m.krull@uninets.eu',
    description=(
        'Get the current price of crypto currencies'
    ),
    install_requires=dependencies,
    extras_require={'test': test_dependencies},
    packages=['pricing.client', 'pricing.api'],
    entry_points={
        'console_scripts':[
            'pricing-api = pricing.api:run',
            'pricing-cli = pricing.client:cli',
        ]
    },
    url='https://github.com/mkrull/topcoins/pricing'
)
