import time
from memory_profiler import profile

t_start = time.perf_counter()


@profile()
def lin_searh(a, n, v):
    res = []
    k = 0
    for i in range(0, n):
        if a[i] == v:
            k += 1
            res.append(i)
    return k, res


if __name__ == '__main__':
    f1 = open('../txtf/input.txt', 'r')
    f2 = open('../txtf/output.txt', 'w')
    n = int(f1.readline())
    a = list(map(int, f1.readline().split()))
    v = int(f1.readline())
    if (0 <= n <= 10 ** 3) and (-10 ** 3 <= min(a), max(a), v <= 10 ** 3):
        k, res = lin_searh(a, n, v)
        if k > 1:
            f2.write(f'{str(k)}\n')
            res = [*map(str, res)]
            for i in range(len(res) - 1):
                f2.write(f'{res[i]}, ')
            f2.write(f'{res[len(res) - 1]}')

        elif k == 1:
            f2.write(str(res[0]))
        else:
            f2.write(str(-1))
        f2.close()

else:
    print('Error.Try again')
f1.close()

t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
