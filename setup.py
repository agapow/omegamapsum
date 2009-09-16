from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='omegamapsum',
      version=version,
      description="Routines to summarize ana analyse Omegamap output",
      long_description="""\
`omegaMap <http://www.danielwilson.me.uk/software.html>`__ is an excellent program for detecting selection and recombination within molecular biosequences. However the output can be formidably large and thus difficult to analyse. The software includes R code for doing this, but in turn the memory demands can be formidable. This package duplicates the functionality oof that code for analysing and summarising omegaMap output, hopefully acheiving it in a more conservative amount of memory and opening the results to visualisation by many Python packages.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='omegamap mcmc molecular analysis selection',
      author='Paul-Michael Agapow & Samit Kundu',
      author_email='agapow@bbsrc.ac.uk',
      url='http://www.agapow.net/software/omegamapsum',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
