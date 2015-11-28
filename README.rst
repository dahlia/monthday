monthday
========

.. image:: https://badge.fury.io/py/monthday.svg
   :alt: PyPI
   :target: https://pypi.python.org/pypi/monthday

.. image:: https://readthedocs.org/projects/monthday/badge/
   :alt: Read the Docs
   :target: https://monthday.readthedocs.org/

.. image:: https://travis-ci.org/dahlia/monthday.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/dahlia/monthday

.. image:: https://codecov.io/github/dahlia/monthday/coverage.svg?branch=master
   :alt: Coverage Status
   :target: https://codecov.io/github/dahlia/monthday?branch=master

This package provides the ``MonthDay`` value type for dealing dates without
year.  It is useful for dealing with birthdays, or anniversaries.
Works on Python 2.6, 2.7, 3.2--3.5, PyPy, PyPy3.

.. code-block:: pycon

   >>> from monthday import *
   >>> aug_4 = MonthDay(8, 4)
   >>> aug_4
   monthday.MonthDay(8, 4)
   >>> aug_4.date(1988)
   datetime.date(1988, 8, 4)
   >>> list(aug_4.dates(range(2013, 2016)))
   [datetime.date(2013, 8, 4),
    datetime.date(2014, 8, 4),
    datetime.date(2015, 8, 4)]
   >>> from datetime import date
   >>> MonthDay.from_date(date(2015, 12, 25))
   monthday.MonthDay(12, 25)

It's available on PyPI__:

.. code-block:: console

   $ pip install monthday

Written by `Hong Minhee`__, and distributed under LGPLv3_ or later.
Find the source code from the `GitHub repository`__.

__ https://pypi.python.org/pypi/monthday
__ http://hongminhee.org/
.. _LGPLv3: http://www.gnu.org/licenses/lgpl-3.0.html
__ https://github.com/dahlia/monthday
