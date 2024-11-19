from lab_1.Task_3.src.main import insertion_sort
import timeit
import tracemalloc
import unittest
from lab_1.utils import read_f


def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    n, read = read_f(3)
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


class TestStringMethods(unittest.TestCase):
    def test_should_insertion_sort(self):
        # given
        expected_result = [3, 2, 1]
        data = [[2, 3, 1], 3]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [100, 9, 4, 3, 2, 1, -10000]
        data = [[100, -10000, 1, 2, 3, 4, 9], 7]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [100, 7, 5, 2, 1, -100]
        data = [[2, 1, 100, 5, -100, 7], 6]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

    def test_should_single_insertion_sort(self):
        # given
        expected_result = [1]
        data = [[1], 1]

        # when
        start_time = timeit.default_timer()
        result = insertion_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
