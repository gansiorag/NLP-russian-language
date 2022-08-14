'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/08/01
Ending 2022//
    
'''
    
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
'''

import re
from collections import Counter
from tkinter import *
from tkinter import Tk, ttk
from tkinter import filedialog as fd
from tkinter import messagebox
    
session = {
'borderLeft':10,
'startY':20,
'HighLabel': 30,
'WidthLabel' : 300,
'widthBt' : 300,
'heighY' : 10 
}
import os
import sys

userPath = os.getcwd().split('NLP-russian-language')[0] + 'NLP-russian-language/NLP_gansior/work_with_error'
sys.path.append(userPath)

from dividing_continuous_stream_characters_into_words.ModulesInterface.WorkWithDB import WorkDB

MenuTypeSources =[nm[1] for nm in WorkDB.selectTypeSources()]
cprint(f'{MenuTypeSources}' , 'magenta', attrs=['bold'])


def crListBox(page:Frame, menu:list, KolStepX, KolStepY, ww, high) :
    listm = Listbox(page)
    listm.insert(0, *MenuTypeSources)
    sb = Scrollbar(listm, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    listm.configure(yscrollcommand=sb.set)
    sb.config(command=listm.yview)
    listm.place(x=session['borderLeft'] +10 + session['WidthLabel']*KolStepX, 
                 y=session['startY']+20+ session['HighLabel']*KolStepY, 
                 anchor="w", heigh=session['HighLabel']*high, width=session['WidthLabel']*ww, 
                 bordermode=OUTSIDE)
    return listm
 
def open_text_file(text:Text):
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('text files', '*.pdf'),
        ('text files', '*.doc'),
        ('text files', '*.docx'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfilename(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f)
     
    
def crLabel(page:Frame, textL:str, KolStepX:int, KolStepY:int):
    labelC = Label(page, text=textL)
    labelC.place(x=session['borderLeft']+ 
                 session['WidthLabel']*KolStepX, 
                 y=session['startY']+20+ session['HighLabel']*KolStepY, 
                 anchor="w", heigh=session['HighLabel'], width=session['WidthLabel'], 
                 bordermode=OUTSIDE)
    return labelC
    
def crText(page:Frame, KolStepX =1, KolStepY=1, Kwidth=1, Kheigh=1) :
    nameFile = Text(page)
    nameFile.place(x=session['borderLeft']+  session['WidthLabel']*KolStepX + 10, 
                   y=session['startY'] + session['HighLabel']* KolStepY +10, 
                   heigh=session['HighLabel']*Kwidth, 
                   width=session['WidthLabel']*Kwidth)    
    return nameFile

def crButton(page:Frame, text, func, KolStepX:int, KolStepY:int):
    open_button = Button(page, text='Open a File', command=func)
    open_button.place(x=session['borderLeft'] + KolStepX*(session['WidthLabel'] + 10), 
                      y=session['startY']+10 + session['HighLabel']* KolStepY, heigh=session['HighLabel'], width=session['WidthLabel'] /2)
    return open_button
        
if __name__ == '__main__':
    name=''
    # prog1()
    # prog2()


