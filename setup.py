import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.RST')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.RST')) as f:
    CHANGES = f.read()

requires = [
    'pelican'
    ]

setup(name='pelican_page_order',
      version='0.1.0',
      description='Page order plugin for pelican',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        ],
      author='Mark Hall',
      author_email='mark.hall@work.room3b.eu',
      url='',
      keywords='pelican page order',
      py_modules=['pelican_page_order'],
      install_requires=requires,
      )
