from lab_2.Task_5.src.main import majority_element
import time
import tracemalloc
import timeit
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = [[1, 2, 3, 4], 4]
        # when

        tracemalloc.start()
        result = majority_element(data[0], data[1])
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
        data = [[1, 2, 3, 4], 4]
        # when

        start_time = timeit.default_timer()
        result = majority_element(data[0], data[1])
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))

    def test_should_majority_element(self):
        # given
        expected_result = 0
        data = [[1, 2, 3, 4], 4]

        # when
        result = majority_element(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)

        # given
        expected_result = 1
        data = [[7, 1, 1], 3]

        # when
        result = majority_element(data[0], data[1])

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
