import subprocess
import os


def run_6_lab_tasks():
    "Функция для запуска заданий 5 лабы"
    tasks = ['1', '2', '5', '6', '8']
    for i in tasks:
        print(' ')
        print('######## Lab_6', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'src', 'main.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_6_lab_tasks()
