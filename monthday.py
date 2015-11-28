""":mod:`monthday` --- Date without year
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import collections
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

    __slots__ = 'month', 'day'

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

        >>> MonthDay(12, 25).date(2015)
        datetime.date(2015, 12, 25)

        It may raise :exc:`ValueError` if February 29 is tried to be combined
        with a non-leap year e.g.:

        >>> feb_29 = MonthDay(2, 29)
        >>> feb_29.date(2012)
        datetime.date(2012, 2, 29)
        >>> feb_29.date(2013)
        Traceback (most recent call last):
          ...
        ValueError: since 2013 is not a leap year,
                    monthday.MonthDay(2, 29) can't be combined with 2013

        :param year: a year to combine with
        :type year: :class:`numbers.Integral`
        :return: a :class:`datetime.date` with the given ``year``
        :rtype: :class:`datetime.date`
        :raise ValueError: when ``year`` is not a leap year
                           while it's ``MonthDay(2, 29)``

        """
        if not isinstance(year, numbers.Integral):
            raise TypeError('year must be an integer, not ' + repr(year))
        try:
            return datetime.date(int(year), self.month, self.day)
        except ValueError:
            if self.month == 2 and self.day == 29:
                raise ValueError("since {0!r} is not a leap year, {1!r} can't "
                                 "be combined with {0!r}".format(year, self))
            raise

    def dates(self, years, error_invalid_dates=True):
        """Get :class:`~datetime.date`\ s by combining the given ``years``
        with it.

        >>> list(MonthDay(8, 4).dates(range(1988, 1992)))
        [datetime.date(1988, 8, 4), datetime.date(1989, 8, 4),
         datetime.date(1990, 8, 4), datetime.date(1991, 8, 4)]

        It may raise :exc:`ValueError` if there happen to be any invalid
        dates in the result, e.g. Feburary 29 for non-leap years:

        >>> feb_29 = MonthDay(2, 29)
        >>> list(feb_29.dates(range(2011, 2017)))
        Traceback (most recent call last):
          ...
        ValueError: since 2010 is not a leap year,
                    monthday.MonthDay(2, 29) can't be combined with 2010

        If you want to simply ignore these invalid dates in the result,
        set ``error_invalid_dates`` to :const:`False` e.g.:

        >>> list(feb_29.dates(range(2011, 2017), error_invalid_dates=False))
        [datetime.date(2012, 2, 29), datetime.date(2016, 2, 29)]

        But the result length might be shorter than the input ``years`` list.

        If you want to match the length of the input and the result, set
        ``error_invalid_dates`` to :const:`None` --- it will replace invalid
        dates in the result with :const:`None` values e.g.:

        >>> list(feb_29.dates(range(2011, 2017), error_invalid_dates=None))
        [None, datetime.date(2012, 2, 29),
         None, None, None, datetime.date(2016, 2, 29)]

        :param years: years to combine with
        :type years: :class:`~collections.abc.Iterable`
        :param error_invalid_dates: if set to :const:`True`, raise
                                    :exc:`ValueError` for invalid dates.
                                    if set to :const:`False`, just ignore
                                    invalid dates --- the result length might
                                    be shorter than the input ``years`` list.
                                    if set to :const:`None`, fill :const:`None`
                                    values instead of invalid dates --- the
                                    result length must be the same to the input
                                    ``year`` list.  :const:`True` by default
        :type error_invalid_dates: :class:`bool`, ``type(None)``
        :return: :class:`datetime.date` values with the given ``years``.
                 the order corresponds to the input ``years``' order
        :rtype: :class:`~collections.abc.Iterable`
        :raise ValueError: if ``error_invalid_dates`` is set to :const:`True`
                           and there happend to be any invalid dates in
                           the result
        :raise TypeError: if ``years`` is not iterable of integers

        """
        if not isinstance(years, collections.Iterable):
            raise TypeError('years must be iterable, not ' + repr(years))

        def generate():
            for year in years:
                try:
                    yield self.date(year)
                except ValueError:
                    if error_invalid_dates:
                        raise
                    elif error_invalid_dates is None:
                        yield None
        return generate()

    def __getstate__(self):
        return self.month, self.day

    def __setstate__(self, state):
        self.month, self.day = state

    def __str__(self):
        return '{0:02d}-{1:02d}'.format(self.month, self.day)

    def __repr__(self):
        return '{0.__module__}.{0.__name__}({1!r}, {2!r})'.format(
            type(self), self.month, self.day
        )
