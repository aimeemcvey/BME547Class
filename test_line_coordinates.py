# test_line_coordinates.py


def test_new_pair():
    from line_coordinates import new_pair
    answer = new_pair(2, 0)
    # insert 2
    expected = "Your y for a point on this line is 4.0."
    assert answer == expected
