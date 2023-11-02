from times import compute_overlap_time, time_range
from pytest import raises

# Positive test
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert result == expected

# time ranges don't overlap
def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = ['0000-00-00 00:00:00', '0000-00-00 00:00:00']
    assert result == expected

# time ranges that both contain several intervals
def test_multiple_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected =     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00'), ('2010-01-12 11:00:30', '2010-01-12 10:37:00'), ('2010-01-12 11:00:30', '2010-01-12 10:45:00')]
    assert result == expected

# test for end1 = start2
def test_time_ranges_touch():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:45:00")
    result = compute_overlap_time(large, short)
    expected = ['2010-01-12 12:00:00']
    assert result == expected

# test for time_range where end_time is smaller than start_time
def test_backwards_inputs():
    with raises(ValueError) as e:
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
        assert e.match("end_time must be greater than start_time")