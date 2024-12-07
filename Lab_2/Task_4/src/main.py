from Lab_2.utils import read_f, write_f


def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    _, read, search_elem = read_f(4)
    data = list(map(int, read.split()))
    result = binary_search(data, int(search_elem))
    write_f(3, str(result))
