from lab_2.Task_6.src.main import find_max_subarray
import timeit
from lab_2.utils import read_f
import tracemalloc
import unittest
class TestStringMethods(unittest.TestCase):
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [0, 121, -2, 1, 4, 2, -1, 0, 0, 9, 10, -5, 2, 3, -2, -2, -4, 1, -1, 1, -1, 0, -1]
        # when

        start_time = timeit.default_timer()
        result = find_max_subarray(data, 0, len(data) - 1)
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
        data = [0, 121, -2, 1, 4, 2, -1, 0, 0, 9, 10, -5, 2, 3, -2, -2, -4, 1, -1, 1, -1, 0, -1]
        # when

        tracemalloc.start()
        result = find_max_subarray(data, 0, len(data) - 1)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))