import random
from lab_3.utils import read_f, write_f

PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'

def quick_sort(a):
    if len(a) <= 1:
        return a
    elem = a[random.randint(0, len(a) - 1)]
    left = [i for i in a if i < elem]
    mid = [elem] * a.count(elem)
    right = [i for i in a if i > elem]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
   _, read = read_f(1)
   data = list(map(int, read.split()))
   result = quick_sort(data)
   write_f(1, result)

