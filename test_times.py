from times import compute_overlap_time, time_range
import pytest

# tests for: positive test, time ranges don't overlap, time ranges containing several intervals, and end1 == start1
@pytest.mark.parametrize("large, short, expected", [
    (
        [('2010-01-12 10:00:00', '2010-01-12 12:00:00')],
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')],
        [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    ),
    (
        [('2010-01-12 10:00:00', '2010-01-12 12:00:00')],
        [('2011-01-12 10:30:00', '2011-01-12 10:37:00'), ('2011-01-12 10:38:00', '2011-01-12 10:45:00')],
        ['0000-00-00 00:00:00', '0000-00-00 00:00:00']
    ),
    (
        [('2010-01-12 10:00:00', '2010-01-12 10:59:30'), ('2010-01-12 11:00:30', '2010-01-12 12:00:00')],
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')],
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00'), ('2010-01-12 11:00:30', '2010-01-12 10:37:00'), ('2010-01-12 11:00:30', '2010-01-12 10:45:00')]
    ),
    (
        [('2010-01-12 10:00:00', '2010-01-12 12:00:00')],
        [('2010-01-12 12:00:00', '2010-01-12 13:45:00')],
        ['2010-01-12 12:00:00']
    )
])
def test_compute_overlap_time(large, short, expected):
    result = compute_overlap_time(large, short)
    assert result == expected

# test for time_range where end_time is smaller than start_time
def test_backwards_inputs():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        assert e.match("end_time must be greater than start_time")