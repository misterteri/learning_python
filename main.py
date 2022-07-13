"""Practice Python 3.10"""

import argparse


def addition(first_number: int | float, second_number: int | float) -> int | float:
    """addition() receives two numbers and returns the sum of them"""
    return first_number + second_number


def multiplication(first_number: int | float, second_number: int | float) -> int | float:
    """multiplication() receives two numbers and returns the product of them"""
    return first_number * second_number
# lambda function # to make the funtion to a one lineR
# multiplication = lambda first_number, second_number: first_number * second_number
# def addition and multiplication are the ways to declare a function in python

# multiplication: Callable[[int | float, int | float], int | float]
# = lambda first_number, second_number: first_number * second_number


def main():
    """ list of arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",  # names to be called to insert the number into
        "--first_number",  # names to be called to insert the number into
        metavar="first_number",
        type=int,
        default=0
    )
    parser.add_argument(
        "-s",
        "--second_number",
        metavar="second_number",
        type=int,
        default=0
    )
    parser.add_argument(
        "-a",
        "--action",
        metavar="action",
        type=str,
        default=0
    )

    args = parser.parse_args()

    if args.action == "addition":
        result = addition(args.first_number, args.second_number)

    elif args.action == "multiplication":
        result = multiplication(args.first_number, args.second_number)

    print(result)


if __name__ == "__main__":
    main()

# example input =  python Intro_1.py -a multiplication -f 3 -s 5
# links
# https://docs.python.org/3/howto/argparse.html

# pylint to score and improve the readability of the code
