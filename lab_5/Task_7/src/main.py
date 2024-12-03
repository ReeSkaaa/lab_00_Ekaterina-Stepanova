from lab_5.utils import read_f, write_f


def heapify(data, n, i):
    largest_root = i  # инициализируем как корень
    left_ind = 2 * i + 1
    right_ind = 2 * i + 2
    if left_ind < n and data[left_ind] < data[largest_root]:
        largest_root = left_ind
    if right_ind < n and data[right_ind] < data[largest_root]:
        largest_root = right_ind
    if largest_root != i:
        data[i], data[largest_root] = data[largest_root], data[i]  # Swap
        heapify(data, n, largest_root)


def do_heapSort(data):
    n = len(data)

    # Построим кучу (переупорядочить массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    # По одному извлекаем элемент из кучи
    for i in range(n - 1, 0, -1):
        # Переместим корень в конец
        data[0], data[i] = data[i], data[0]

        # Вызовем max heapify на уменьшенной куче
        heapify(data, i, 0)


def get_answer(arr):
    result = ''
    for i in arr:
        result += str(i) + ' '
    return result


if __name__ == "__main__":
    data = read_f(7)
    data = list(map(int, data[0].split()))
    do_heapSort(data)
    r = get_answer(data)
    write_f(7, r)
