import time
from memory_profiler import profile


@profile
def main():
    a, b = open('../input.txt').read().split()
    a, b = int(a), int(b)
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
        open('../output.txt', 'w').write(str(a + b ** 2))
    else:
        quit('Введите еще раз')
if __name__ == '__main__':
    main()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
