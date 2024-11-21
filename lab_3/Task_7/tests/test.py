from lab_3.Task_7.src.main import get_answer
import timeit
import tracemalloc
import unittest


class TestStringMethods(unittest.TestCase):
    def test_should_memory(self):
        "Функция для теста затрат памяти"
        # given
        b = 256
        data = ['3 3 1', 'bab', 'bba', 'baa']
        # when

        tracemalloc.start()
        result = get_answer(data)
        tracemalloc.stop()
        a = tracemalloc.get_traced_memory()[1] / 2 ** 20
        # then

        if not a <= b:
            standardMsg = 'Превышен лимит памяти'
            self.fail(self._formatMessage(standardMsg))
        # given

        b = 256
        data = ['3 3 1', 'bab', 'bba', 'baa']
        # when

        tracemalloc.start()
        result = get_answer(data)
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
    data = ['3 3 1', 'bab', 'bba', 'baa']
    # when

    start_time = timeit.default_timer()
    result = get_answer(data)
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))
    # given

    b = 2
    data = ['3 3 2', 'bab', 'bba', 'baa']
    # when

    start_time = timeit.default_timer()
    result = get_answer(data)
    end_time = timeit.default_timer()
    a = end_time - start_time
    # then

    if not a <= b:
        standardMsg = 'Превышен лимит времени'
        self.fail(self._formatMessage(standardMsg))


def test_should_check_get_answer(self):
    # given

    expected_result = '2 3 1\n'
    data = ['3 3 1', 'bab', 'bba', 'baa']
    # when

    result = get_answer(data)
    end_time = timeit.default_timer()
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = '3 2 1\n'
    data = ['3 3 2', 'bab', 'bba', 'baa']
    # when

    result = get_answer(data)
    # then

    self.assertEqual(result, expected_result)
    # given

    expected_result = '2 3 1\n'
    data = ['3 3 3', 'bab', 'bba', 'baa']
    # when

    result = get_answer(data)
    # then

    self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
