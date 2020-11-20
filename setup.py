import os

from setuptools import find_packages, setup

pjoin = os.path.join

here = os.path.abspath(os.path.dirname(__file__))

# Version
ns = {}
with open(pjoin(here, 'botiper', 'version.py')) as f:
    exec(f.read(), {}, ns)

dependencies = []
if os.path.isfile("requirements.txt"):
    with open("requirements.txt") as f:
        for l in f.readlines():
            dependencies.append(l)


def setup_package():
    metadata = dict(
        name='botiper',
        packages=find_packages(),
        description="""Telegram bot that will responde the ip of the server where is running.""",
        install_requires=dependencies,
        author="selrach",
        platforms="Linux",
        version=ns['__version__'],
        keywords=['Interactive', 'Interpreter', 'Shell', 'Web'],
        classifiers=['Programming Language :: Python :: 3'],
        entry_points={
            'console_scripts': [
                'botiper = botiper.botiper:up'
            ]
        }
    )

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
