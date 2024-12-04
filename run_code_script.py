import subprocess
from colorama import Fore, Back, Style
import os


def run_all_tasks():
    "Функция для запуска всех заданий"
    for i in range(1, 7):
        print(Fore.GREEN + '-------Запуск тестов для', f'lab_{i}',
              '------------------------------------------' + Style.RESET_ALL)
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'lab_{i}', 'run_code_script.py'))
        subprocess.run("python " + PATH, shell=True)

if __name__ == '__main__':
    run_all_tasks()