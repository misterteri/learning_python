"""String manipulation tutorial"""

from copy import deepcopy
from operator import truediv


def main():
    """Main driver."""
    brackets = "{[()]}"
    brackets2 = "([{}])"
    result = brackets2.replace("{", "").replace("}", "").replace(
        "(", "").replace(")", "").replace("[", "").replace("]", "")
    print(result)
    if len(result) == 0:
        return True
    return False


if __name__ == "__main__":
    print(main())
