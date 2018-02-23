from setuptools import setup

setup(name="flaskplatform",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="chenshen",
      author_email="chen.shen@ucdconnect.ie",
      licence="GPL3",
      packages=['flaskp'],
      include_package_data=True,
      zip_safe = False,
      classifiers=[
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
      ],
      entry_points={
          'console_scripts':['flaskplatform=flaskp.main:main']
          }
      )
