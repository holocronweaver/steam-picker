from setuptools import setup

setup(
    name='steam-picker',
    version='0.1.3',
    author='Jesse Johnson',
    author_email='holocronweaver@gmail.com',
    packages=['steampicker'],
    scripts=['bin/steam-picker.py', 'bin/steam-picker'],
    include_package_data=True,
    # url='http://pypi.python.org/pypi/MyApplication_v010/',
    license='LICENSE.txt',
    description='A Python 3 CLI for picking a random game from your Steam library!',
    # long_description=open('README.org').read(),
    # Dependent packages (distributions)
    install_requires=[
        'appdirs',
        'pyyaml',
        'requests',
        'steam',
    ],
)
