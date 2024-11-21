from lab_1.Task_6.src.main import bubble_sort
import timeit
import unittest
import tracemalloc


class TestStringMethods(unittest.TestCase):

    
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [1, 2, 3, 4, 5]
        # when

        tracemalloc.start()
        result = bubble_sort(data)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [7, 8, 1, 2, 3, 1]
        # when

        tracemalloc.start()
        result = bubble_sort(data)
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
        data = [1, 2, 3, 4, 5]
        # when

        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [7, 8, 1, 2, 3, 1]
        # when

        start_time = timeit.default_timer()
        result = bubble_sort(data)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


def test_should_single_bubble_sort(self):
    # given

    expected_result = [1]
    data = [1]
    # when

    result = bubble_sort(data)

    # then

    self.assertEqual(result, expected_result)


def test_should_bubble_sort(self):
    # given

    expected_result = [1, 2, 3, 4, 5]
    data = [1, 2, 3, 4, 5]
    # when

    result = bubble_sort(data)
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = [1, 1, 2, 3, 7, 8]
    data = [7, 8, 1, 2, 3, 1]
    # when

    result = bubble_sort(data)
    # then

    self.assertEqual(result, expected_result)


def test_should_empty_bubble_sort(self):
    # given

    expected_result = []
    data = []

    # when

    result = bubble_sort(data)
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
