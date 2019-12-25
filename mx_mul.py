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

    def print_matrix_content(self):
        for row in range(self.rows):
            print(" ".join(map(str, self.values[row])))


def get_dimensions():
    columns = int(input("width: "))
    rows = int(input("height: "))
    if rows <= 0 and columns <= 0:
        raise ValueError("Invalid dimensions of matrix")
    return rows, columns


def fill_values(rows, columns):
    values = []
    for row in range(rows):
        values.append(list(map(int, input().split(" "))))
        if len(values[row]) != columns:
            raise ValueError("Invalid number of elements in row")
    return values


def user_input():
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
