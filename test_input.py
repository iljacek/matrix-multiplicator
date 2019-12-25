import pytest
import mx_mul


def test_user_input():
    matrix_A, matrix_B = mx_mul.user_input()
    assert matrix_A.rows == len(matrix_A.values)
    assert matrix_A.columns == len(matrix_A.values[0])
    assert matrix_B.rows == len(matrix_B.values)
    assert matrix_B.columns == len(matrix_B.values[0])


def test_dimensions():
    matrix = mx_mul.Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
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
