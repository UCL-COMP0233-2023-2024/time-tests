import unittest
import times
from times import time_range, compute_overlap_time


test_range1 = "2010-01-12 10:00:00", "2010-01-12 12:00:00"
test_range2 = "2010-01-12 10:30:00", "2010-01-12 10:45:00"


def test_time_range():
    assert(time_range(test_range1[0],test_range1[1])) == [("2010-01-12 10:00:00", "2010-01-12 12:00:00")]


def test_time_range_1split():
    assert(time_range(test_range1[0],test_range1[1],2,0)) == [("2010-01-12 10:00:00", "2010-01-12 11:00:00"),("2010-01-12 11:00:00","2010-01-12 12:00:00")]


def test_time_range_1split_1minute():
    assert(time_range(test_range1[0],test_range1[1],2,60)) == [("2010-01-12 10:00:00", "2010-01-12 10:59:30"),("2010-01-12 11:00:30","2010-01-12 12:00:00")]

def test_time_range_4splits_5minutes():
    assert(time_range(test_range1[0],test_range1[1],4,300)) == [('2010-01-12 10:00:00', '2010-01-12 10:26:15'), ('2010-01-12 10:31:15', '2010-01-12 10:57:30'), ('2010-01-12 11:02:30', '2010-01-12 11:28:45'), ('2010-01-12 11:33:45', '2010-01-12 12:00:00')]

def test_time_range_evensplit_oddgap():
    assert(time_range(test_range1[0],test_range1[1],2,1)) == [("2010-01-12 10:00:00", "2010-01-12 10:59:59"),("2010-01-12 11:00:00","2010-01-12 12:00:00")]


test_time_range()
test_time_range_1split()
test_time_range_1split_1minute()
test_time_range_4splits_5minutes()
test_time_range_evensplit_oddgap()

from unittest import TestCase
from unittest.mock import Mock

from pytest import raises
def test_time_wrong_dates():
    with raises(Exception) as exception: 
        time_range("wrong date 1", "wrong date 2")

test_time_wrong_dates()


class ConstructorTestCase(unittest.TestCase):
    def test_time_wrong_dates(self):
        self.assertRaises(Exception, time_range, "wrong date 1", "wrong date 2")

if __name__ == "__main__":
    unittest.main()


def compute_empty_overlap_time():
    test_range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    test_range2 = time_range("2010-01-13 22:30:00", "2010-01-13 22:45:00")
    result = compute_overlap_time(test_range1,test_range2)
    assert(result) == []

def compute_overlap_time_1h():
    test_range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    test_range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(test_range1,test_range2)
    assert(result) == [("2010-01-12 10:30:00", "2010-01-12 10:45:00")]

compute_empty_overlap_time()
compute_overlap_time_1h()