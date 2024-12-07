from Lab_6.utils import read_f, write_f


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [y for y in arr[1:] if y > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def sort_items(s):
    result = []
    for key, value in s.items():
        result.append((key, value))
    return quicksort(result)

def do_task(n, a, s):
    for i in range(n):
        name, count = a[i].split()
        if name in s:
            s[name] += int(count)
        else:
            s[name] = int(count)

    ans = sort_items(s)
    return ans


if __name__ == "__main__":
    data = read_f(5)
    s = {}
    n = len(data)
    res = do_task(n, data, s)
    write_f(5, *res)
