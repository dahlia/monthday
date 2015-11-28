``monthday``
============

This package provides the ``MonthDay`` value type for dealing dates without
year.  It is useful for dealing with birthdays, or anniversaries.

.. code-block:: pycon

   >>> from monthday import *
   >>> aug_4 = MonthDay(8, 4)
   >>> aug_4
   monthday.MonthDay(8, 4)
   >>> aug_4.date(1988)
   datetime.date(1988, 8, 4)
   >>> from datetime import date
   >>> MonthDay.from_date(date(2015, 12, 25))
   monthday.MonthDay(12, 25)

Written by `Hong Minhee`__, and distributed under LGPLv3_ or later.

__ http://hongminhee.org/
.. _LGPLv3: http://www.gnu.org/licenses/lgpl-3.0.html
