from lab_3.utils import read_f, write_f

PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'


def digit_sort(n, m, k, a):

    strings = ['']*n

    for i in range(m):
        line = a[i + 1].strip()
        for j in range(n):
            strings[j] += line[j]

    indexed_strings = [(strings[i], i + 1) for i in range(n)]
    for phase in range(1, k + 1):
        indexed_strings.sort(key=lambda x: x[0][m - phase])

    result = ' '.join(str(index) for _, index in indexed_strings) + '\n'
    return result

if __name__ == '__main__':
    a, read1, read2, read3 = read_f(7)
    a = list(map(int, a.split()))
    n, m, k = a[0], a[1], a[2]
    res = digit_sort(n, m, k, data)
    write_f(7, res)

