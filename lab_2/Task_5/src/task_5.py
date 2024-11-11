from memory_profiler import profile
from lab_2.Task_5.utils import read_f, write_f

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

if __name__ == "__main__":
    read = read_f('../txtf/input.txt')
    n = read[0]
    if 1 <= n <= 10 ** 5:
        a = read[1]
        write_f('../txtf/output.txt', str(majority_element(a, n)))

