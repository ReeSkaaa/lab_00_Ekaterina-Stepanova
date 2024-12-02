from lab_4.utils import read_f, write_f


def do_queue(data):
    h = 0
    queue = list()
    ans = list()
    for char in data:
        if char == "-":
            ans += [queue[h]]
            h += 1
        else:
            queue += [int(char[1:])]
    return ans


if __name__ == "__main__":
    data = read_f(2)
    data.pop(0)
    result = do_queue(data)
    write_f(2, *result)
