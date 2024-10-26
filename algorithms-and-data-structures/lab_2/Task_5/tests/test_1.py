from lab_2.Task_5.src.task_5 import majority_element
import time
from lab_1.Task_9.utils import read_f, write_f


def main():
    if __name__ == "__main__":
        read = read_f('../txtf/input.txt')
        n = read[0]
        if 1 <= n <= 10 ** 5:
            a = read[1]
            write_f('../txtf/output.txt', str(majority_element(a, n)))


def test_time():
    t_start = time.perf_counter()
    main()
    t_start = time.perf_counter()
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))


def test_majority_elem():
    assert majority_element([1, 2, 3, 4], 4) == 0
    assert majority_element([7, 1, 1], 3) == 1
    assert majority_element([2, 3, 9, 2, 2], 5) == 1
