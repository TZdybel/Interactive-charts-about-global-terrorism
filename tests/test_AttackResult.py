from Project2 import AttackResult as ar
import pytest


def test_properties():
    atckres = ar.AttackResult(True, False, 4, 5)
    assert atckres.num_of_kills == 4
    assert atckres.num_of_wounded == 5
    assert atckres.is_successful == True
    assert atckres.is_suicide_committed == False

def test_value_error():
    with pytest.raises(ValueError):
        ar.AttackResult(True, True, -2, 10)
    with pytest.raises(ValueError):
        ar.AttackResult(True, True, 10, -2)