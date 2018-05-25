import Project2.Date as Date
import pytest


def test_properties():
    date1 = Date.Date(23, 12, 1999)
    date2 = Date.Date(1, 1, 2012)
    assert date1.year == 1999 and date2.year == 2012
    assert date1.month == 12 and date2.month == 1
    assert date1.day == 23 and date2.day == 1

def test_value_error():
    with pytest.raises(ValueError):
        date1 = Date.Date(32, 12, 2007)
    with pytest.raises(ValueError):
        date1 = Date.Date(1, 1, 1969)
    with pytest.raises(ValueError):
        date1 = Date.Date(1, 13, 1970)

def test_date_behaviour():
    assert Date.Date(0, 0, 1970).day == 1
    assert Date.Date(0, 0, 1970).month == 1
    try:
        Date.Date(29, 2, 2000)
    except ValueError:
        pytest.fail("Unexpected ValueError")

def test_operators():
    date1 = Date.Date(3, 4, 2005)
    date2 = Date.Date(5, 6, 2007)
    date3 = Date.Date(1, 4, 2005)
    date4 = Date.Date(3, 4, 2005)
    assert date1 > date3
    assert date3 < date1
    assert date1 == date4
    assert date1 >= date4
    assert date1 <= date2
