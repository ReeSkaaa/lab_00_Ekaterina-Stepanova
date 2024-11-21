from lab_1.Task_5.src.main import selection_sort
import timeit
import unittest
import tracemalloc


class TestStringMethods(unittest.TestCase):
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [[1], 1]
        # when

        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 2
        data = [[1, 3, 2], 3]
        # when

        start_time = timeit.default_timer()
        result = selection_sort(data[0], data[1])
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
    data = [[1], 1]
    # when

    tracemalloc.start()
    result = selection_sort(data[0], data[1])
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 256
    data = [[1, 3, 2], 3]
    # when

    tracemalloc.start()
    result = selection_sort(data[0], data[1])
    tracemalloc.stop()
    a = tracemalloc.get_traced_memory()[1] / 2 ** 20
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит памяти'
        self.fail(self._formatMessage(standardMsg))


def test_should_selection_sort(self):
    # given
    expected_result = [1]
    data = [[1], 1]

    # when
    start_time = timeit.default_timer()
    result = selection_sort(data[0], data[1])
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

    # then
    self.assertEqual(result, expected_result)

    # given
    expected_result = [1, 2, 3]
    data = [[1, 3, 2], 3]

    # when
    start_time = timeit.default_timer()
    result = selection_sort(data[0], data[1])
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

    # then
    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
