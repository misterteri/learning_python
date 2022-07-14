"""Dicitionary Tutorial"""

from copy import deepcopy
from pyexpat.errors import messages


students = {
    "name": "john",
    "age": 26,
    "sex": "male",
}
# print(students["age"])

# alphabet a to z
alphabet = "abcdefghijklmnopqrstuvwxyz"  # just a normal string
alphabet_dict = {}  # empty dictionary


def encrypted_message(message: str, direction: int) -> str:
    for i in range(len(alphabet)):
        alphabet_dict[alphabet[i]] = alphabet[(i+direction) % len(alphabet)]

    for letters in message:
        print(alphabet_dict[letters], end="")

    return


def main():
    message = "abcde"
    direction = 1
    # alphabet_dict[alphabet[0]] = alphabet[(0+1) % len(alphabet)]
    encrypted_message(message, direction)
    # print(message)


if __name__ == "__main__":
    main()

my_dict = {34: 'apple', 65: 'ball', 32: 'cat', 78: 'dog'}

# values = list(my_dict.values())
# i = len(values)-1
# for item in my_dict:
#     my_dict[item] = values[i]
#     i -= 1

# print(my_dict)
