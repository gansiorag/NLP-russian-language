'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/07/26
Ending 2022//
    
'''

import sys
import os
from tkinter import Tk, ttk, BOTH
from tkinter import Frame, END
from ModulesInterface.widgets import crListBox, MenuTypeSources
from ModulesInterface.widgets import crLabel, crText, crButton, open_text_file
from ModulesInterface.baseModul import var_sit
from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue 
on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
'''


# nameProject = 'ModulesInterface'
nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error/' +\
    'dividing_continuous_stream_characters_into_words'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)


class Page1(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.Osn = parent
        self.page1 = Frame(parent)
        # label1 = crLabel(self.page1, "Выбрать файл для исследования:", 0, 0)

        # open text window
        self.nameFile = crText(self.page1,
                               KolStepX=1,
                               KolStepY=0,
                               Kwidth=2,
                               Kheigh=7)

        # open file button
        self.func = lambda: open_text_file(self.nameFile)
        self.open_button = crButton(self.page1, self.nameFile, self.func, 3, 0)

        self.label2 = crLabel(
            self.page1, "Установите характеристики файла.", 1, 3)

        self.label3 = crLabel(self.page1, "Тематика файла", 0, 4)
        self.TemaSource = crListBox(self.page1, MenuTypeSources, 0, 6, 1, 2)
        # TemaSource = crText(page1, KolStepX =0, KolStepY=5,
        # Kwidth=2, Kheigh=7)

        self.label4 = crLabel(self.page1, "Описание источника файла", 0, 8)
        self.DescSource = crText(
            self.page1, KolStepX=0, KolStepY=9, Kwidth=2, Kheigh=7)
        self.label5 = crLabel(self.page1, "Ссылка на источник файла", 0, 12)
        self.HrefSource = crText(
            self.page1, KolStepX=0, KolStepY=13, Kwidth=2, Kheigh=7)
        var_sit['name_file'] = self.nameFile.get("1.0", END).strip()
        print()
        print('Page1', var_sit)
        print()
        # self.Osn.add(self.page1, text=zag)


if __name__ == '__main__':
    root = Tk()
    root.title("Разделение сплошного потока символов")
    root.geometry("1200x700")
    # Начальные установки

    Osn = ttk.Notebook()
    PageOne = Page1(Osn)
    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)
    print(Osn.widgetName)  # .nametowidget['page1'])
    # Osn.page1.open_button.bind('<Button-1>', event_info)
    root.mainloop()
