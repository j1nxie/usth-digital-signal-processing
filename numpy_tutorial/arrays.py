import sys

import numpy as np


def array_overview():
    a = np.array([1, 2, 3])
    print(type(a))
    print(a.shape)
    print(a[0], a[1], a[2])
    a[0] = 5
    print(a)

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b.shape)
    print(b[0, 0], b[0, 1], b[1, 0])


def array_creation():
    a = np.zeros((2, 2))
    print(a)

    b = np.ones((1, 2))
    print(b)

    c = np.full((2, 2), 7)
    print(c)

    d = np.eye(2)
    print(d)

    e = np.random.random((2, 2))
    print(e)


def array_slicing():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    b = a[:2, 1:3]

    print(a[0, 1])
    b[0, 0] = 77
    print(a[0, 1])

    row_r1 = a[1, :]
    row_r2 = a[1:2, :]
    print(row_r1, row_r1.shape)
    print(row_r2, row_r2.shape)

    col_r1 = a[:, 1]
    col_r2 = a[:, 1:2]
    print(col_r1, col_r1.shape)
    print(col_r2, col_r2.shape)


def array_integer_indexing():
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a[[0, 1, 2], [0, 1, 0]])

    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

    print(a[[0, 0], [1, 1]])

    print(np.array([a[0, 1], a[0, 1]]))

    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(b)

    c = np.array([0, 2, 0, 1])
    print(b[np.arange(4), c])

    b[np.arange(4), c] += 10
    print(b)


def array_boolean_indexing():
    a = np.array([[1, 2], [3, 4], [5, 6]])

    bool_idx = a > 2
    print(bool_idx)

    print(a[bool_idx])
    print(a[a > 2])


def array_init():
    print("- Array overview:")
    array_overview()
    print("- Array creation:")
    array_creation()
    print("- Array slicing:")
    array_slicing()
    print("- Array integer indexing:")
    array_integer_indexing()
    print("- Array boolean indexing:")
    array_boolean_indexing()


if __name__ == "__main__":
    try:
        array_init()
    except KeyboardInterrupt:
        sys.exit(0)
