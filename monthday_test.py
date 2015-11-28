import datetime

from pytest import fixture, raises

from monthday import MonthDay


@fixture
def feb_29():
    """February 29.  Only available for leap years."""
    return MonthDay(2, 29)


@fixture
def aug_4():
    """August 4.  Author's birthday."""
    return MonthDay(8, 4)


@fixture
def dec_25():
    """December 25.  Christmas."""
    return MonthDay(12, 25)


def test_month_day_from_date(aug_4, dec_25):
    assert MonthDay.from_date(datetime.date(1988, 8, 4)) == aug_4
    assert MonthDay.from_date(datetime.date(2015, 12, 25)) == dec_25
    assert MonthDay.from_date(datetime.datetime(1988, 8, 4)) == aug_4


def test_month_day_from_date_type_error():
    with raises(TypeError):
        MonthDay.from_date('1988-08-04')
    with raises(TypeError):
        MonthDay.from_date(19880804)


def test_month_day_init():
    aug_4 = MonthDay(8, 4)
    assert aug_4.month == 8
    assert aug_4.day == 4


def test_month_day_init_value_error():
    # Invalid months
    with raises(ValueError):
        MonthDay(-12, 1)
    with raises(ValueError):
        MonthDay(-1, 1)
    with raises(ValueError):
        MonthDay(0, 1)
    # Invalid days
    with raises(ValueError):
        MonthDay(1, -31)
    with raises(ValueError):
        MonthDay(1, -1)
    with raises(ValueError):
        MonthDay(1, 0)
    with raises(ValueError):
        MonthDay(1, 32)
    with raises(ValueError):
        MonthDay(2, 30)
    with raises(ValueError):
        MonthDay(2, 31)
    with raises(ValueError):
        MonthDay(3, 32)
    with raises(ValueError):
        MonthDay(4, 31)
    with raises(ValueError):
        MonthDay(5, 32)
    with raises(ValueError):
        MonthDay(6, 31)
    with raises(ValueError):
        MonthDay(7, 32)
    with raises(ValueError):
        MonthDay(8, 32)
    with raises(ValueError):
        MonthDay(9, 31)
    with raises(ValueError):
        MonthDay(10, 32)
    with raises(ValueError):
        MonthDay(11, 31)
    with raises(ValueError):
        MonthDay(12, 32)


def test_month_day_init_type_error():
    with raises(TypeError):
        MonthDay('8', 4)
    with raises(TypeError):
        MonthDay(8.0, 4)
    with raises(TypeError):
        MonthDay(8, '4')
    with raises(TypeError):
        MonthDay(8, 4.0)


def test_month_day_equality(aug_4, dec_25):
    assert aug_4 == MonthDay(8, 4)
    assert not aug_4 != MonthDay(8, 4)
    assert hash(aug_4) == hash(MonthDay(8, 4))
    assert dec_25 == MonthDay(12, 25)
    assert not dec_25 != MonthDay(12, 25)
    assert hash(dec_25) == hash(MonthDay(12, 25))
    assert aug_4 != MonthDay(8, 5)
    assert not aug_4 == MonthDay(8, 5)
    assert hash(aug_4) != hash(MonthDay(8, 5))
    assert aug_4 != dec_25
    assert not aug_4 == dec_25
    assert hash(aug_4) != hash(dec_25)
    assert dec_25 != MonthDay(12, 24)
    assert not dec_25 == MonthDay(12, 24)
    assert hash(dec_25) != hash(MonthDay(12, 24))
    assert dec_25 != aug_4
    assert not dec_25 == aug_4
    assert hash(dec_25) != hash(aug_4)


def test_month_day_date(aug_4, feb_29):
    assert aug_4.date(1988) == datetime.date(1988, 8, 4)
    assert feb_29.date(2016) == datetime.date(2016, 2, 29)
    with raises(ValueError) as excinfo:
        feb_29.date(2015)
    assert str(excinfo.value) == '''since 2015 is not a leap year, monthday.\
MonthDay(2, 29) can't be combined with 2015'''
    with raises(ValueError) as excinfo:
        feb_29.date(2014)
    with raises(ValueError):
        feb_29.date(2013)
    assert feb_29.date(2012) == datetime.date(2012, 2, 29)
    with raises(ValueError):
        feb_29.date(2011)
    with raises(TypeError):
        aug_4.date('1988')


def test_month_day_dates(aug_4, feb_29):
    assert list(aug_4.dates([])) == []
    assert list(aug_4.dates(range(1988, 1992))) == [
        datetime.date(1988, 8, 4),
        datetime.date(1989, 8, 4),
        datetime.date(1990, 8, 4),
        datetime.date(1991, 8, 4),
    ]
    years = range(2010, 2017)
    with raises(ValueError):
        list(feb_29.dates(years))
    with raises(ValueError):
        list(feb_29.dates(years, error_invalid_dates=True))
    assert list(feb_29.dates(years, error_invalid_dates=False)) == [
        datetime.date(2012, 2, 29), datetime.date(2016, 2, 29),
    ]
    assert list(feb_29.dates(years, error_invalid_dates=None)) == [
        None, None, datetime.date(2012, 2, 29),
        None, None, None, datetime.date(2016, 2, 29),
    ]
    with raises(TypeError):
        aug_4.dates(1988)


def test_month_day_str(aug_4, dec_25):
    assert str(aug_4) == '08-04'
    assert str(dec_25) == '12-25'


def test_month_day_repr(aug_4, dec_25):
    assert repr(aug_4) == 'monthday.MonthDay(8, 4)'
    assert repr(dec_25) == 'monthday.MonthDay(12, 25)'
