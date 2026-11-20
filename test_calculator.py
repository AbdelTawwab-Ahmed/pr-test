from calculator import calculate_total


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_empty_prices():
    assert calculate_total([]) == 0
