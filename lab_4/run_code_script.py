import subprocess
import os


def run_4_lab_tasks():
    "Функция для запуска заданий 4 лабы"
    tasks = ['2','4', '6', '7', '8']
    for i in tasks:
        print(' ')
        print('######## Lab_4', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'src', 'main.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_4_lab_tasks()
