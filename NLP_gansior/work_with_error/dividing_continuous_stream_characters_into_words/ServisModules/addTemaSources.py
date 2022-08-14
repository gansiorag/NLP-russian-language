'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''

import os
import sys

userPath = os.getcwd().split('NLP-russian-language')[0] + 'NLP-russian-language/NLP_gansior/work_with_error'
cprint(userPath, 'red')
sys.path.append(userPath)

import uuid 
from dividing_continuous_stream_characters_into_words.ModulesInterface.WorkWithDB import WorkDB
    
def WriteDB(tema):
    db = WorkDB()
    for nn in tema:
        guid = str(uuid.uuid3(uuid.NAMESPACE_DNS, nn))
        cprint(nn, 'red')
        dictRow = {'guidtema': guid, 'name_tema': nn }
        cprint(dictRow, 'green')
        db.InsertDataTb_Tema(dictRow)
        
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    tema=['Художествення литература - Проза', 'Художествення литература - Поэзия','Политическая литература', 'Медицинская литература']
    WriteDB(tema)
    prog2()