import sys
from numpy_tutorial import array_init


def main():
    while True:
        print("1 - numpy tutorial")
        print("2 - exit")

        choice = int(input("choice: "))
        match choice:
            case 1:
                array_init()
            case 2:
                break
            case _:
                print("invalid choice!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
