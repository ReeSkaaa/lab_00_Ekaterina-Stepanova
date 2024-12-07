from Lab_4.utils import read_f, write_f


def postfix_notation(data):
    stack = list()
    for char in data:
        if not char.isdigit():
            second = stack.pop()
            first = stack.pop()
            if char == '+':
                stack.append(first + second)
            elif char == '*':
                stack.append(first * second)
            elif char == '-':
                stack.append(first - second)
        else:
            stack.append(int(char))
    ans = stack[0]
    return ans


if __name__ == "__main__":
    N, data = read_f(8)
    data = list(map(str, data.split()))
    result = postfix_notation(data)
    write_f(8, result)
