"""String manipulation tutorial"""

from copy import deepcopy


def main():
    """Main driver."""
    alphabet: str = "abcabc"
    print(alphabet.find("abcabc"))
    # to make the new object 'new' independent to 'alphabet'
    new = deepcopy(alphabet)
    new = new + "abc"
    print(alphabet)
    print(new)


if __name__ == "__main__":
    main()
