from lab_1.Task_9.src.main import binary_addition
import timeit
import unittest
import tracemalloc
from lab_1.utils import read_f


def test_time():
    "Функция для проверки затрат памяти и времени при данных, взятых пользователем из файла"
    # given
    read_ = read_f(9)
    read = read_[0].split()
    n1, n2 = read[0], read[1]
    n1 = [*map(int, n1)]
    n2 = [*map(int, n2)]
    # when
    start_time = timeit.default_timer()
    tracemalloc.start()
    binary_addition(n1, n2)
    end_time = timeit.default_timer()
    # then
    print("Время работы программы:", end_time - start_time)
    print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "mb")
    tracemalloc.stop()


class TestStringMethods(unittest.TestCase):
    def test_should_small_ex_binary_addition(self):
        # given
        expected_result = '11'
        data = [[1, 0], [0, 1]]

        # when
        result = binary_addition(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = '10'
        data = [[1], [1]]

        # when
        result = binary_addition(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)

    def test_should_bigger_data_binary_addition(self):
        # given
        expected_result = '1111'
        data = [[1, 1, 1, 0], [0, 0, 0, 1]]

        # when
        result = binary_addition(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = '100'
        data = [[1, 0, 0], [0, 0, 0]]

        # when
        result = binary_addition(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)

    def test_should_empty_binary_addition(self):
        # given
        expected_result = ''
        data = [[], []]

        # when
        result = binary_addition(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
