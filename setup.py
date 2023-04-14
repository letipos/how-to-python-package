from setuptools import setup

setup(
    name='fraud_detection',
    version='0.2',
    packages=['fraud_detection'],
    install_requires=[
        'numpy>=1.20.3',
        'matplotlib>=3.4.2',
        'seaborn>=0.11.1',
        'scikit-learn==1.0'
    ],
    entry_points={
        'console_scripts': [
            'myproject=myproject.__main__:main'
        ]
    },
    author='Leonard Posner',
    author_email='Leonard.Timo.Posner@ibm.com',
    description='This is a sample project to demonstrate python packaging with fraud detection use case',
    license='MIT'
)