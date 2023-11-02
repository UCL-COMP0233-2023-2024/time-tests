from times import time_range,compute_overlap_time
import pytest


def test_given_result():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 6, 36)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:32:00'), ('2010-01-12 10:32:36', '2010-01-12 10:34:36'), ('2010-01-12 10:35:12', '2010-01-12 10:37:12'), ('2010-01-12 10:37:48', '2010-01-12 10:39:48'), ('2010-01-12 10:40:24', '2010-01-12 10:42:24'), ('2010-01-12 10:43:00', '2010-01-12 10:45:00')]
    assert result == expected

def second_test():
    # two time ranges that both contain several intervals each
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 6, 36)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:32:00'), ('2010-01-12 10:32:36', '2010-01-12 10:34:36'), 
                ('2010-01-12 10:35:12', '2010-01-12 10:37:12'), ('2010-01-12 10:37:48', '2010-01-12 10:39:48'), 
                ('2010-01-12 10:40:24', '2010-01-12 10:42:24'), ('2010-01-12 10:43:00', '2010-01-12 10:45:00')]
    assert result == expected

second_test()    

def no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short =  time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large,short)
    expected = []
    assert result == expected

#large = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
#print(large)
#short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
#print(compute_overlap_time(large,short))


def third_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short =  time_range("2010-01-12 12:00:00", "2010-01-12 12:15:00", 6, 36)
    result = compute_overlap_time(large,short)
    #print(result)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00'), ('2010-01-12 12:02:36', '2010-01-12 12:00:00'), 
     ('2010-01-12 12:05:12', '2010-01-12 12:00:00'), ('2010-01-12 12:07:48', '2010-01-12 12:00:00'), 
     ('2010-01-12 12:10:24', '2010-01-12 12:00:00'), ('2010-01-12 12:13:00', '2010-01-12 12:00:00')]
    assert result == expected
third_case()