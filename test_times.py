from times import compute_overlap_time

def test_given_input():
    result = compute_overlap_time(
        [
            ("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        ],
        [
            ("2010-01-12 10:30:00", "2010-01-12 10:45:00"),
        ]
    )

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:45:00"),
    ]

    assert result == expected