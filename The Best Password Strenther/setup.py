from setuptools import setup, find_packages

setup(
    name='The_Best_password_strength',
    version='0.1',
    description='Check the strength of a password',
    py_modules=['password_strength', 'passwordss'],
    entry_points={
        'console_scripts': ['password_strength=password_strength:main']
    },
    install_requires=['password_strength'],
    
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
