import pytest

@pytest.mark.smoke
def test_one_is_one(separator):
    assert 1 == 1

@pytest.mark.regression
def test_two_is_two(separator):
    assert 2 == 2

@pytest.mark.skip('Bug-21')
def test_three_is_three(separator):
    assert  3 == 4



