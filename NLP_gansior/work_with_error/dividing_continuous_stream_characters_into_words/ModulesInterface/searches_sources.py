"""_summary_

Returns:
    _type_: _description_
"""

import os
import sys
from collections import Counter
from tkinter import Text, Label, Button, Frame, OUTSIDE, END
from datetime import datetime
import pickle
import json

from testFeuch import connectLearn, separatorWords
from ModulesInterface.baseModul import geom_par, var_sit


NAME_PROJECT_START = 'NLP-russian-language'
NAME_PROJECT = 'NLP-russian-language/NLP_gansior/work_with_error'
PathPrj = os.getcwd().split(NAME_PROJECT_START)[0] + NAME_PROJECT + '/'
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


class SearchS():
    """_summary_
    """

    def __init__(self, Osn) -> None:

        self.page_base = Frame(Osn)

        # First colunm =======================================================

        self.page_base_label_Nom2_Slovo = Label(
            self.page_base, text="Слитный текст")
        self.page_base_label_Nom2_Slovo.place(
            x=120, y=geom_par['heigh_y']+10, anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        def func1():
            return self.vis_text()
        self.page_base_read_bt = Button(
            self.page_base, text="Показать текст", command=func1)
        self.page_base_read_bt.place(
            x=10, y=geom_par['heigh_y'] + 40,
            anchor="w", heigh=30, width=170,
            bordermode=OUTSIDE)

        def func3():
            return self.page_study()
        self.page_base_btn_ras = Button(
            self.page_base, text="Обучиться", command=func3)
        self.page_base_btn_ras.place(x=190,
                                     y=geom_par['heigh_y'] + 40,
                                     anchor="w",
                                     heigh=30,
                                     width=150,
                                     bordermode=OUTSIDE)

        self.page_base_line_text_dubl_slovo = Text(self.page_base)
        self.page_base_line_text_dubl_slovo.place(
            x=30,
            y=geom_par['heigh_y'] + 200,
            anchor="nw",
            heigh=500,
            width=geom_par['P2widthW'],
            bordermode=OUTSIDE)

        def func2():
            return self.page_base_click_btn_clear()
        self.page_base_btn_clear = Button(
            self.page_base, text="Очистить", command=func2)
        self.page_base_btn_clear.place(
            x=400,
            y=geom_par['heigh_y'] + 40,
            anchor="w", heigh=30,
            width=150, bordermode=OUTSIDE)

        # Two colunm ====================================================

        def func4():
            return self.page_base_click_btn_ras()

        self.page_base_btn_unm = Button(self.page_base,
                                        text="Разделить",
                                        command=func4)
        self.page_base_btn_unm.place(x=geom_par['P2widthW'] + 40,
                                     y=geom_par['heigh_y'] + 40,
                                     anchor="w",
                                     heigh=30,
                                     width=110,
                                     bordermode=OUTSIDE)

        self.page_base_clear_Text = Text(self.page_base)
        self.page_base_clear_Text.place(
            x=geom_par['P2widthW'] + 30,
            y=geom_par['heigh_y'] + 200,
            anchor="nw",
            heigh=500,
            width=geom_par['P2widthW'],
            bordermode=OUTSIDE)



        # ========= Three column =================
        self.page_base_label_Path3 = Label(self.page_base, text="Результат")
        self.page_base_label_Path3.place(
            x=1150, y=geom_par['heigh_y']+10,
            anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        def func5():
            return self.stat_text()
        self.btn_stat = Button(
            self.page_base, text="Статистика длин слов", command=func5)
        self.btn_stat.place(x=geom_par['P2widthW']*2 + 30,
                            y=geom_par['heigh_y'] + 40,
                            anchor="w",
                            heigh=30,
                            width=200, bordermode=OUTSIDE)

        self.page_base_text_path3 = Text(self.page_base)
        self.page_base_text_path3.place(x=geom_par['P2widthW']*2 + 30,
                                        y=geom_par['heigh_y'] + 200,
                                        anchor="nw",
                                        heigh=500,
                                        width=geom_par['P2widthW'],
                                        bordermode=OUTSIDE)

    # =============== functions =========================

    def stat_text(self):
        """_summary_
        """
         
        IsTxt = var_sit['result_text']
        stat = Counter()
        servList = IsTxt.strip().split()
        for word in servList:
            stat[len(word)] += 1
        stat.most_common()
        # print(stat)
        self.page_base_text_path3.delete('1.0', END)
        text_out = f' общее количество слов  ----- {str(len(servList))}\n\n'
        text_out += ' длина слова  -----  кол.слов\n'
        stat = sorted(stat.items(), key=lambda i: i[1], reverse=True)
        for k in stat:
            text_out += (f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page_base_text_path3.insert('1.0', text_out)

    def stat_textList(self, textList):
        stat = Counter()
        for word in textList:
            stat[len(word)] += 1
        stat.most_common()
        # print(stat)
        self.page_base_text_path3.delete('1.0', END)
        textOut = ' длина слова  -----  кол.слов\n'
        for k in stat.most_common():
            textOut += (f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page_base_text_path3.delete('1.0', END)
        self.page_base_text_path3.insert('1.0', textOut)

    def vis_text(self):
        """_summary_
        """
        print('vis_text(', var_sit)
        text_out = 'Сначала токенезируйте текст!!! \n'
        self.page_base_line_text_dubl_slovo.delete('1.0', END)
        if var_sit['token_text']:
            text_out = var_sit['token_text'].replace(' ', '')
        self.page_base_line_text_dubl_slovo.insert('1.0', text_out)

    def page_base_click_btn_clear(self):
        """_summary_
        """
        self.page_base_clear_Text.delete(1.0, END)

    def page_study(self):
        """_summary_
        """
        # learn and get dict fragment of diferetnt

        ttt = var_sit['token_text'].split()

        # lead module count dictionary
        # dd, text_exp, reserch_text, reserch_text332 = connectLearn(ttt)
        dd_c, text_exp, reserch_text = connectLearn(ttt)
        var_sit['dict_model'] = dd_c
        var_sit['text_exp'] = text_exp
        # define name file rezult work
        str_base = {'name_fileIs': var_sit['name_file']}
        name_file = var_sit['name_file'].strip()\
            .split('/')[-1].split('.')[0] + '_'
        PathPrjWork = PathPrj +\
            'dividing_continuous_stream_characters_into_words/rezultResearch/'
        dat_file = str(datetime.now())\
            .replace('-', '_').replace(' ', '_')\
            .replace(':', '_').split('.')[0]
        name_fileStream = (PathPrjWork + name_file +
                           'Stream_' + dat_file + '.txt')

        print('first count words = ', len(ttt))
        str_base['name_fileStream'] = name_fileStream
        FileStream = open(name_fileStream, 'w', encoding='utf-8')
        name_fileVoc = PathPrjWork + name_file + 'Voc_' + dat_file + '.picle'
        str_base['name_fileVoc'] = name_fileVoc
        FileVoc = open(name_fileVoc, 'wb')
        pickle.dump(dd_c, FileVoc)
        FileVoc.close()
        json.dump(reserch_text, FileStream, ensure_ascii=False)
        FileStream.close()

    def page_base_click_btn_ras(self):
        """_summary_
        """
        
        rez_text = separatorWords(var_sit['text_exp'],
                                  var_sit['dict_model'])
        self.page_base_clear_Text.delete('1.0', END)
        self.page_base_clear_Text.insert('1.0', rez_text)
        var_sit['result_text'] = rez_text
        print('second count words = ', len(rez_text.split()))
