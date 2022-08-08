'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/07/26
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''
    
    

import re
from collections import Counter
from tkinter import *
from tkinter import Tk, ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from widgets import crLabel, crText, crButton, open_text_file



def addPage1(Osn):
    page1 = Frame(Osn)
    label1 = crLabel(page1, "Выбрать файл для исследования:", 0, 0)

    # open text window
    nameFile = crText(page1, KolStepX =1, KolStepY=0, Kwidth=2, Kheigh=7)
    # open file button
    func = lambda: open_text_file(nameFile)
    open_button = crButton(page1, nameFile, func, 3, 0)

    
    label2 = crLabel(page1, "Установите характеристики файла.",1, 3)
    
    label3 = crLabel(page1, "Тематика файла",0, 4)
    TemaSource = crText(page1, KolStepX =0, KolStepY=5, Kwidth=2, Kheigh=7)
    
    
    label4 = crLabel(page1, "Описание источника файла",0, 8)
    DescSource = crText(page1, KolStepX =0, KolStepY=9, Kwidth=2, Kheigh=7)
    label5 = crLabel(page1, "Ссылка на источник файла",0, 12)
    HrefSource = crText(page1, KolStepX =0, KolStepY=13, Kwidth=2, Kheigh=7)
    Osn.add(page1, text='  Начальные установки  ')
    return page1

    
    
if __name__ == '__main__':
    root = Tk()
    root.title("Разделение сплошного потока символов")
    root.geometry("1200x700")
    # Начальные установки

    Osn = ttk.Notebook()
    addPage1(Osn)
    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)
    root.mainloop()