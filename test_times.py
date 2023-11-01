from times import time_range, compute_overlap_time


def test_full_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_no_overlap():
    range0 = time_range("2010-01-12 09:00:00", "2010-01-12 09:59:59", 2, 60)
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(large, range0)
    expected = ValueError("There is no overlap")
    assert result == expected



def test_point_overlap():
    range1 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00") # fail if have intervals????????????????
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    result = compute_overlap_time(large, range1)
    expected = "2010-01-12 10:00:00" #problem: not a list--how to solve
    assert result == expected

def test_partial_overlap():
    range2 = time_range("2010-01-12 09:30:00", "2010-01-12 10:40:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(range2, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:40:00')]
    assert result == expected

    

