from lab_1.utils import read_f, write_f

PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def insertion_sort(a, n):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break

    return a
if __name__ == '__main__':
    n, read = read_f(1)
    data = list(map(int, read.split()))
    result = insertion_sort(data, int(n))
    write_f(1, result)

