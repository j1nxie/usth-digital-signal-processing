import sys

import numpy as np


def array_math_overview():
    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)

    print("# Adding:")
    print("- with + operator:")
    print(x + y)
    print("- with add() method:")
    print(np.add(x, y))

    print("# Subtracting:")
    print("- with - operator:")
    print(x - y)
    print("- with subtract() method:")
    print(np.subtract(x, y))

    print("# Elementwise product:")
    print("- with * operator:")
    print(x * y)
    print("- with multiply() method:")
    print(np.multiply(x, y))

    print("# Elementwise division:")
    print("- with / operator:")
    print(x / y)
    print("- with divide() method:")
    print(np.divide(x, y))

    print("# Elementwise square root with sqrt() method:")
    print(np.sqrt(x))


def array_dot_product():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    v = np.array([9, 10])
    w = np.array([11, 12])

    print("# Inner product of vectors:")
    print("- with x.dot(y) method:", v.dot(w))
    print("- with np.dot(x, y) method:", np.dot(v, w))
    print()

    print("# Matrix / vector product:")
    print("- with x.dot(y) method:", x.dot(v))
    print("- with np.dot(x, y) method:", np.dot(x, v))
    print()

    print("# Matrix / matrix product:")
    print("- with x.dot(y) method:")
    print(x.dot(y))
    print("- with np.dot(x, y) method:")
    print(np.dot(x, y))
    print()


def array_sum():
    x = np.array([[1, 2], [3, 4]])

    print("- Sum of all elements:", np.sum(x))
    print("- Sum of each column:", np.sum(x, axis=0))
    print("- Sum of each row:", np.sum(x, axis=1))


def array_manipulation():
    x = np.array([[1, 2], [3, 4]])

    print(x)
    print("- Transposition of x:")
    print(x.T)

    v = np.array([1, 2, 3])
    print("- Taking transpose of rank 1 array does nothing.")
    print(v)
    print(v.T)


def array_math_init():
    print("- Array math overview:")
    array_math_overview()
    print()

    print("- Array dot products:")
    array_dot_product()
    print()

    print("- Array sum:")
    array_sum()
    print()

    print("- Array manipulation:")
    array_manipulation()
    print()


if __name__ == "__main__":
    try:
        array_math_init()
    except KeyboardInterrupt:
        sys.exit(0)
