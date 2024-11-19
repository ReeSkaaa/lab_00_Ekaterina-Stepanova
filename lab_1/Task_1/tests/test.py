from lab_1.Task_1.src.main import insertion_sort
from lab_2.utils import read_f
import tracemalloc
import timeit
import unittest


def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    n, read = read_f(1)
    data = list(map(int, read.split()))
    # when

    start_time = timeit.default_timer()
    tracemalloc.start()
    result = insertion_sort(data, int(n))
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestInsertionSort(unittest.TestCase):
    def test_should_insertion_sort(self):
        # given
        expected_result = [1, 2, 3]
        data = [[2, 3, 1], 3]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [26, 31, 41, 41, 58, 59]
        data = [[31, 41, 59, 26, 41, 58], 6]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [1, 2]
        data = [[1, 2], 2]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], int(data[1]))
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
