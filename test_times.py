from times import time_range, compute_overlap_time
import datetime

def test_given_input():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

        result = compute_overlap_time(large, short)
        print(result)
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        assert result == expected

def test_do_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = ['0000-00-00 00:00:00', '0000-00-00 00:00:00']
    assert result == expected

def test_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected =     [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00'), ('2010-01-12 11:00:30', '2010-01-12 10:37:00'), ('2010-01-12 11:00:30', '2010-01-12 10:45:00')]
    assert result == expected

def test_time_ranges_touch():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:45:00")
    result = compute_overlap_time(large, short)
    expected = ['2010-01-12 12:00:00']
    assert result == expected


        

