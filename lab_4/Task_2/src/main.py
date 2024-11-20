import random
from lab_4.utils import read_f, write_f

PATH = '../txtf/input.txt'
OUTPUT_PATH = '../txtf/output.txt'


def queue_func(commands):
    queue = []
    front_index = 0
    res = []
    for command in commands:
        if command[0] == "+":
            queue.append(int(command[1]))
        elif command[0] == "-":
            res.append(str(queue[front_index]) + "\n")
            front_index += 1

    return res

if __name__ == "__main__":
    read = read_f(2)
    res = queue_func(read[1:])
    print(res)


