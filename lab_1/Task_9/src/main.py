from lab_1.utils import read_f, write_f

PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'



def binary_addition(n1, n2):
    ans = []
    n1 = n1[::-1]
    n2 = n2[::-1]
    max_size = max(len(n2), len(n1))
    n1 += (max_size - len(n1)) * [0]
    n2 += (max_size - len(n2)) * [0]
    limit = 0
    for a in zip(n1, n2):
        add = a[0] + a[1] + limit
        limit = add // 2
        ans.append(add % 2)

    if limit == 1:
        ans.append(1)

    ans = ans[::-1]
    return ''.join(map(str, ans))


if __name__ == '__main__':
    read_ = read_f(9)
    read = read_[0].split()
    n1, n2 = read[0], read[1]
    n1 = [*map(int, n1)]
    n2 = [*map(int, n2)]
    write_f(9, binary_addition(n1, n2))
