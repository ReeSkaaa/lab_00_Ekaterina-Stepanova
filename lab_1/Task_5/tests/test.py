from lab_1.Task_5.src.main import selection_sort
from lab_1.utils import read_f, write_f
import timeit
import unittest
import tracemalloc


def test_time_memory():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    n, read_res = read_f(5)
    data = list(map(int, read_res.split()))
    # when

    start_time = timeit.default_timer()
    tracemalloc.start()
    result = selection_sort(data, int(n))
    end_time = timeit.default_timer()
    # then

    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()
    print("Время работы программы:", end_time - start_time)


class TestStringMethods(unittest.TestCase):
    def test_should_selection_sort(self):
        # given
        expected_result = [1]
        data = [[1], 1]

        # when
        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [1, 2, 3]
        data = [[1, 3, 2], 3]

        # when
        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
