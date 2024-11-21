from lab_1.Task_9.src.main import binary_addition
import timeit
import unittest
import tracemalloc


class TestStringMethods(unittest.TestCase):
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [[1, 0], [0, 1]]
        # when

        start_time = timeit.default_timer()
        result = binary_addition(data[0], data[1])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))
            # given

        b = 2
        data = [[1, 0, 0], [0, 0, 0]]
        # when

        start_time = timeit.default_timer()
        result = binary_addition(data[0], data[1])
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
        data = [[1, 0], [0, 1]]
        # when

        tracemalloc.start()
        result = binary_addition(data[0], data[1])
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))

        # given
        b = 256
        data =  [[1, 0, 0], [0, 0, 0]]
        # when

        tracemalloc.start()
        result = binary_addition(data[0], data[1])
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))


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
