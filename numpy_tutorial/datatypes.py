import numpy as np
import sys


def datatypes_init():
    x = np.array([1, 2])
    print(x.dtype)

    x = np.array([1.0, 2.0])
    print(x.dtype)

    x = np.array([1, 2], dtype=np.int64)
    print(x.dtype)


if __name__ == "__main__":
    try:
        datatypes_init()
    except KeyboardInterrupt:
        sys.exit(0)
