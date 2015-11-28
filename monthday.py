""":mod:`monthday` --- Date without year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import datetime
import numbers


__all__ = 'MonthDay', '__version__'
__version__ = '0.9.0'


class MonthDay(object):
    """Date without year.  Useful for birthdays, or anniversaries.

    :param month: a month number, from 1 to 12
    :type month: :class:`numbers.Integral`
    :param day: a day of the ``month``, from 1 to 31 (or 30, or 29)
    :type day: :class:`numbers.Integral`
    :raise ValueError: if ``month`` or ``date`` is out of valid range

    .. attribute:: month

       (:class:`numbers.Integral`) The month number, from 1 to 12.

    .. attribute:: day

       (:class:`numbers.Integral`) The day of the ``month``, from 1 to 31.

    """

    @classmethod
    def from_date(cls, date):
        """Get only :class:`MonthDay` from the given ``date``.

        :param date: the date or date/time
        :type date: :class:`datetime.date`, :class:`datetime.datetime`
        :return: :class:`MonthDay` without ``date``'s
                 :attr:`~datetime.date.year`
        :rtype: :class:`MonthDay`

        """
        if isinstance(date, datetime.date):
            return cls(date.month, date.day)
        raise TypeError('date must be an instance of datetime.date, not ' +
                        repr(date))

    def __init__(self, month, day):
        if not isinstance(month, numbers.Integral):
            raise TypeError('month must be an integer, not ' + repr(month))
        elif not isinstance(day, numbers.Integral):
            raise TypeError('day must be an integer, not ' + repr(day))
        elif not 1 <= month <= 12:
            raise ValueError('month must be from 1 to 12, not ' + repr(month))
        elif month in (1, 3, 5, 7, 8, 10, 12) and not 1 <= day <= 31:
            raise ValueError('day must be from 1 to 31 for month={!r}, but '
                             '{!r} was given'.format(month, day))
        elif month in (2, 4, 6, 9, 11) and not 1 <= day <= 30:
            raise ValueError('day must be from 1 to 30 for month={!r}, but '
                             '{!r} was given'.format(month, day))
        elif month == 2 and not 1 <= day <= 29:
            raise ValueError('day must be from 1 to 29 for month=2, but '
                             '{!r} was given'.format(day))
        self.month = int(month)
        self.day = int(day)

    def __eq__(self, other):
        return (isinstance(other, type(self)) and
                self.month == other.month and
                self.day == other.day)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return self.month * 100 + self.day

    def date(self, year):
        """Get a :class:`~datetime.date` by combining the given ``year``
        with it.

        :param year: a year to combine with
        :type year: :class:`numbers.Integral`
        :return: a :class:`datetime.date` with the given ``year``
        :rtype: :class:`datetime.date`
        :raise ValueError: when ``year`` is not a leap year
                           while it's ``MonthDay(2, 29)``

        """
        return datetime.date(year, self.month, self.day)

    def __str__(self):
        return '{0:02d}-{1:02d}'.format(self.month, self.day)

    def __repr__(self):
        return '{0.__module__}.{0.__name__}({1!r}, {2!r})'.format(
            type(self), self.month, self.day
        )
