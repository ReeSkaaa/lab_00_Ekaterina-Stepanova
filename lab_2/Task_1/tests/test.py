from lab_2.Task_1.src.main import merge_sort
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [1, 2, 3]
        # when

        tracemalloc.start()
        result = merge_sort(data, 0, len(data) - 1)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [1, 3, 2]
        # when

        tracemalloc.start()
        result = merge_sort(data, 0, len(data) - 1)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))

        # given
        b = 2
        data = [1, 2, 4, 5, 3, 8]
        # when

        tracemalloc.start()
        result = merge_sort(data, 0, len(data) - 1)
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
        data = [1, 2, 3]
        # when

        start_time = timeit.default_timer()
        result = merge_sort(data, 0, len(data) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [1, 3, 2]
        # when

        start_time = timeit.default_timer()
        result = merge_sort(data, 0, len(data) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [1, 2, 4, 5, 3, 8]
        # when

        start_time = timeit.default_timer()
        result = merge_sort(data, 0, len(data) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should_empty_massive(self):
    # given

    data = []
    expected_result = None

    # when

    result = merge_sort(data, 0, len(data) - 1)

    # then

    self.assertEqual(None, result)


def test_should_already_sorted(self):
    # given

    data = [1, 2, 3, 4]
    expected_result = [1, 2, 3, 4]

    # when

    result = merge_sort(data, 0, len(data) - 1)
    # then

    self.assertEqual(result, expected_result)


def test_should_merge_sort(self):
    # given

    data = [12, 11, 13, 5, 6, 7]
    expected_result = [5, 6, 7, 11, 12, 13]
    # when

    result = merge_sort(data, 0, len(data) - 1)
    # then

    self.assertEqual(result, expected_result)


def test_should_reverse_sorted(self):
    # given

    data = [4, 3, 2, 1]
    expected_result = [1, 2, 3, 4]
    # when

    result = merge_sort(data, 0, len(data) - 1)
    # then

    self.assertEqual(result, expected_result)


def test_should_large_numbers(self):
    # given

    data = [1000000000, 9999998, 1000000000]
    expected_result = [9999998, 1000000000, 1000000000]
    # when

    result = merge_sort(data, 0, len(data) - 1)

    # then
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
