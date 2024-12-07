import subprocess
from colorama import Fore, Style
import os


def run_all_tests():
    "Функция для запуска всех тестов"
    for i in range(1, 8):
        print(Fore.GREEN + '-------Запуск тестов для', f'lab_{i}',
              '------------------------------------------' + Style.RESET_ALL)
        PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'lab_{i}', 'run_tests_script.py'))
        subprocess.run("python " + PATH, shell=True)


if __name__ == '__main__':
    run_all_tests()
