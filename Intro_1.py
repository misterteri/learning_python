import argparse


def addition(first_number: int | float, second_number: int | float) -> int | float:
    return first_number + second_number


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--first_number",
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
    args = parser.parse_args()
    result = addition(args.first_number, args.second_number)
    print(result)


if __name__ == "__main__":
    main()
