from Lab_3.utils import read_f, write_f


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] > pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_Rev_Sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_Rev_Sort(arr, low, p - 1)
        quick_Rev_Sort(arr, p + 1, high)
    return arr


def h_index(citations, N):
    h = 0
    quick_Rev_Sort(citations, 0, N - 1)
    for i in range(N):
        if citations[i] >= (i + 1):
            h = i + 1
    return h


if __name__ == "__main__":
    read = read_f(5)
    a = read[0]
    a = list(map(int, a.split()))
    result = h_index(a, len(a))
    write_f(5, result)
