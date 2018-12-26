from setuptools import setup, find_packages


setup(
    name='nasalatlon',
    version='1.0',
    install_requires=[
        'requests'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
