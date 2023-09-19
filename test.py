def test_addition():
    result = 2 + 2
    expected = 4
    assert result == expected, f"Addition test failed. Expected: {expected}, but got: {result}"

def test_subtraction():
    result = 5 - 3
    expected = 2
    assert result == expected, f"Subtraction test failed. Expected: {expected}, but got: {result}"

def test_multiplication():
    result = 4 * 3
    expected = 12
    assert result == expected, f"Multiplication test failed. Expected: {expected}, but got: {result}"

# Run the tests
test_addition()
test_subtraction()
test_multiplication()