from lab_1.Task_6.src.main import bubble_sort
import timeit
import unittest
import tracemalloc
from lab_1.utils import read_f


def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given

    read = read_f(6)
    data = list(map(int, read[0].split()))
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    result = [*map(str, bubble_sort(data))]
    end_time = timeit.default_timer()
    # then
    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestStringMethods(unittest.TestCase):
    def test_should_single_bubble_sort(self):
        # given
        expected_result = [1]
        data = [1]

        # when
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

    def test_should_bubble_sort(self):
        # given
        expected_result = [1, 2, 3, 4, 5]
        data = [1, 2, 3, 4, 5]

        # when
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = [1, 1, 2, 3, 7, 8]
        data = [7, 8, 1, 2, 3, 1]

        # when
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)

    def test_should_empty_bubble_sort(self):
        # given
        expected_result = []
        data = []

        # when
        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        print("Время работы программы:", end_time - start_time)

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
