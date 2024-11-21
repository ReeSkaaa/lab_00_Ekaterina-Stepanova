from lab_1.Task_1.src.main import insertion_sort
import tracemalloc
import timeit
import unittest


class TestInsertionSort(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [[2, 3, 1], 3]
        # when

        tracemalloc.start()
        result = insertion_sort(data[0], int(data[1]))
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))

        # given
        b = 256
        data = [[31, 41, 59, 26, 41, 58], 6]
        # when

        tracemalloc.start()
        result = insertion_sort(data[0], int(data[1]))
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
    data = [[2, 3, 1], 3]
    # when

    start_time = timeit.default_timer()
    result = insertion_sort(data[0], int(data[1]))
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 2
    data = [[31, 41, 59, 26, 41, 58], 6]
    # when

    start_time = timeit.default_timer()
    result = insertion_sort(data[0], int(data[1]))
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))


def test_should_insertion_sort(self):
    # given

    expected_result = [1, 2, 3]
    data = [[2, 3, 1], 3]
    # when

    result = insertion_sort(data[0], int(data[1]))
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = [26, 31, 41, 41, 58, 59]
    data = [[31, 41, 59, 26, 41, 58], 6]
    # when

    result = insertion_sort(data[0], int(data[1]))
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = [1, 2]
    data = [[1, 2], 2]
    # when

    result = insertion_sort(data[0], int(data[1]))
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
