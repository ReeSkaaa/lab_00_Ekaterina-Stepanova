import subprocess
from colorama import Fore, Back, Style
import os

for i in range(1, 4):
    print(Fore.GREEN +'-------Запуск тестов для', f'lab_{i}', '------------------------------------------' + Style.RESET_ALL)
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'lab_{i}', 'run_tests_script.py'))
    subprocess.run("python " + PATH, shell=True)
