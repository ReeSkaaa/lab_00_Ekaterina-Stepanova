from Lab_5.utils import read_f, write_f
import heapq


def do_schedule(n, data):
    answer = []

    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    for task_time in data:
        free_time, thread_index = heapq.heappop(heap)
        answer.append((thread_index, free_time))
        heapq.heappush(heap, (free_time + task_time, thread_index))
    return answer


if __name__ == "__main__":
    a, data = read_f(5)
    a = list(map(int, a.split()))
    n, m = a[0], a[1]
    data = list(map(int, data.split()))
    result = do_schedule(n, data)
    answer = ''
    for i in result:
        answer += str(i[0]) + ' ' + str(i[1]) + '\n'
    write_f(5, answer)
