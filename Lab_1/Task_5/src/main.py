from Lab_1.utils import read_f, write_f


def selection_sort(a, n):
    for i in range(n - 1):
        min_elem = i
        for j in range(i + 1, n):
            if a[j] < a[min_elem]:
                min_elem = j
        a[i], a[min_elem] = a[min_elem], a[i]
    return a


if __name__ == '__main__':
    n, read_res = read_f(5)
    data = list(map(int, read_res.split()))
    result = selection_sort(data, int(n))
    write_f(5, result)
