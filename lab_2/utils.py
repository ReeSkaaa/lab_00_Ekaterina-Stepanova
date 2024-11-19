import os
import time

def read_f(task):
    """
    Функция для чтения входных данных из файла 'input.txt'.

    """
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{task}', 'txtf', 'input.txt'))
    with open(PATH, 'r') as file:
        return [line.strip() for line in file.readlines()]


def write_f(task, *args):
    """
    Функция для записи выходных данных в файл 'output.txt'.

    """
    PATH_OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{task}', 'txtf', 'output.txt'))
    with open(PATH_OUTPUT, 'w') as file:
        for i in args:
            print(i, file=file)

