# 13.1
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
        tmp = self.stack
        if reverse:
            while tmp:
                print(tmp[-1], '----', end='')
                tmp = tmp[:-1]
        else:
            while tmp:
                print(tmp[0], '----', end='')
                tmp = tmp[1:]
        print('None')


# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

# Вывод стека
print("\nОбратный вывод:")
stack.output(reverse=True)

# Извлечение и вывод верхнего элемента стека
value = stack.pop()
print("Извлеченное значение:", value)

# Повторный вывод стека после извлечения элемента
stack.output(reverse=True)
