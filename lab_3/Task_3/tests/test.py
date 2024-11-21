from lab_3.Task_3.src.main import scarecrow_sort
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given

        b = 256
        data = [2, 1, 3]
        n, k = 3, 2
        # when

        tracemalloc.start()
        result = scarecrow_sort(n, k, data)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = [1, 5, 3, 4, 1]
        n, k = 5, 3
        # when

        tracemalloc.start()
        result = scarecrow_sort(n, k, data)
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
        data = [2, 1, 3]
        n, k = 3, 2
        # when

        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [1, 5, 3, 4, 1]
        n, k = 5, 3
        # when

        start_time = timeit.default_timer()
        result = scarecrow_sort(n, k, data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should_no_scarecrow(self):
    # given
    expected_result = False
    data = [2, 1, 3]
    n, k = 3, 2
    # when

    result = scarecrow_sort(n, k, data)
    # then

    self.assertEqual(result, expected_result)


def test_should_scarecrow(self):
    # given
    expected_result = False
    data = [1, 5, 3, 4, 1]
    n, k = 5, 3

    # when

    result = scarecrow_sort(n, k, data)
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
