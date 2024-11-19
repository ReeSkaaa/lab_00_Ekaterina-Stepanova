from lab_1.Task_4.src.main import lin_searh
from lab_1.utils import read_f, write_f
import timeit
import tracemalloc
import unittest


def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    n, read, elem = read_f(4)
    data = list(map(int, read.split()))
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    result = lin_searh(data, int(n), int(elem))
    result = list(result)
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestStringMethods(unittest.TestCase):
    def test_should_insertion_sort(self):
        # given
        expected_result = (1, [0])
        data = [[1, 2, 3], 3, 1]

        # when
        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = (2, [3, 4])
        data = [[1, 2, 3, 7, 7, 5], 6, 7]

        # when
        start_time = timeit.default_timer()
        result = lin_searh(data[0], data[1], data[2])
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
