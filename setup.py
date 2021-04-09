from setuptools import setup

setup(
    name='runt',
    version='0.1',
    description='Python task runner triggered by api calls',
    url='http://github.com/james-burgess/runt',
    author='james-burgess',
    author_email='dev@jimmyb.co.za',
    license='MIT',
    packages=['runt'],
    install_requires=[
        'flask',
        'flask-httpauth',
    ],    
    scripts=['bin/runt'],
    zip_safe=False
)
