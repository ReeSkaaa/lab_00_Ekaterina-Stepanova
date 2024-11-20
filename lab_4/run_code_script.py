import subprocess
import os

# запуск третьей лабы
tasks = ['1', '2', '3', '5', '6', '7']
for i in tasks:
    print(' ')
    print('######## Lab_3', f'Task_{i}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), f'Task_{i}', 'src', 'main.py'))
    subprocess.run("python " + PATH, shell=True)
