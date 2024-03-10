'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/07/26
Ending 2022//

'''
import os
import sys
from termcolor import cprint

# Text colors: grey red green yellow blue magenta cyan white
# Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
# Attributes: bold dark underline blink reverse concealed


from tkinter import Tk, BOTH
from tkinter import ttk, Frame


nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error/' +\
    'dividing_continuous_stream_characters_into_words/'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)
import ModulesInterface.baseModul as pmod
# import geom_par, var_sit
from add_pages import add_page

# try:
#     # from ModulesInterface.page2 import Page2
#     # from ModulesInterface.page1 import Page1
#     from ModulesInterface.add_pages import add_page
#     # from ModulesInterface.baseModul import geom_par, var_sit
# except Exception as e:
#     print(e)

# `Словарь сочетаний символов
# цифры определяют следующее
# Первая цифра количество символов с конца слова вот так симво - "лов"
# Вторая цифра количество сиволов с начала слова вот так "сим" - волов
# количество сочетаний до трех символов
# 33, 32, 31, 23, 22, 21, 13, 12, 11
# примеры возникновения сочетаний
#
#
#


if __name__ == '__main__':

    # Get list of documents and work with them.
    # Result - file csv with two fields field one - six simbols - [xxxxxx]
    # field two - [xxx xxx]

    root = Tk()
    root.title("Разделение сплошного потока символов")
    rxy = pmod.geom_par['rootGeometry']
    root.geometry(rxy)
    # Начальные установки
    widthLabe = pmod.geom_par['widthLabe']
    widthBt = pmod.geom_par['widthBt']
    heigh_y = pmod.geom_par['heigh_y']

    Osn = ttk.Notebook(root)
    add_page(Osn, 'page_start',  ' Начальные установки  ')
    add_page(Osn, 'page_pred_work', '  Предобработка источника  ')
    add_page(Osn, 'searches_sources', ' Исследование источника ')
    add_page(Osn, 'searches_dict', '  Исследование словаря  ')

    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)

    root.mainloop()
