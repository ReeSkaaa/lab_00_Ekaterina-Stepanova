from lab_1.Task_5.src.task_5 import selection_sort, main
import timeit
def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_selection():
    assert selection_sort([1], 1) == [1]
    assert selection_sort([1, 3, 2], 3) == [1, 2, 3]
