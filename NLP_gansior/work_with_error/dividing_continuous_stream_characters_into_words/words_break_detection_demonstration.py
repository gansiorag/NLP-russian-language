'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/02/15
Ending 2022//
    
'''


from ModulesInterface.page2 import addPage2
from ModulesInterface.page1 import addPage1


import re
from collections import Counter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

# `Словарь сочетаний символов
# цифры определяют следующее
# Первая цифра количество символов с конца слова
# Вторая цифра количество сиволов с начала слова
# количество сочетаний до трех символов
# 33, 32, 31, 23, 22, 21, 13, 12, 11
# примеры возникновения сочетаний
#
#
#

import sys
import os

userPath = os.getcwd().split(
    'NLP-russian-language')[0] + 'NLP-russian-language/'
sys.path.append(userPath)





def addPage3(Osn):
    page3 = Frame(Osn)
    Osn.add(page3, text='  Исправление ошибок в словаре  ')
    return page3


if __name__ == '__main__':
    """
    Get list of documents and work with them.
    Result - file csv with two fields field one - six simbols - [xxxxxx] field two - [xxx xxx]

    """

    root = Tk()
    root.title("Разделение сплошного потока символов")
    root.geometry("1050x700")
    # Начальные установки
    widthLabe = 500
    widthBt = 300
    heighY = 10

    Osn = ttk.Notebook()
    page1 = addPage1(Osn)
    page2 = addPage2(Osn, heighY)
    page3 = addPage3(Osn)

    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)

root.mainloop()
