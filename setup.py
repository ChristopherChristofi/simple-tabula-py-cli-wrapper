from setuptools import setup

setup(
    name='tabula-py-cli-wrapper',
    version='1.0.0',
    py_modules=['tabulapycliwrapper'],
    install_requires=[
        'Click',
        'tabula-py',
    ],
    entry_points={
        'console_scripts': [
            'tabulapycliwrapper = tabulapycliwrapper:cli',
        ],
    },

)
