import subprocess
import os


def run_6_lab_tests():
    "Функция для запуска тестов 5 лабы"
    tasks = ['1', '2', '5', '6', '8']
    for i in tasks:
        print(' ')
        print('######## Lab_5', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'tests', 'test.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_6_lab_tests()
