import random
import string
import sys


def main():
    arg_length = sys.argv[1] if len(sys.argv) >= 2 else None
    if arg_length is None:
        x = input("Enter your Id key length Number :")
        print(generate_id(x))
    else:
        try:
            print(generate_id(arg_length))
        except ValueError:
            print(f"x = {arg_length} value must be >= 1")


def generate_id(x):
    if not isinstance(x, int):
        raise TypeError(f"must be integer x : {type(x).__name__}")
    if x < 1:
        raise ValueError("x should be greater than 0")
    generator_list = [
        random.choice(string.ascii_lowercase)
        if i < x // 2
        else random.choice(string.digits)
        for i in range(x)
    ]
    random.shuffle(generator_list)
    return "".join(generator_list)


if __name__ == "__main__":
    main()
