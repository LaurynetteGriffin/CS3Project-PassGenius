from setuptools import setup

setup(
    name='password_strength',
    version='0.1',
    description='Check the strength of a password',
    py_modules=['password_strength', 'passwords'],
    entry_points={
        'console_scripts': ['password_strength=password_strength:password_strength']
    },
    install_requires=['password_strength'],
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
