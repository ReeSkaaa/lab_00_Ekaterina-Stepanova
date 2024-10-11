import time
from memory_profiler import profile


@profile

def majority_element(a, n):
    count_map = {}
    for num in a:
        if num in count_map:
            count_map[num] += 1
            if count_map[num] > n // 2:
                return 1
        else:
            count_map[num] = 1
    return 0

t_start = time.perf_counter()
if __name__ == "__main__":
    f1 = open('../txtf/input.txt', 'r')
    n = int(f1.readline())
    if 1 <= n <= 10 ** 5:
        a = list(map(int, f1.readline().split()))
        f2 = open('../txtf/output.txt', 'w')
        f2.write(str(majority_element(a, n)))
        f2.close()
    else:
        print('Error. Try again')
    f1.close()
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
