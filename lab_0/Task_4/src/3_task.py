import time

from memory_profiler import profile

t_start = time.perf_counter()

PATH = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

@profile
def main():
    def fib(n):
        f_prev = 0
        f_new = 1
        for k in range(n):
            f_prev, f_new = f_new, f_new + f_prev
        return f_prev

    def last_digit():
        ans = fib(n) % 10
        return ans

    f1 = open('../../input.txt', 'r')
    n = int(f1.readline())
    f1.close()
    if 0 <= n <= 10 ** 7:
        f2 = open('../../output.txt', 'w')
        f2.write(str(last_digit()))
        f2.close()
    else:
        quit('Введите еще раз')


if __name__ == '__main__':
    main()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
