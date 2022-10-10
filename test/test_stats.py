import pytest

from src.data_capture import DataCapture, Stats


def stats_instance(inputs: list) -> Stats:
    dc = DataCapture()
    for i in inputs:
        dc.add(i)
    stats = dc.build_stats()
    return stats


@pytest.mark.parametrize(
    "inputs, input, expected",
    [
        ([3, 9, 3, 4, 6], 4, 2),  # Good scenario
        ([3, 9, 3, 4, 6, 5, 2, 2, 2, 8, 1, 1, 3, 3, 3, 0, 2, 2, 2], 6, 16),  # More data scenario
        ([3, 9, 3, 4, 6], 3, 0),  # Min value,
        ([3, 9, 3, 4, 6], 9, 4),  # Max value
    ]
)
def test_less(inputs, input, expected):
    stats = stats_instance(inputs)
    assert stats.less(input) == expected


@pytest.mark.parametrize(
    "inputs, input, expected",
    [
        ([3, 9, 3, 4, 6], 4, 3),  # Good scenario
        
    ]
)
def test_less_not_equal(inputs, input, expected):
    stats = stats_instance(inputs)
    assert stats.less(input) != expected


@pytest.mark.parametrize(
    "inputs, invalid_input",
    [
        ([3, 9, 3, 4, 6], 5),  # raise exception scenario
    ]
)
def test_less_with_exception(inputs, invalid_input):
    stats = stats_instance(inputs)

    with pytest.raises(KeyError, match="Not valid arguments"):
        stats.less(invalid_input)


@pytest.mark.parametrize(
    "inputs, min_value, max_value, expected",
    [
        ([3, 9, 3, 4, 6], 3, 6, 4),  # Good scenario
        ([3, 9, 3, 4, 6, 5, 2, 2, 2, 8, 1, 1, 3, 3, 3, 0, 2, 2, 2], 3, 8, 9),  # More data scenario
        ([3, 9, 3, 4, 6], 3, 9, 5),  # Min value,
        ([3, 9, 3, 4, 6], 6, 9, 2),  # Max value
    ]
)
def test_between(inputs, min_value, max_value, expected):
    stats = stats_instance(inputs)
    assert stats.between(min_value, max_value) == expected


@pytest.mark.parametrize(
    "inputs, min_value, max_value, expected",
    [
        ([3, 9, 3, 4, 6], 3, 6, 5),  # Good scenario
        ([3, 9, 3, 4, 6, 5, 2, 2, 2, 8, 1, 1, 3, 3, 3, 0, 2, 2, 2], 3, 8, 10),  # More data scenario
    ]
)
def test_between_not_equal(inputs, min_value, max_value, expected):
    stats = stats_instance(inputs)
    assert stats.between(min_value, max_value) != expected


@pytest.mark.parametrize(
    "inputs, invalid_min_value, max_value",
    [
        ([3, 9, 3, 4, 6], 2, 6),  # raise exception scenario
    ]
)
def test_between_with_invalid_min_exception(inputs, invalid_min_value, max_value):
    stats = stats_instance(inputs)
    with pytest.raises(KeyError, match="Not valid arguments"):
        stats.between(invalid_min_value, max_value)


@pytest.mark.parametrize(
    "inputs, min_value, invalid_max_value",
    [
        ([3, 9, 3, 4, 6], 3, 5),  # raise exception scenario
    ]
)
def test_between_with_invalid_max_exception(inputs, min_value, invalid_max_value):
    stats = stats_instance(inputs)
    with pytest.raises(KeyError, match="Not valid arguments"):
        stats.between(min_value, invalid_max_value)


@pytest.mark.parametrize(
    "inputs, input, expected",
    [
        ([3, 9, 3, 4, 6], 4, 2),  # Good scenario
        ([3, 9, 3, 4, 6, 5, 2, 2, 2, 8, 1, 1, 3, 3, 3, 0, 2, 2, 2], 6, 2),  # More data scenario
        ([3, 9, 3, 4, 6], 3, 3),  # Min value,
        ([3, 9, 3, 4, 6], 9, 0),  # Max value
    ]
)
def test_greater(inputs, input, expected):
    stats = stats_instance(inputs)
    assert stats.greater(input) == expected


@pytest.mark.parametrize(
    "inputs, input, expected",
    [
        ([3, 9, 3, 4, 6], 4, 3),  # Good scenario
        
    ]
)
def test_greater_not_equal(inputs, input, expected):
    stats = stats_instance(inputs)
    assert stats.greater(input) != expected


@pytest.mark.parametrize(
    "inputs, invalid_input",
    [
        ([3, 9, 3, 4, 6], 5),  # raise exception scenario
    ]
)
def test_greater_with_exception(inputs, invalid_input):
    stats = stats_instance(inputs)

    with pytest.raises(KeyError, match="Not valid arguments"):
        stats.greater(invalid_input)