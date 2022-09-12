'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/07/26
Ending 2022//
    
'''
    
from pydoc import ispath
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''

import re
from collections import Counter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

import os
import sys

nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)

from ModulesInterface.page2 import Page2
from ModulesInterface.page1 import Page1
from ModulesInterface.baseModul import geomPar

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
    root.geometry(geomPar['rootGeometry'])
    # Начальные установки
    widthLabe = geomPar['widthLabe']
    widthBt = geomPar['widthBt']
    heighY = geomPar['heighY']

    Osn = ttk.Notebook(root)
    page1 = Page1(Osn)
    page2 = Page2(Osn, page1)
    page3 = addPage3(Osn)

    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)

    root.mainloop()
