from setuptools import setup, find_packages

setup(
    name='Password_strengthener',
    version='0.1',
    description='Check the strength of a password',
    py_modules=['password_strength', 'passwordss'],
    entry_points={
        'console_scripts': ['password_strengthener=password_strengthener:main']
    },
    install_requires=['password_strengthener'],
    
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
