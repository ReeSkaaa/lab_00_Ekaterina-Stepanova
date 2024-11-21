from lab_1.Task_3.src.main import insertion_sort
import timeit
import unittest
import tracemalloc


class TestStringMethods(unittest.TestCase):

    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given

        b = 256
        data = [[100, -10000, 1, 2, 3, 4, 9], 7]
        # when

        tracemalloc.start()
        result = insertion_sort(data[0], data[1])
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [[2, 3, 1], 3]
        # when

        tracemalloc.start()
        result = insertion_sort(data[0], data[1])
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
    result = insertion_sort(data[0], data[1])
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))

    # given

    b = 2
    data = [[100, -10000, 1, 2, 3, 4, 9], 7]
    # when

    start_time = timeit.default_timer()
    result = insertion_sort(data[0], data[1])
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))


def test_should_insertion_sort(self):
    # given

    expected_result = [3, 2, 1]
    data = [[2, 3, 1], 3]
    # when

    result = insertion_sort(data[0], data[1])
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = [100, 9, 4, 3, 2, 1, -10000]
    data = [[100, -10000, 1, 2, 3, 4, 9], 7]
    # when

    result = insertion_sort(data[0], data[1])
    # then

    self.assertEqual(result, expected_result)

    # given
    expected_result = [100, 7, 5, 2, 1, -100]
    data = [[2, 1, 100, 5, -100, 7], 6]
    # when

    result = insertion_sort(data[0], data[1])
    # then

    self.assertEqual(result, expected_result)


def test_should_single_insertion_sort(self):
    # given

    expected_result = [1]
    data = [[1], 1]
    # when

    result = insertion_sort(data[0], data[1])
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
