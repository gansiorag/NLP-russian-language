"""_summary_

Returns:
    _type_: _description_
"""

import os
import sys
import re
from typing import Dict, ClassVar
from collections import Counter
from tkinter import Text, Label, Button, Frame, OUTSIDE, END
from datetime import datetime
import pickle
import json

from testFeuch import connectLearn, separatorWords
from ModulesInterface.baseModul import geom_par, var_sit
from ModulesInterface.page1 import Page1


nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error'
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
sys.path.append(PathPrj)
dd = dict()
dd = {33: {},
      32: {},
      31: {},
      23: {},
      22: {},
      21: {},
      13: {},
      12: {},
      11: {}
      }


def get_num(i: int):
    """ Get number

    Args:
        i (int): this number

    Returns:
        [str]: if number 1 - 9 returne 01 - 09
    """
    answer = ''
    if i < 10:
        answer = '0' + str(i)
    else:
        answer = str(i)
    return answer


class page_pred_work():

    def __init__(self, Osn) -> None:

        self.page1 = Page1(Osn)

        self.page2 = Frame(Osn)
        Osn.add(self.page2, text='  Разделение строки по словам  ')

        self.page2_label_Path3 = Label(self.page2, text="Результат")
        self.page2_label_Path3.place(
            x=1150, y=geom_par['heighY']+10,
            anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        self.page2_TextPath3 = Text(self.page2)
        self.page2_TextPath3.place(x=geom_par['P2widthW']*2 + 30,
                                   y=geom_par['heighY'] + 60,
                                   anchor="nw",
                                   heigh=500,
                                   width=geom_par['P2widthW'],
                                   bordermode=OUTSIDE)

        # First colunm =======================================================

        self.page2_label_Nom2_Slovo = Label(self.page2, text="Исходный текст")
        self.page2_label_Nom2_Slovo.place(
            x=120, y=geom_par['heighY']+10, anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        def func1(): return self.readAllSource()
        self.page2_read_bt = Button(
            self.page2, text="Прочитать весь файл", command=func1)
        self.page2_read_bt.place(
            x=10, y=geom_par['heighY'] + 40,
            anchor="w", heigh=30, width=170,
            bordermode=OUTSIDE)

        def func3(): return self.readSimb()
        self.page2_read_bt_pit = Button(
            self.page2, text="Прочитать симв", command=func3)
        self.page2_read_bt_pit.place(
            x=190, y=geom_par['heighY'] + 40, anchor="w", heigh=30, width=150,
            bordermode=OUTSIDE)

        self.kolSimb = Text(self.page2)
        self.kolSimb.place(
            x=345, y=geom_par['heighY'] + 25, anchor="nw",
            heigh=30, width=50,
            bordermode=OUTSIDE)

        def func2(): return self.page2_click_btn_clear()
        self.page2_btn_clear = Button(
            self.page2, text="Очистить", command=func2)
        self.page2_btn_clear.place(
            x=400, y=geom_par['heighY'] + 40, anchor="w", heigh=30,
            width=150, bordermode=OUTSIDE)

        self.page2_lineText_DublSlovo = Text(self.page2)  # all text
        self.page2_lineText_DublSlovo.place(x=10, y=geom_par['heighY'] + 60,
                                            anchor="nw", heigh=500,
                                            width=geom_par['P2widthW'],
                                            bordermode=OUTSIDE)

        botBg = 590

        # Two colunm ====================================================

        self.page2_clear_Text = Text(self.page2)
        self.page2_clear_Text.place(x=geom_par['P2widthW']+20,
                                    y=geom_par['heighY'] + 60,
                                    anchor="nw", heigh=500,
                                    width=geom_par['P2widthW'],
                                    bordermode=OUTSIDE)

        def func4(): return self.tokinez()
        self.btn_token = Button(self.page2, text="Токинезация", command=func4)
        self.btn_token.place(x=geom_par['P2widthW']+20, y=geom_par['heighY'] +
                             40, anchor="w", heigh=30, width=110,
                             bordermode=OUTSIDE)

        def func5(): return self.statText()
        self.btn_stat = Button(self.page2, text="Статистика", command=func5)
        self.btn_stat.place(x=geom_par['P2widthW']+20 + 115,
                            y=geom_par['heighY'] +
                            40, anchor="w", heigh=30,
                            width=110, bordermode=OUTSIDE)

        def func6(): return self.page2_click_btn_Ras()
        self.page2_btn_Ras = Button(
            self.page2, text="Обучиться", command=func6)
        self.page2_btn_Ras.place(x=geom_par['P2widthW']+20,
                                 y=geom_par['heighY'] +
                                 botBg, anchor="w", heigh=30,
                                 width=150, bordermode=OUTSIDE)

        def func7(): return self.page2_click_btn_Ras()
        self.page2_btn_Unm = Button(
            self.page2, text="Разделить", command=func7)
        self.page2_btn_Unm.place(x=geom_par['P2widthW']+180,
                                 y=geom_par['heighY'] +
                                 botBg, anchor="w",
                                 heigh=30, width=150, bordermode=OUTSIDE)

        # self.page2_btn_Kontext = Button(self.page2, text="Разделить текст",
        # command=self.page2_click_btn_Kontext())
        # self.page2_btn_Kontext.place(x=340, y=geom_par['heighY']+botBg ,
        # anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

    def statText(self):
        IsTxt = self.page2_clear_Text.get('1.0', END)
        stat = Counter()
        servList = IsTxt.strip().split(' ')
        for word in servList:
            stat[len(word)] += 1
        stat.most_common()
        # print(stat)
        self.page2_TextPath3.delete('1.0', END)
        textOut = ' длина слова  -----  кол.слов\n'
        for k in stat.most_common():
            textOut += (f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page2_TextPath3.insert('1.0', textOut)

    def statTextList(self, textList):
        stat = Counter()
        for word in textList:
            stat[len(word)] += 1
        stat.most_common()
        # print(stat)
        self.page2_TextPath3.delete('1.0', END)
        textOut = ' длина слова  -----  кол.слов\n'
        for k in stat.most_common():
            textOut += (f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page2_TextPath3.delete('1.0', END)
        self.page2_TextPath3.insert('1.0', textOut)

    def tokinez(self):
        """
        This module clear document of all bad simbols and
        start 20/12/2021
        end 21/12/2021

        Args:
            name (str): full text in lower simbols

        Returns:
            [str]: text with empty simbols bitween words

        """

        is_txt = self.page2_lineText_DublSlovo.get('1.0', END).lower()
        tt = is_txt.replace('c', 'с')
        tt = tt.replace('e', 'е')
        tt = tt.replace('a', 'а')
        tt = tt.replace('h', 'н')
        tt = tt.replace('p', 'р')
        tt = tt.replace('o', 'о')
        tt = tt.replace('t', 'т')
        tt = tt.replace('s', 'с')
        tt = tt.replace('r', 'р')
        # rul_one = re.compile(r'\s[а-я]\s')
        rul_ru = re.compile(r'[^А-Яа-яЁё]')
        rul_two = re.compile(r'[.,?!«»;:“)(№0-9]')
        rul_three = re.compile(r'\s+')
        # ttt =''
        tt = rul_ru.sub(' ', tt.strip())
        tt = ' '.join(tt.split('\n'))
        tt = tt.replace('\n', ' ')
        tt = tt.replace('”', ' ')
        tt = tt.replace('-', '')
        tt = tt.replace('‑', ' ')
        tt = tt.replace('"', ' ')
        tt = rul_two.sub(' ', tt)
        tt = rul_three.sub(' ', tt)
        ttt = tt.strip()
        # #ttt = ttt.replace(' в ', ' ')
        # #ttt = ttt.replace(' г ', ' ')
        # ttt = ttt.replace(' iv ', ' ')
        # ttt = ttt.replace(' iii ', ' ')
        # ttt = ttt.replace(' iii ', ' ')
        # ttt = ttt.replace(' ‑го ', ' го ')
        # ttt = ttt.replace(' – ', ' ')
        # ttt = ttt.replace(' i ', ' ')
        # ttt = rul_one.sub(' ', ttt)
        # ttt = rul_three.sub(' ',ttt)
        self.page2_clear_Text.delete('1.0', END)
        self.page2_clear_Text.insert('1.0', ttt)
        return ttt

    def readAllSource(self):
        # nameFile = self.page1.nameFile.get("1.0", END).strip()
        nameFile = var_sit['name_file']
        print('readAllSource ', var_sit)
        # sys.path.append(nameFile)
        if os.path.isfile(nameFile):
            with open(nameFile, "r", encoding='utf-8') as i_f:
                allText = i_f.read()
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0', allText)
        else:
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert(
                '1.0', f"файла с таким именем {nameFile}  не существует!!!")
        # print(nameFile)

    def readSimb(self):
        nameFile = var_sit['name_file']
        kolS = int(self.kolSimb.get("1.0", END).strip())
        # sys.path.append(nameFile)
        if os.path.isfile(nameFile):
            with open(nameFile, "r", encoding='utf-8') as i_f:
                allText = i_f.read()
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0', allText[:kolS])
        else:
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert(
                '1.0', f"файла с таким именем {nameFile}  не существует!!!")
        # print(nameFile)

    def page2_click_btn_clear(self):
        self.page2_lineText_DublSlovo.delete(1.0, END)

    def page2_click_btn_Ras(self):
        # learn and get dict fragment of diferetnt

        statis = Counter()
        ttt = self.tokinez().split()

        # lead module count dictionary
        # dd, text_exp, ReserchText, ReserchText332 = connectLearn(ttt)
        dd, text_exp, ReserchText = connectLearn(ttt)

        # define name file rezult work
        strBase = {'nameFileIs': var_sit['name_file']}
        nameFile = var_sit['name_file'].strip()\
            .split('/')[-1].split('.')[0] + '_'
        PathPrjWork = PathPrj +\
            'dividing_continuous_stream_characters_into_words/rezultResearch/'
        datFile = str(datetime.now())\
            .replace('-', '_').replace(' ', '_').replace(':', '_').split('.')[0]
        nameFileStream = PathPrjWork + nameFile + 'Stream_' + datFile + '.txt'

        print('first count words = ', len(ttt))
        strBase['nameFileStream'] = nameFileStream
        FileStream = open(nameFileStream, 'w', encoding='utf-8')
        nameFileVoc = PathPrjWork + nameFile + 'Voc_' + datFile + '.picle'
        strBase['nameFileVoc'] = nameFileVoc
        FileVoc = open(nameFileVoc, 'wb')
        pickle.dump(dd, FileVoc)
        FileVoc.close()
        self.page2_clear_Text.delete('1.0', END)
        self.page2_clear_Text.insert('1.0', ReserchText['rez'])
        json.dump(ReserchText, FileStream, ensure_ascii=False)
        FileStream.close()
        RezText = separatorWords(text_exp, dd)
        self.page2_TextPath3.delete('1.0', END)
        self.page2_TextPath3.insert('1.0', RezText)
        print('second count words = ', len(RezText.split()))
