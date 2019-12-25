import pytest
import mx_mul


@pytest.fixture
def init_matrix():
    matrix = mx_mul.Matrix(3, 2, [[1, 2], [4, 5], [8, 6]])
    matrix_2 = mx_mul.Matrix(2, 4, [[-25, -16, 1, 2], [71, -18, -8, -4]])
    return matrix, matrix_2


def test_square():
    matrix = mx_mul.Matrix(2, 2, [[1, 2], [4, 5]])
    matrix_2 = mx_mul.Matrix(2, 2, [[5, 6], [7, 8]])
    result = matrix.multiply(matrix_2)
    assert result.values == [[19, 22], [55, 64]]
    matrix_2 = mx_mul.Matrix(2, 2, [[-25, -16], [71, -18]])
    result = matrix.multiply(matrix_2)
    assert result.values == [[117, -52], [255, -154]]


def test_rectangular(init_matrix):
    matrix, matrix_2 = init_matrix
    result = matrix.multiply(matrix_2)
    assert result.values == [[117, -52, -15, -6], [255, -154, -36, -12], [226, -236, -40, -8]]


# def test_big():
#     pass


def test_invalid(init_matrix):
    matrix, matrix_2 = init_matrix
    with pytest.raises(TypeError):
        result = matrix_2.multiply(matrix)