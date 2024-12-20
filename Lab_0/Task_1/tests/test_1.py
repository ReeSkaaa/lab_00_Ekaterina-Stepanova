import time
from Lab_0.Task_2.src.main import main


def main():
    a, b = 7, 8
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
        print(a + b ** 2)


def test_time():
    t_start = time.perf_counter()
    main()
    t_start = time.perf_counter()
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
