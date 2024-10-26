from lab_1.Task_4.src.task_4 import main, lin_searh
import timeit
def test_time():
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Время работы программы:", end_time - start_time)

def test_isertion_sort():
    assert lin_searh([1, 2, 3], 3, 1) == (1, [0])
    assert lin_searh([1, 2, 3, 7, 7, 5], 6, 7) == (2, [3, 4])

