from lab_3.Task_1.src.main import quick_sort
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [0, -1, 2]
        # when

        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [10000, 200, 45, 23, 11, 76, 3, 1]
        # when

        start_time = timeit.default_timer()
        result = quick_sort(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should_memory(self):
    "Функция для теста затрат памяти"
    # given
    b = 256
    data = [1, 9, 2]
    # when

    tracemalloc.start()
    result = quick_sort(data)
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))

    # given
    b = 256
    data = [1, 3, 2, 5, 4, 10, 14, 56]
    # when

    tracemalloc.start()
    result = quick_sort(data)
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))


def test_should_no_elem_binary_search(self):
    # given

    expected_result = []
    data = []
    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_single_binary_search(self):
    # given

    expected_result = [1]
    data = [1]
    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_binary_search(self):
    # given

    expected_result = [1, 2, 9]
    data = [1, 9, 2]
    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)

    # given

    expected_result = [1, 2, 3, 4, 5]
    data = [1, 3, 2, 5, 4]
    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_long_binary_search(self):
    # given
    expected_result = [100, 200, 700, 8000, 9999999, 100000000000000000]
    data = [200, 100, 100000000000000000, 700, 8000, 9999999]

    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_sorted_binary_search(self):
    # given
    expected_result = [1, 2, 3]
    data = [1, 2, 3]
    # when

    result = quick_sort(data)
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
