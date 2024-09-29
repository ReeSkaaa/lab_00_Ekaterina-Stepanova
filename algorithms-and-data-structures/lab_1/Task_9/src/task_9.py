import time
from memory_profiler import profile

t_start = time.perf_counter()


@profile()
def binary_addition(n1, n2):
    ans = []
    n1 = n1[::-1]
    n2 = n2[::-1]
    max_size = max(len(n2), len(n1))
    n1 += (max_size - len(n1)) * [0]
    n2 += (max_size - len(n2)) * [0]
    limit = 0
    for a in zip(n1, n2):
        add = a[0] + a[1] + limit
        limit = add // 2
        ans.append(add % 2)

    if limit == 1:
        ans.append(1)

    ans = ans[::-1]
    return ''.join(map(str, ans))


if __name__ == '__main__':
    f1 = open('../txtf/input_Task9.txt', 'r')
    n1, n2 = map(str, f1.readline().split())
    n1 = [*map(int, n1)]
    n2 = [*map(int, n2)]
    f2 = open('../txtf/output_Task9.txt', 'w')
    f2.write(binary_addition(n1, n2))
    f2.close()
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
