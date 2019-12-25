import pytest


class DB:
    a = 25
    b = 30
    c = 5


class Matrix1:
    rows = 2
    columns = 3
    values = [[2, 1, 4], [5, 4, 3]]


@pytest.fixture(scope="session")
def db():
    return DB()


@pytest.fixture(scope="session")
def matrix_1():
    return Matrix1()
