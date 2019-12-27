# !usr/bin/env python3

# =====================================================
#  mx_mul - Hiring project
#
#  Author: Lubomir Svehla <lubomir.svehla@gmail.com>
#
#  mx_mul.py created: 2019-December-25
# =====================================================


class Matrix:
    def __init__(self, rows, columns, values):
        self.rows = rows
        self.columns = columns
        if rows > 0 and columns > 0:
            self.values = values
        else:
            raise ValueError("Invalid dimensions of matrix")

    def __str__(self):
        return "Matrix of dimensions {}x{} with values: {}".format(self.rows, self.columns, self.values)

    def multiply(self, other):
        """
        Multiplies current matrix with another one
        @param other: matrix to be multiplied with current instance
        @return: new matrix object with the result

        """
        if self.columns != other.rows:
            raise TypeError("Size of first matrix columns and second matrix rows does not correspond")
        product = [[sum(element_a * element_b for element_a, element_b in zip(column, row))
                    for column in zip(*other.values)] for row in self.values]
        return Matrix(self.rows, self.columns, product)

    def print_matrix_content(self):
        """
        Prints the matrix in human readable form
        """
        for row in range(self.rows):
            print(" ".join(map(str, self.values[row])))


def get_dimensions():
    """
    Get dimensions of matrix from user input
    @return: two integers, containing number of rows and columns
    """
    columns = int(input("width: "))
    rows = int(input("height: "))
    if rows <= 0 and columns <= 0:
        raise ValueError("Invalid dimensions of matrix")
    return rows, columns


def fill_values(rows, columns):
    """
    Fill the matrix values from user input
    @param rows: number of rows of new matrix
    @param columns: number of columns of new matrix
    @return: two-dimensional list, which contains values of the matrix
    """
    values = []
    for row in range(rows):
        values.append(list(map(int, input().split(" "))))
        if len(values[row]) != columns:
            raise ValueError("Invalid number of elements in row")
    return values


def user_input():
    """
    Presents form for user and waits for his input
    @return: two matrix objects with matrices, to be multiplied later
    """
    print("\nMatrix A")
    rows_A, columns_A = get_dimensions()
    print("\nMatrix B")
    rows_B, columns_B = get_dimensions()

    print("\nMatrix A values: ")
    values_A = fill_values(rows_A, columns_A)
    print("\nMatrix B values: ")
    values_B = fill_values(rows_B, columns_B)

    matrix_A = Matrix(rows_A, columns_A, values_A)
    matrix_B = Matrix(rows_B, columns_B, values_B)

    # print("Input matrices are: \n{} \n{}".format(matrix_A, matrix_B))
    return matrix_A, matrix_B
