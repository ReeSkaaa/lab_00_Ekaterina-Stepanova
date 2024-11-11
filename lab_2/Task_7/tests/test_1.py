import random
from lab_2.Task_7.src import find_max_subarray
import time
from lab_2.Task_5.utils import read_f, write_f


def main():
    if __name__ == '__main__':
        read = read_f('../txtf/input.txt')
        n = read[0]
        a = [random.randint(-10 ** 3, 10 ** 3) for i in range(n)]
        res = find_max_subarray(a, n)
        write_f('../txtf/output.txt', res)
def test_time():
    t_start = time.perf_counter()
    main()
    t_start = time.perf_counter()
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
