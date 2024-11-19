from lab_2.Task_4.src.main import binary_search
import timeit
import time
import tracemalloc
from lab_2.utils import read_f
import unittest


def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given
    _, read, search_elem = read_f(4)
    data = list(map(int, read.split()))
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()

    result = binary_search(data, int(search_elem))
    end_time = timeit.default_timer()
    # then

    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestStringMethods(unittest.TestCase):
    def test_should_no_elem_binary_search(self):
        # given
        expected_result = -1
        data = [[1, 1, 2], 6]

        # when
        start_time = time.perf_counter()
        result = binary_search(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")
        # then
        self.assertEqual(result, expected_result)

    def test_should_binary_search(self):
        # given
        expected_result = 0
        data = [[0, 1], 0]

        # when
        start_time = time.perf_counter()
        result = binary_search(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = 1
        data = [[1, 2, 3], 2]

        # when
        start_time = time.perf_counter()
        result = binary_search(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = 3
        data = [[10, 10, 1, 11, 11], 11]

        # when
        start_time = time.perf_counter()
        result = binary_search(data[0], data[1])
        end_time = time.perf_counter()
        print(f"Время работы: {end_time - start_time:.4f} секунд")

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
