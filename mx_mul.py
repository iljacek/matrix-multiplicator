import pypy
psyco.full()

from pip._vendor.urllib3.connectionpool import xrange


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
        if self.columns != other.rows:
            raise TypeError("Size of first matrix columns and second matrix rows does not correspond")
        product = [[0 for j in xrange(other.columns)] for i in xrange(self.rows)]
        for i in xrange(self.rows):
            for k in xrange(self.columns):
                for j in xrange(other.columns):
                    product[i][j] += self.values[i][k] * other.values[k][j]
        return Matrix(self.rows, self.columns, product)


def user_input():
    print("Matrix A")
    rows_A = int(input("width: "))
    columns_A = int(input("height: "))

    print("Matrix B")
    rows_B = int(input("width: "))
    columns_B = int(input("height: "))


    print("Matrix A values: ")
    values = [[int((input("Enter element to row {}, column {}: ".format(row, column))))
               for column in range(columns_A)] for row in range(rows_A)]

    matrix = Matrix(rows_A, columns_A, values)
    print("Input is a {}".format(matrix))
    return matrix
