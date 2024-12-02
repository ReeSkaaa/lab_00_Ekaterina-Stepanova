from lab_4.utils import read_f, write_f

MATCH_BRACKETS = {')': '(', ']': '[', '}': '{'}


def check_brackets(data):
    """Организует поиск правильной скобочной последовательности"""
    stack = list()
    for index, sym in enumerate(data):
        if sym in "{([":
            stack.append((sym, index + 1))
        elif sym in "])}":
            if not stack:
                return index + 1
            top, position = stack.pop()
            if top != MATCH_BRACKETS[sym]:
                return index + 1

    if stack:
        i, position = stack[0]
        return position
    return "Success"


if __name__ == "__main__":
    a = read_f(4)
    data = list(map(str, a[0].strip()))
    result = check_brackets(data)
    write_f(4, result)
