from lab_2.Task_7.src.main import find_max_subarray
import timeit
import unittest
import tracemalloc


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [-1, -2, -3]
        # when

        tracemalloc.start()
        res = find_max_subarray(data, len(data) - 1)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given
        b = 256
        data = [2, -1, 2, 3, -9]
        # when

        tracemalloc.start()
        res = find_max_subarray(data, len(data) - 1)
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
        data = [-1, -2, -3]
        # when

        start_time = timeit.default_timer()
        res = find_max_subarray(data, len(data) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [2, -1, 2, 3, -9]
        # when

        start_time = timeit.default_timer()
        res = find_max_subarray(data, len(data) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should__max_subarray(self):
    # given

    data = [-1, -2, -3]
    expected_result = 5
    # when

    res = find_max_subarray(data, len(data) - 1)
    result = res[0]
    # then

    self.assertEqual(result, expected_result)

    # given

    data = [2, -1, 2, 3, -9]
    expected_result = 6
    # when

    res = find_max_subarray(data, len(data) - 1)
    result = res[0]
    # then

    self.assertEqual(result, expected_result)


def test_should_no_max_subarray(self):
    # given

    data = [-1, -2, -3]
    expected_result = 0
    # when

    res = find_max_subarray(data, len(data) - 1)
    result = res[0]
    # then

    self.assertEqual(result, expected_result)
