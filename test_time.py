import times

def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    overlap = times.compute_overlap_time(large, short)

    # Define the expected overlap intervals based on output on file "time.py"
    expected_overlap = [
       ('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    # Print the actual and expected overlap intervals just to check
    print("Actual Overlap:", overlap)
    print("Expected Overlap:", expected_overlap)

    
    assert overlap == expected_overlap

if __name__ == "__main__":
    test_given_input()



