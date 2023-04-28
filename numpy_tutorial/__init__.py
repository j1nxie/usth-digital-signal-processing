from .arrays import array_creation, array_overview, array_init
from .datatypes import datatypes_init


def numpy_tutorial():
    while True:
        print("1 - arrays")
        print("2 - datatypes")
        print("3 - back")

        choice = int(input("choice: "))
        match choice:
            case 1:
                array_init()
            case 2:
                datatypes_init()
            case 3:
                break
            case _:
                print("invalid choice!")


__all__ = [
    "array_creation",
    "array_overview",
    "array_init",
    "datatypes_init",
    "numpy_tutorial",
]
