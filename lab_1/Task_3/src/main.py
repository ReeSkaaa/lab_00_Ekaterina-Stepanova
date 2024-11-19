from lab_1.utils import read_f, write_f

PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def insertion_sort(a, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] > a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

    return a


def main():
    read_res = read_f(PATH)
    n = read_res[0]
    if (1 <= n <= 10 ** 3):
        a = read_res[1]
        write_f(PATH_OUTPUT, str(insertion_sort(a, n)))
if __name__ == '__main__':
    n, read = read_f(3)
    data = list(map(int, read.split()))
    result = insertion_sort(data, int(n))
    write_f(3, result)