import subprocess
import os


# запуск тестов первой лабы
tasks = ['1', '3', '4', '5', '6', '8', '9']
for i in tasks:
    print(' ')
    print('######## Lab_1', f'Task_{i}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lab_1', f'Task_{i}', 'src', 'main.py'))
    subprocess.run("python " + PATH, shell=True)

# запуск тестов второй лабы
tasks = ['1', '3', '4', '5', '6', '7']
for i in tasks:
    print(' ')
    print('######## Lab_2', f'Task_{i}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lab_2', f'Task_{i}', 'src', 'main.py'))
    subprocess.run("python " + PATH, shell=True)

#запуск третьей лабы
tasks = ['1', '2', '3', '5', '6', '7']
for i in tasks:
    print(' ')
    print('######## Lab_3', f'Task_{i}', '###########################################################')
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lab_3', f'Task_{i}', 'src', 'main.py'))
    subprocess.run("python " + PATH, shell=True)
