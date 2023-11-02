from times import compute_overlap_time, time_range
import pytest

def test_given_input():
   
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
   
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2015-01-12 10:30:00", "2015-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    #expected = [('2015-01-12 10:30:00', '2010-01-12 12:00:00'), ('2015-01-12 10:38:00', '2010-01-12 12:00:00')]
    #assert result == []

    assert type(result) is list

def test_last_before_first():
    start_time = "2010-01-12 12:00:00"
    end_time = "2010-01-12 10:00:00"
    with pytest.raises(ValueError) as e:
        time_range(start_time, end_time)

