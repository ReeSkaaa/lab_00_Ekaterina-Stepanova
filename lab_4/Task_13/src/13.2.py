# 13.2

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
        current = self.head
        while current:
            print(current[0], end=" -> ")
            current = current[1]
        print("None")



q = Queue()

# Добавление элементов в очередь
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Проверка размера очереди
print("Размер очереди:", q.size)

# Отображение оставшихся элементов очереди
q.output()
# Удаление и вывод первого элемента очереди
first_element = q.dequeue()
print("Удаленный элемент:", first_element)

# Отображение оставшихся элементов очереди
q.output()
print("Размер очереди:", q.size)
