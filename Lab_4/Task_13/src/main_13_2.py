# 13.2
from Lab_4.utils import read_f, write_f


class Queue:
    """Класс реализует очередь"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = 3

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size >= self.max_size

    def enqueue(self, value):
        if self.isFull():
            print('Очередь заполнена!')
        new_node = [value, None]
        if self.tail:
            self.tail[1] = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail
        self.size += 1
        return self.head, self.tail, self.size

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        value = self.head[0]  # Получаем значение из начала очереди
        self.head = self.head[1]  # Сдвигаем указатель начала
        if not self.head:  # Если очередь опустела
            self.tail = None
        self.size -= 1
        return value

    def output(self):
        answer = []
        current = self.head
        while current:
            answer.append(str(current[0]) + " -> ")
            current = current[1]
        answer.append("None")
        return answer


if __name__ == "__main__":
    data = read_f(13)
    result = []
    data_push = list(map(int, data[0].split()))
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    result.append("Размер очереди: " + str(q.size))
    q.output()
    first_element = q.dequeue()
    result.append("Удаленный элемент: " + str(first_element))
    q.output()
    result.append("Размер очереди: " + str(q.size))
    result.append(q.output())
    write_f(13, result)
