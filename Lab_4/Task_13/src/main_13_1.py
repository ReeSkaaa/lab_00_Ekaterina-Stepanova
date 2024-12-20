# 13.1
from Lab_4.utils import read_f, write_f


class Stack:
    """Класс реализует стек"""

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, char):
        self.stack.append(char)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Error. Stack is empty")
        else:
            return self.stack.pop()

    def output(self, reverse=False):
        answer = []
        tmp = self.stack
        if reverse:
            while tmp:
                answer.append(str(tmp[-1]) + '----')
                tmp = tmp[:-1]
        else:
            while tmp:
                answer.append(str(tmp[0]) + '----'[0])
                tmp = tmp[1:]
        answer.append('None')

        return answer


if __name__ == "__main__":
    data = read_f(13)
    result = []
    data_push = list(map(int, data[0].split()))
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    result.append("Обратный вывод: " + str(stack.output(reverse=True)))
    value = stack.pop()
    result.append("Извлеченное значение: " + str(value))
    result.append(stack.output(reverse=True))
    write_f(13, *result)
