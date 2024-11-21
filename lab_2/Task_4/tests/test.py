from lab_2.Task_4.src.main import binary_search
import timeit
import time
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given

        b = 256
        data = [[1, 1, 2], 6]
        # when

        tracemalloc.start()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [[1, 1, 2], 6]

        # when

        tracemalloc.start()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20

        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [[1, 1, 2], 6]
        # when

        tracemalloc.start()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [[1, 1, 2, 1000, 1, 1, 2, 7], 1]

        # when

        tracemalloc.start()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20

        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))

    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [[1, 1, 2], 6]
        # when

        start_time = timeit.default_timer()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [[1, 1, 1, 1000, 20, 4], 0]
        # when

        start_time = timeit.default_timer()
        result = binary_search(data[0], data[1])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


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
