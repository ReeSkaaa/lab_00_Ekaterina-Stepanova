from lab_3 import read_f, write_f
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
    quick_Rev_Sort(citations, 0, N-1)
    for i in range(N):
        if citations[i]>=(i+1):
            h = i+1
    return h

if __name__ == "__main__":
    read_vector = read_f("../txtf/input.txt")
    citations = read_vector[0]
    write_f("../txtf/output.txt", str(h_index(citations, len(citations))))