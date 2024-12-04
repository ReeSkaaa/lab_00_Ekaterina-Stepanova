from lab_6.utils import read_f, write_f




def sort(s):
    answer = sorted(s.items(), key=lambda x: x[0])
    return answer


def do_task(n, a, s):
    for i in range(n):
        name, count = a[i].split()
        if name in s:
            s[name] += int(count)
        else:
            s[name] = int(count)

    ans = sort(s)
    return ans


if __name__ == "__main__":
    data = read_f(5)
    s = {}
    n = len(data)
    res = do_task(n, data, s)
    write_f(5, *res)
