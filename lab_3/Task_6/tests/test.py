from lab_3.Task_6.src.main import get_result, quickSort, multiplication
import timeit
import tracemalloc
from lab_3.utils import read_f
import unittest
class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data1 = [7, 1, 4, 9]
        data2 = [2, 7, 8, 11]
       # when

        tracemalloc.start()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
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
        data1 = [7, 1, 4, 9]
        data2 = [2, 7, 8, 11]
        # when

        start_time = timeit.default_timer()
        c = multiplication(data1, data2)
        quickSort(c, 0, len(c) - 1)
        end_time = timeit.default_timer()
        a = end_time - start_time
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит времени'
            self.fail(self._formatMessage(standardMsg))


    def test_should_sort(self):
        # given
        expected_result = 51
        data1 = [7, 1, 4, 9]
        data2 = [2, 7, 8, 11]
        # when

        c = multiplication(data1, data2)
        quickSort(c, 0, len(c)-1)
        result = get_result(c)
        # then

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
