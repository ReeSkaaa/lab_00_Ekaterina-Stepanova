from lab_1.Task_3.src.task_3 import insertion_sort, main
import timeit
def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_isertion_sort():
    assert insertion_sort([1, 2, 3], 3) ==[3, 2, 1]
    assert insertion_sort([100, -10000, 1, 2, 3, 4, 9], 7) == [100, 9, 4, 3, 2, 1, -10000]
    assert insertion_sort([1], 1) == [1]
    assert insertion_sort([2, 1, 100, 5, -100,  7], 6) == [100, 7, 5, 2, 1, -100]