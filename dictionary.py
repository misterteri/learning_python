"""Dicitionary Tutorial"""


# usual dictionary
students = {
    "name": "john",
    "age": 26,
    "sex": "male",
}
# example command: print(students["age"])


ALPHABET = "abcdefghijklmnopqrstuvwxyz"  # just a normal string
alphabet_dict = {}  # empty dictionary


def encrypted_message(message: str, direction: int) -> str:
    """function to encrypt a message and will output the encrypted message"""
    for idx, _ in enumerate(ALPHABET):
        alphabet_dict[ALPHABET[idx]] = ALPHABET[(
            idx+direction) % len(ALPHABET)]

    for idx, _ in enumerate(message):
        message = message[:idx] + alphabet_dict[message[idx]] + message[idx+1:]
        # print(alphabet_dict[letters], end="")
        # easier way to just print it

    return message


def main():
    """main function"""
    message = "abcde"
    direction = 10
    print(encrypted_message(message, direction))


if __name__ == "__main__":
    main()
