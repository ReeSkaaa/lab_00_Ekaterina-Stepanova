def partition(arr, low, high):
    # Choose the pivot
    pivot = arr[high]

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1


# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def multiplication(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append(a[i] * b[j])
    return c


# Main driver code
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [7, 1, 4, 9]
    b = [2, 7, 8, 11]
    c = multiplication(a, b)
    quickSort(c, 0, len(c) - 1)
    for i in c:
        print(i, end=' ')
