import pyautogui as py
import os


#renomear pastas (nome/path antigo, nome/path novo)
# os.rename('teste',
#            'mod')
PATH_TO_WORK = r'D:\pinoso\programação\LearningPython\ExGuanabara'
DIR_LIST = os.listdir(PATH_TO_WORK)



for n, y in enumerate(DIR_LIST,1):
    print(y)
    if y[0] == 'e':
        new_name_logic = f'Ex_py0{n}.py'
        path_to_change = rf'{PATH_TO_WORK}\{y}'
        print(path_to_change)
        path_new_name = rf'{PATH_TO_WORK}\{new_name_logic}'
        os.rename(path_to_change,path_new_name)
