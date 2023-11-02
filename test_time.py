import times

def test_given_input():
    range1 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    overlap = times.compute_overlap_time(range1, range2)

    # Define the expected overlap intervals based on output on file "time.py"
    expected_overlap = [
       ('2010-01-12 10:30:00', '2010-01-12 10:38:30'), ('2010-01-12 10:39:30', '2010-01-12 10:48:00')
    ]

    # Print the actual and expected overlap intervals just to check
    print("Actual Overlap:", overlap)
    print("Expected Overlap:", expected_overlap)

    
    assert overlap == expected_overlap

if __name__ == "__main__":
    test_given_input()

from times import time_range, compute_overlap_time

def test_non_overlapping_ranges():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:30:00", "2010-01-12 11:45:00")
    overlap = compute_overlap_time(range1, range2)

    # Define the expected overlap intervals, which should be an empty list
    expected_overlap = []

    # Print the actual and expected overlap intervals just to check
    print("Actual Overlap:", overlap)
    print("Expected Overlap:", expected_overlap)

    assert overlap == expected_overlap

if __name__ == "__main__":
    test_non_overlapping_ranges()

if __name__ == "__main":
    # Define two time ranges with multiple intervals
    range3 = time_range("2023-01-01 08:00:00", "2023-01-01 09:00:00", 3, 30)
    range4 = time_range("2023-01-01 08:30:00", "2023-01-01 09:30:00", 3, 30)

    # Calculate the overlap between the two time ranges
    overlap = compute_overlap_time(range3, range4)

    # Check if there is an overlap
    if overlap:
        print("There is overlap between the two time ranges.")
    else:
        print("The two time ranges do not overlap.")