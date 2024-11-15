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


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [7, 1, 4, 9]
    b = [2, 7, 8, 11]
    c = multiplication(a, b)
    quickSort(c, 0, len(c) - 1)
    for i in c:
        print(i, end=' ')
