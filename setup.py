from setuptools import setup

setup(
    name='tabula-py-cli-wrapper',
    version='1.0.0',
    py_modules=['tabulapycliwrapper', 'log'],
    install_requires=[
        'Click',
        'tabula-py',
    ],
    entry_points={
        'console_scripts': [
            'tabulapycli = tabulapycliwrapper:cli',
        ],
    },

)
