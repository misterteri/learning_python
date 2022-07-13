"""String manipulation tutorial"""

from cgi import test
from copy import deepcopy
from operator import truediv


def checker1(test_brackets):
    """"Brackets balance checker #1"""
    old_len = len(test_brackets)
    result = deepcopy(test_brackets)
    while True:
        result = result.replace(
            "()", "").replace("[]", "").replace("{}", "")
        if len(result) != old_len:
            old_len = len(result)
        elif len(result) == 0:
            return True
        else:
            return False


def checker2(brackets):
    """Check if brackets are balanced."""
    while True:
        if '()' in brackets:
            brackets = brackets.replace("()", "")
        elif '{}' in brackets:
            brackets = brackets.replace("{}", "")
        elif '[]' in brackets:
            brackets = brackets.replace("[]", "")
        else:
            return not brackets


def main():
    """Main driver"""
    example = ("{{(({[]}))}")
    print(checker1(example))
    print(checker2(example))


if __name__ == "__main__":
    main()
