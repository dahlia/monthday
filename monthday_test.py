import datetime

from pytest import raises

from monthday import MonthDay


def test_month_day_from_date():
    assert MonthDay.from_date(datetime.date(1988, 8, 4)) == MonthDay(8, 4)
    assert MonthDay.from_date(datetime.date(2015, 12, 25)) == MonthDay(12, 25)
    assert MonthDay.from_date(datetime.datetime(1988, 8, 4)) == MonthDay(8, 4)


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


def test_month_day_equality():
    assert MonthDay(8, 4) == MonthDay(8, 4)
    assert not MonthDay(8, 4) != MonthDay(8, 4)
    assert hash(MonthDay(8, 4)) == hash(MonthDay(8, 4))
    assert MonthDay(12, 25) == MonthDay(12, 25)
    assert not MonthDay(12, 25) != MonthDay(12, 25)
    assert hash(MonthDay(12, 25)) == hash(MonthDay(12, 25))
    assert MonthDay(8, 4) != MonthDay(8, 5)
    assert not MonthDay(8, 4) == MonthDay(8, 5)
    assert hash(MonthDay(8, 4)) != hash(MonthDay(8, 5))
    assert MonthDay(8, 4) != MonthDay(12, 25)
    assert not MonthDay(8, 4) == MonthDay(12, 25)
    assert hash(MonthDay(8, 4)) != hash(MonthDay(12, 25))
    assert MonthDay(12, 25) != MonthDay(12, 24)
    assert not MonthDay(12, 25) == MonthDay(12, 24)
    assert hash(MonthDay(12, 25)) != hash(MonthDay(12, 24))
    assert MonthDay(12, 25) != MonthDay(8, 4)
    assert not MonthDay(12, 25) == MonthDay(8, 4)
    assert hash(MonthDay(12, 25)) != hash(MonthDay(8, 4))


def test_month_day_date():
    assert MonthDay(8, 4).date(1988) == datetime.date(1988, 8, 4)
    feb_29 = MonthDay(2, 29)
    assert feb_29.date(2016) == datetime.date(2016, 2, 29)
    with raises(ValueError):
        feb_29.date(2015)
    with raises(ValueError):
        feb_29.date(2014)
    with raises(ValueError):
        feb_29.date(2013)
    assert feb_29.date(2012) == datetime.date(2012, 2, 29)
    with raises(ValueError):
        feb_29.date(2011)


def test_month_day_str():
    assert str(MonthDay(8, 4)) == '08-04'
    assert str(MonthDay(12, 25)) == '12-25'


def test_month_day_repr():
    assert repr(MonthDay(8, 4)) == 'monthday.MonthDay(8, 4)'
    assert repr(MonthDay(12, 25)) == 'monthday.MonthDay(12, 25)'
