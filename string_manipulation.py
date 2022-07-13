"""String manipulation tutorial"""

from copy import deepcopy


def checker1(test_brackets):
    """"Brackets balance checker #1"""
    old_len = len(test_brackets)
    result = deepcopy(test_brackets)
    while True:
        result = result.replace(
            "()", "").replace("[]", "").replace("{}", "")
        if len(result) != old_len:  # replacement have just done.
            old_len = len(result)
        elif len(result) == 0:  # no more brackets, proceed to quit the loop
            return True
        else:  # IMBALANCE total of brackets have been found, quit the loop
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
