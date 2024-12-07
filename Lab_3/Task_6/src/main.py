from Lab_3.utils import read_f, write_f


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def multiplication(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append(a[i] * b[j])
    return c


def get_result(c):
    sum_of_tenth = 0
    i = 0
    while i < len(c):
        if i % 10 == 0:
            sum_of_tenth += c[i]
        i += 1
    return sum_of_tenth


if __name__ == "__main__":
    _, a_, b_ = read_f(6)
    a = list(map(int, a_.split()))
    b = list(map(int, b_.split()))
    c = multiplication(a, b)
    quickSort(c, 0, len(c) - 1)
    result = get_result(c)
    write_f(6, result)
