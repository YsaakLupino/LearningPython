import pyautogui as py
import os


#renomear pastas (nome/path antigo, nome/path novo)
# os.rename('teste',
#            'mod')

class OSchanger():
    def __init__(self):
        pass
    def change_file_nem(self, path_to_change:str, logic_name:str ):
        PATH_TO_WORK = path_to_change #pasta a explorar
        DIR_LIST = os.listdir(PATH_TO_WORK)
        for n, y in enumerate(DIR_LIST,1):
            if y.find('.') > 0: #quais arquivos modificar
                new_name_logic = f'{logic_name}_0{n}.py' #nome do arquivo 
                path_to_change = rf'{PATH_TO_WORK}\{y}'
                print(path_to_change)
                path_new_name = rf'{PATH_TO_WORK}\{new_name_logic}'
                os.rename(path_to_change,path_new_name)
                
        return None




