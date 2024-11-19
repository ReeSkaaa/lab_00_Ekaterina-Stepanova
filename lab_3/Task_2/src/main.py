from lab_3.utils import read_f, write_f


PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def antiQuickSortPermutation(n):
    perm = [i for i in range(1, n + 1)]

    for i in range(2, n):
        swap(perm, i // 2, i)

    return perm


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    read = read_f(2)
    n = int(read[0])
    result = antiQuickSortPermutation(n)
    write_f(2, result)