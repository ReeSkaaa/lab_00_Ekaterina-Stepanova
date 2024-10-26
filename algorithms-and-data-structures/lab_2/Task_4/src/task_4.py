from memory_profiler import profile
from lab_2.Task_4.utils import read_f, write_f

@profile
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
    read = read_f('../txtf/input.txt')
    n = read[0]
    a = read[1]
    k = read[2]
    b = read[3]
    if (1 <= n, k <= 10 ** 5):
        result = ''
        for i in range(k):
            result+= str(binary_search(a, b[i])) + ' '
    write_f('../txtf/input.txt', result)