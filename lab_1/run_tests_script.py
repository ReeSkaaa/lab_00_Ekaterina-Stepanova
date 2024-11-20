import subprocess
import os


# запуск тестов первой лабы
tasks = ['1', '3', '4', '5', '6', '8', '9']
for i in tasks:
    print(' ')
    print('######## Lab_1', f'Task_{i}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'tests', 'test.py'))
    subprocess.run("python " + PATH, shell=True)

