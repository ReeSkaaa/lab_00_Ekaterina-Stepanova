from lab_3.utils import read_f, write_f

PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'


def scarecrow_sort(n, k, data):
    groups = [[] for i in range(k)]
    for i in range(n):
        groups[i % k].append(data[i])
    for group in groups:
        group.sort(reverse=True)

    sorted_items = [groups[i % k][i // k] for i in range(n)]
    return sorted_items == sorted(sorted_items, reverse=True)


if __name__ == "__main__":
    a, read = read_f(3)
    a = a.split()
    n, k = int(a[0]), int(a[1])
    data = list(map(int, read.split()))
    result = scarecrow_sort(n, k, data)
    if result:
        write_f(3, "ДА")
    else:
        write_f(3, "НЕТ")
