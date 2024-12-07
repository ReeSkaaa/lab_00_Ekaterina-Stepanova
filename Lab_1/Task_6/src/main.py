from Lab_1.utils import read_f, write_f


def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


if __name__ == '__main__':
    read = read_f(6)
    data = list(map(int, read[0].split()))
    result = [*map(str, bubble_sort(data))]
    res = ''
    for i in result:
        res += i + ' '
    write_f(6, res)
