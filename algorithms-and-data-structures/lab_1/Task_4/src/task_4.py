from memory_profiler import profile
from lab_1.Task_4.utils import read_f


@profile()
def lin_searh(a, n, v):
    res = []
    k = 0
    for i in range(0, n):
        if a[i] == v:
            k += 1
            res.append(i)
    return k, res

def main():
    read_res = read_f('../txtf/input.txt')
    n = read_res[0]
    a = read_res[1]
    v = read_res[2]
    f2 = open('../txtf/output.txt', 'w')
    if (0 <= n <= 10 ** 3) and (-10 ** 3 <= v <= 10 ** 3):
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
