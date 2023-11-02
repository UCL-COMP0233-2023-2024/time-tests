import times
import datetime
from times import compute_overlap_time, time_range
import pytest

def test_compute_overlap_time_1():
    # Test case 1: No overlap
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 01:00:00")
    range2 = time_range("2022-01-01 02:00:00", "2022-01-01 03:00:00")
    assert compute_overlap_time(range1, range2) == []

def test_compute_overlap_time_2():
    # Test case 2: Partial overlap
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00")
    range2 = time_range("2022-01-01 01:00:00", "2022-01-01 03:00:00")
    assert compute_overlap_time(range1, range2) == [("2022-01-01 01:00:00", "2022-01-01 02:00:00")] 

def test_compute_overlap_time_3():
    # Test case 3: Full overlap
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00")
    range2 = time_range("2022-01-01 00:30:00", "2022-01-01 01:30:00")
    assert compute_overlap_time(range1, range2) == [("2022-01-01 00:30:00", "2022-01-01 01:30:00")]

def test_compute_overlap_time_4():
    # Test case 4: One range contained within the other
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 04:00:00")
    range2 = time_range("2022-01-01 01:00:00", "2022-01-01 03:00:00")
    assert compute_overlap_time(range1, range2) == [("2022-01-01 01:00:00", "2022-01-01 03:00:00")]

def test_compute_overlap_time_5():
    # Test case 5: Ranges with gaps
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00", 2, 60)
    range2 = time_range("2022-01-01 01:00:00", "2022-01-01 03:00:00", 2, 60)
    assert compute_overlap_time(range1, range2) == [('2022-01-01 01:00:30', '2022-01-01 01:59:30')]

def test_compute_overlap_time_6():
    # Test case 6: Ranges with more gaps
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00", 3, 60)
    range2 = time_range("2022-01-01 01:00:00", "2022-01-01 03:00:00", 3, 60)
    assert compute_overlap_time(range1, range2) == [('2022-01-01 01:00:00', '2022-01-01 01:19:40'), ('2022-01-01 01:20:40', '2022-01-01 01:39:20'), ('2022-01-01 01:40:20', '2022-01-01 02:00:00')]
    
def test_compute_overlap_time_7():
    # Test case 7: exact overlap
    range1 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00")
    range2 = time_range("2022-01-01 00:00:00", "2022-01-01 02:00:00")
    assert compute_overlap_time(range1, range2) == [('2022-01-01 00:00:00', '2022-01-01 02:00:00')]

    
def test_time_range_input():
    # error when end time is before start time
    pytest.raises(ValueError, time_range, "2022-01-01 03:00:00", "2022-01-01 02:00:00")