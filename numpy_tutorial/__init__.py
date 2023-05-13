from .array_math import array_dot_product, array_math_init, array_math_overview
from .arrays import array_creation, array_init, array_overview
from .datatypes import datatypes_init


def numpy_tutorial():
    while True:
        print("1 - arrays")
        print("2 - datatypes")
        print("3 - array math")
        print("4 - back")

        choice = int(input("choice: "))
        match choice:
            case 1:
                array_init()
            case 2:
                datatypes_init()
            case 3:
                array_math_init()
            case 4:
                break
            case _:
                print("invalid choice!")


__all__ = [
    "array_creation",
    "array_overview",
    "array_init",
    "array_dot_product",
    "array_math_overview",
    "array_math_init",
    "datatypes_init",
    "numpy_tutorial",
]
