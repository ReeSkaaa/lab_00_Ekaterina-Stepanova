from Lab_6.utils import read_f, write_f

def iterativeFib(all_fib_num, n):
    a, b = 0, 1
    all_fib_num.add(a)
    all_fib_num.add(b)
    for i in range(n):
        a, b = b, a + b
        all_fib_num.add(a)
        all_fib_num.add(b)
    return all_fib_num

def fib_come_back(all_fib_num, n, data):
    answer = []
    for i in range(n):
        if data[i] in all_fib_num:
            answer.append('Yes')
        else:
            answer.append('No')
    return answer


if __name__ == "__main__":
    all_fib_num = set()
    data = read_f(6)
    n = int(data[0])
    data.pop(0)
    data = list(map(int, data))
    all_fib_num = iterativeFib(all_fib_num, 5000)
    result = fib_come_back(all_fib_num, n, data)
    write_f(6, *result)

