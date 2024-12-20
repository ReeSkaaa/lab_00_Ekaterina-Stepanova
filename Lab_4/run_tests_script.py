import subprocess
import os


def run_4_lab_tests():
    "Функция для запуска тестов 4 лабы"
    tasks = ['2', '4', '6', '7', '8']
    for i in tasks:
        print(' ')
        print('######## Lab_4', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'tests', 'test.py'))
        subprocess.run("python " + PATH, shell=True)
    print(' ')
    print('######## Lab_4', f'Task_{13}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{13}', 'tests', 'test_13_1.py'))
    subprocess.run("python " + PATH, shell=True)
    print(' ')
    print('######## Lab_4', f'Task_{13}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{13}', 'tests', 'test_13_2.py'))
    subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_4_lab_tests()
