from lab_2.Task_6.src.task_6 import find_max_subarray
import time
from lab_2.Task_6.utils import read_f, write_f


def main():
    if __name__ == "__main__":
        read = read_f('../txtf/input.txt')
        a = read[0]
        s = find_max_subarray(a, 0, len(a) - 1)
        write_f('../txtf/output.txt', s)


def test_time():
    t_start = time.perf_counter()
    main()
    t_start = time.perf_counter()
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
