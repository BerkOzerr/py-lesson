import random
import string
import sys


def main():
    if len(sys.argv) >= 2:
        try:
            arg_value = int(sys.argv[1])
            print(generate_id(arg_value))
        except ValueError:
            print("Please your value should be integer.")
    else:
        try:
            x = int(input("Enter your id size :"))
            print(generate_id(x))
        except ValueError:
            print("Please your value should be integer.")


def generate_id(x):
    if x < 1:
        raise ValueError(f"{x} Value must be greater than 0")
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
