from Lab_4.utils import read_f, write_f
from collections import deque


def sequence_maximum(n, data, m):
    """Находит максимум в движущейся последовательности"""
    answer = list()
    deque_indx = deque()
    for pos in range(0, n):
        if deque_indx and deque_indx[0] < (pos - m + 1):
            deque_indx.popleft()
        while deque_indx and data[deque_indx[len(deque_indx)-1]] <= data[pos]:
            deque_indx.pop()
        deque_indx.append(pos)
        if pos >= m - 1:
            add = data[deque_indx[0]]
            answer.append(add)

    return answer


if __name__ == "__main__":
    data = read_f(7)
    n = int(data[0])
    m = int(data[len(data) - 1])
    data.pop(0)
    data.pop(len(data) - 1)
    data = list(map(int, data[0].split()))
    res = sequence_maximum(n, data, m)
    write_f(7, *res)
