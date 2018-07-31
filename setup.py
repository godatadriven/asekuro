from setuptools import setup, find_packages

setup(
    name='asekuro',
    version='0.0.2',
    entry_points={
        'console_scripts': [
            'asekuro = asekuro.commandline:main',
        ],
    },
    packages=find_packages(),
    install_requires=['pytest==3.7.0',
                      'nbval==0.9.1',
                      'fire==0.1.3',
                      'nbformat==4.4.0',
                      'ipython==6.5.0',
                      'jupyter-client==5.2.3',
                      'jupyter-core==4.4.0']
)
