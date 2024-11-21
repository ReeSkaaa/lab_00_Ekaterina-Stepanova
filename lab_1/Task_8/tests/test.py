from lab_1.Task_8.src.main import mister_swap
import tracemalloc
import timeit
import unittest

class TestStringMethods(unittest.TestCase):
    def test_should_time(self):
        "Функция для теста затрат времени"
        # given

        b = 2
        data = [3, 1, 4, 2, 2]
        n = 5
        # when

        start_time = timeit.default_timer()
        result = mister_swap(data, n)
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
        data = [3, 1, 4, 2, 2]
        n = 5
        # when

        tracemalloc.start()
        result = mister_swap(data, n)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))

