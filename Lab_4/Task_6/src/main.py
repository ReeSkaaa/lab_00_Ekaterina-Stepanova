from collections import deque
from Lab_4.utils import read_f, write_f


def queue_with_minimal(commands):
    """Реализует работу очереди с минимумом"""
    answer = list()
    queue = deque()
    minimal_queue = deque()

    for char in commands:
        if char.startswith('+'):
            a, num = char.split()
            num = int(num)
            queue.append(num)

            while minimal_queue and minimal_queue[-1] > num:
                minimal_queue.pop()
            minimal_queue.append(num)

        elif char == '?':
            if minimal_queue != None:
                add = str(minimal_queue[0])
                answer.append(add)
        elif char == '-':
            if queue != None:
                if minimal_queue[0] == queue.popleft() and minimal_queue:
                    minimal_queue.popleft()

    return answer


if __name__ == "__main__":
    commands = read_f(6)
    M = commands[0]
    commands.pop(0)
    result = queue_with_minimal(commands)
    write_f(6, *result)
