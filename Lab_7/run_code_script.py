import subprocess
import os


def run_7_lab_tasks():
    "Функция для запуска заданий 7 лабы"
    tasks = ['1', '3', '4', '6']
    for i in tasks:
        print(' ')
        print('######## Lab_7', f'Task_{i}', '###########################################################')
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'src', 'main.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_7_lab_tasks()
