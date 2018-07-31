import asekuro
from setuptools import setup, find_packages

setup(
    name='asekuro',
    version=asekuro.__version__,
    description='CLI util to deal with Jupyter Notebooks',
    author=['Vincent D. Warmerdam'],
    entry_points={
        'console_scripts': [
            'asekuro = asekuro.commandline:main',
        ],
    },
    url='https://github.com/godatadriven/asekuro',
    packages=find_packages(),
    install_requires=['pytest==3.7.0',
                      'nbval==0.9.1',
                      'fire==0.1.3',
                      'nbformat==4.4.0',
                      'ipython==6.5.0',
                      'jupyter-client==5.2.3',
                      'jupyter-core==4.4.0']
)
