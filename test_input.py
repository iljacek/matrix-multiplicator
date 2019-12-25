import pytest
import mx_mul


def test_dimensions():
    matrix = mx_mul.Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    # matrix = mx_mul.user_input()
    assert len(matrix.values) == matrix.rows
    for row in range(matrix.rows):
        assert len(matrix.values[row]) == matrix.columns


def test_invalid_dimensions():
    with pytest.raises(ValueError):
        mx_mul.Matrix(0, 3, [])
    with pytest.raises(ValueError):
        mx_mul.Matrix(-42, 3, [])
    with pytest.raises(ValueError):
        mx_mul.Matrix(3, 0, [])
    with pytest.raises(ValueError):
        mx_mul.Matrix(3, -3, [])
    with pytest.raises(ValueError):
        mx_mul.Matrix(-42, -3, [])
