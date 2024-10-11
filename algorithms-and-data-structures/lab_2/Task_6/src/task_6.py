import time
from memory_profiler import profile

@profile()
def find_max_subarray(a, low, high):
    if high == low:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        (leftlow, lefthigh, leftsum) = find_max_subarray(a, low, mid)
        (rightlow, righthigh, rightsum) = find_max_subarray(a, mid + 1, high)
        (crosslow, crosshigh, crosssum) = find_max_crossing_subarray(a, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)


def find_max_crossing_subarray(a, low, mid, high):
    leftsum = -10 ** 10
    maxleft, maxright = 0, 0
    sum = 0
    for i in range(mid, low, -1):
        sum += a[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -10 ** 10
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += a[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return (maxleft, maxright, leftsum + rightsum)


t_start = time.perf_counter()
if __name__ == "__main__":
    f1 = open('../txtf/input.txt', 'r')
    a = list(map(int, f1.readline().split()))
    f1.close()
    f2 = open('../txtf/output.txt', 'w')
    f2.write(str("Name: Gazprom" + '\n'))
    f2.write(str("Period under review: March 2024" + '\n'))
    start, end, sum = find_max_subarray(a, 0, len(a) - 1)
    f2.write('Day start: ' + str(start) + '\n')
    f2.write('Day end: ' + str(end) + '\n')
    f2.write('Max_sum: ' + str(sum))
t_start = time.perf_counter()
print("Время работы: %s секунд" % (time.perf_counter() - t_start))
