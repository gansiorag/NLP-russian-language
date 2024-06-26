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
from ServisModules.oper_w_words import del_word_len_1, stat_combi_n_n
from ServisModules.oper_w_words import stat_combi_2_n


nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error'
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
sys.path.append(PathPrj)


class page_pred_work():

    def __init__(self, Osn) -> None:

        self.page_base = Frame(Osn)
        # ширина окон
        y_st_text = geom_par['P2widthW']
        # высота расположения окон
        у_hihg = geom_par['heigh_y'] + 260

        # First colunm =======================================================

        self.page_base_label_Nom2_Slovo = Label(self.page_base,
                                                text="Исходный текст")
        self.page_base_label_Nom2_Slovo.place(
            x=120, y=geom_par['heigh_y']+10, anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        self.page_base_start = Label(self.page_base,
                                     text="Прочитать с ")
        self.page_base_start.place(
            x=10, y=geom_par['heigh_y'] + 40,
            anchor="w", heigh=30, width=150,
            bordermode=OUTSIDE)

        self.start_simb = Text(self.page_base)
        self.start_simb.insert('1.0', '0')
        self.start_simb.place(
            x=130, y=geom_par['heigh_y'] + 30, anchor="nw",
            heigh=30, width=50,
            bordermode=OUTSIDE)

        def func3():
            return self.read_simb()
        self.page_base_read_bt_pit = Button(
            self.page_base, text="Прочитать симв", command=func3)
        self.page_base_read_bt_pit.place(
            x=190, y=geom_par['heigh_y'] + 45, anchor="w", heigh=30, width=170,
            bordermode=OUTSIDE)

        self.kol_sim = Text(self.page_base)
        self.kol_sim.place(
            x=365, y=geom_par['heigh_y'] + 30, anchor="nw",
            heigh=30, width=50,
            bordermode=OUTSIDE)

        def func1():
            return self.readAllSource()
        self.page_base_read_bt = Button(
            self.page_base, text="Прочитать весь файл", command=func1)
        self.page_base_read_bt.place(
            x=190, y=geom_par['heigh_y'] + 85,
            anchor="w", heigh=30, width=170,
            bordermode=OUTSIDE)

        def func2():
            return self.page_base_click_btn_clear()
        self.page_base_btn_clear = Button(
            self.page_base, text="Очистить", command=func2)
        self.page_base_btn_clear.place(
            x=190, y=geom_par['heigh_y'] + 125, anchor="w", heigh=30,
            width=170, bordermode=OUTSIDE)

        self.page_base_lineText_DublSlovo = Text(self.page_base)  # all text
        self.page_base_lineText_DublSlovo.place(x=10, y=у_hihg,
                                                anchor="nw", heigh=500,
                                                width=y_st_text,
                                                bordermode=OUTSIDE)

        botBg = 40

        # Two colunm ====================================================

        self.page_base_clear_Text = Text(self.page_base)
        self.page_base_clear_Text.place(x=geom_par['P2widthW']+20,
                                        y=у_hihg,
                                        anchor="nw", heigh=500,
                                        width=y_st_text,
                                        bordermode=OUTSIDE)

        def func4(): return self.tokinez()
        self.btn_token = Button(self.page_base, text="Токинезация",
                                command=func4)
        self.btn_token.place(x=geom_par['P2widthW']+20, y=geom_par['heigh_y'] +
                             40, anchor="w", heigh=30, width=110,
                             bordermode=OUTSIDE)

        def func9():
            return self.link_words_1()
        self.btn_stat = Button(self.page_base, text="Сливаем слова N + N",
                               command=func9)
        self.btn_stat.place(x=geom_par['P2widthW'] + 200,
                            y=geom_par['heigh_y'] + 40,
                            anchor="w", heigh=30,
                            width=200, bordermode=OUTSIDE)

# ========= thert column ==================
        t_col = 600
        w_bot = 170

        def func5():
            return self.stat_simb()
        self.btn_stat = Button(self.page_base, text="Статистика символов",
                               command=func5)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col,
                            y=geom_par['heigh_y'] + botBg,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

        def func6():
            return self.stat_word_full_text()

        self.page_base_btn_Ras = Button(
            self.page_base, text="Статистика слов", command=func6)
        self.page_base_btn_Ras.place(x=geom_par['P2widthW'] + t_col,
                                     y=geom_par['heigh_y'] + botBg * 2,
                                     anchor="w", heigh=30,
                                     width=w_bot, bordermode=OUTSIDE)

        def func7():
            return self.stat_text_len_word()

        self.page_base_btn_Unm = Button(
            self.page_base, text="Статистика длин слов", command=func7)
        self.page_base_btn_Unm.place(x=geom_par['P2widthW'] + t_col,
                                     y=geom_par['heigh_y'] + botBg * 3,
                                     anchor="w",
                                     heigh=30, width=w_bot, bordermode=OUTSIDE)

        # self.page_base_btn_Kontext = Button(self.page_base,
        # text="Разделить текст",
        # command=self.page_base_click_btn_Kontext())
        # self.page_base_btn_Kontext.place(x=340, y=geom_par['heigh_y']+botBg ,
        # anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

        self.page_base_label_Path3 = Label(self.page_base, text="Результат")
        self.page_base_label_Path3.place(
            x=1150, y=geom_par['heigh_y']+10,
            anchor="w", heigh=20, width=150,
            bordermode=OUTSIDE)

        self.page_base_TextPath3 = Text(self.page_base)
        self.page_base_TextPath3.place(x=geom_par['P2widthW']*2 + 30,
                                       y=у_hihg,
                                       anchor="nw",
                                       heigh=500,
                                       width=y_st_text,
                                       bordermode=OUTSIDE)

        def func8():
            return self.stat_combi_1_1()
        self.btn_stat = Button(self.page_base, text="Статистика слов 1 + N",
                               command=func8)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col + 200,
                            y=geom_par['heigh_y'] + botBg,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

        def func10():
            return self.stat_combi_2_2()
        self.btn_stat = Button(self.page_base, text="Статистика слов 2 + N",
                               command=func10)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col + 200,
                            y=geom_par['heigh_y'] + botBg*2,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

        def func11():
            return self.stat_combi_3_3()
        self.btn_stat = Button(self.page_base, text="Статистика слов 3 + N",
                               command=func11)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col + 200,
                            y=geom_par['heigh_y'] + botBg*3,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

        def func12():
            return self.stat_combi_4_4()
        self.btn_stat = Button(self.page_base, text="Статистика слов 4 + N",
                               command=func12)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col + 200,
                            y=geom_par['heigh_y'] + botBg*3,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

        def func13():
            return self.stat_combi_lg_lg()
        self.btn_stat = Button(self.page_base, text="Статистика слов lg + lg",
                               command=func13)
        self.btn_stat.place(x=geom_par['P2widthW'] + t_col + 200,
                            y=geom_par['heigh_y'] + botBg*4,
                            anchor="w", heigh=30,
                            width=w_bot, bordermode=OUTSIDE)

    def stat_combi_1_1(self):
        """AI is creating summary for stat_combi_1_1
        """
        text_out = ''
        if var_sit['searched_text']['text']:
            text_out, stat_n_n = stat_combi_n_n(
                var_sit['searched_text']['text'])
            var_sit['searched_text']['stat_1+N'] = stat_n_n
        else:
            # print(var_sit['token_text']['text'])
            text_out, stat_n_n = stat_combi_n_n(
                var_sit['token_text']['text'])
            var_sit['token_text']['stat_1+N'] = stat_n_n

        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def stat_combi_2_2(self):
        """AI is creating summary for stat_combi_2_n
        """
        text_out = ''
        if var_sit['searched_text']['text']:
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['searched_text']['text'])
            var_sit['searched_text']['stat_2+N'] = stat_2_n
        else:
            # print(var_sit['token_text']['text'])
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['token_text']['text'])
            var_sit['token_text']['stat_2+N'] = stat_2_n

        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def stat_combi_3_3(self):
        """AI is creating summary for stat_combi_2_n
        """
        text_out = ''
        if var_sit['searched_text']['text']:
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['searched_text']['text'])
            var_sit['searched_text']['stat_2+N'] = stat_2_n
        else:
            # print(var_sit['token_text']['text'])
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['token_text']['text'])
            var_sit['token_text']['stat_2+N'] = stat_2_n

        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def stat_combi_4_4(self):
        """AI is creating summary for stat_combi_2_n
        """
        text_out = ''
        if var_sit['searched_text']['text']:
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['searched_text']['text'])
            var_sit['searched_text']['stat_2+N'] = stat_2_n
        else:
            # print(var_sit['token_text']['text'])
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['token_text']['text'])
            var_sit['token_text']['stat_2+N'] = stat_2_n

        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def stat_combi_lg_lg(self):
        """AI is creating summary for stat_combi_2_n
        """
        text_out = ''
        if var_sit['searched_text']['text']:
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['searched_text']['text'])
            var_sit['searched_text']['stat_2+N'] = stat_2_n
        else:
            # print(var_sit['token_text']['text'])
            text_out, stat_2_n = stat_combi_2_n(
                var_sit['token_text']['text'])
            var_sit['token_text']['stat_2+N'] = stat_2_n

        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def link_words_1(self):
        if var_sit['searched_text']['text']:
            var_sit['searched_text'] = del_word_len_1(
                var_sit['searched_text']['text'])
        else:
            var_sit['searched_text']['text'] = del_word_len_1(
                var_sit['token_text']['text'])
        self.page_base_clear_Text.delete('1.0', END)
        self.page_base_clear_Text.insert(
            '1.0', var_sit['searched_text']['text'])

    def stat_text_len_word(self):
        """AI is creating summary for stat_text_len_word
        """
        text_out = 'Сначала токенезируйте текст!!! \n'
        if var_sit['token_text']['text']:
            text_list = var_sit['token_text'].split()
            stat = Counter()
            for word in text_list:
                stat[len(word)] += 1
            stat.most_common()

            var_sit['stat_len_word_token_text'] = dict(stat)
            self.page_base_TextPath3.delete('1.0', END)
            text_out = (' общее количество слов  ----- ' +
                        f'{str(len(text_list))}\n\n')
            text_out += ' длина слова  -----  кол.слов\n'
            stat = sorted(stat.items(), key=lambda i: i[1], reverse=True)
            # print(stat)
            for k in stat:
                text_out += (f'{k[0]:12}  -----  {k[1]:8}\n')
        # print(var_sit['stat_len_word_token_text'])
        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

    def stat_simbol_full_text(self):
        is_text = var_sit['all_text'].lower()
        is_text = is_text.replace('\n', ' ').replace('  ', ' ')\
            .replace('  ', ' ').replace('\t', ' ').replace('\r', ' ')
        stat = Counter()
        stat['общ_кол'] = len(is_text)
        for simb in list(is_text):
            stat[simb] += 1
        vv = dict(stat.most_common())
        return vv

    def stat_word_full_text(self):
        """_summary_
        """
        text_out = 'Сначала токенезируйте текст!!! \n'
        if var_sit['token_text']['text']:
            is_text = var_sit['token_text']['text']
            is_text = is_text.replace('\n', ' ').replace('  ', ' ')\
                .replace('  ', ' ').replace('\t', ' ').replace('\r', ' ')
            stat = Counter()
            list_text = is_text.split()
            text_out = f' общее количество слов  ----- {str(len(list_text))}\n\n'
            text_out += ' слово  -----------  кол.\n'
            for simb in list_text:
                stat[simb.strip()] += 1
            stat = dict(stat)
            var_sit['stat_word_token_text'] = dict(stat)
            stat = sorted(stat.items(), key=lambda i: i[1], reverse=True)
            for word in stat:
                str_s = (f" {word[0]}  ----- "
                         f"{word[1]} \n")
                text_out += str_s
        self.page_base_TextPath3.delete('1.0', END)
        self.page_base_TextPath3.insert('1.0', text_out)

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

        is_txt = self.page_base_lineText_DublSlovo.get('1.0', END).lower()
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
        self.page_base_clear_Text.delete('1.0', END)
        self.page_base_clear_Text.insert('1.0', ttt)
        var_sit['token_text']['text'] = ttt
        var_sit['searched_text']['text'] = ''
        var_sit['stat_simb_all_text'] = self.stat_simbol_full_text()
        # var_sit = {
        #    'stat_token_text': [],
        #    'result_text': '',
        #    'stat_result_text': [],
        #    'dict_text': []}
        return ttt

    def readAllSource(self):
        """_summary_
        """

        name_file = var_sit['name_file']
        # print('readAllSource ', var_sit)
        start_s = int(self.start_simb.get("1.0", END).strip())
        # sys.path.append(name_file)
        if os.path.isfile(name_file):
            with open(name_file, "r", encoding='utf-8') as i_f:
                all_text = i_f.read()
            self.page_base_lineText_DublSlovo.delete('1.0', END)
            self.page_base_lineText_DublSlovo.insert('1.0', all_text[start_s:])
            var_sit['all_text'] = all_text[start_s:]
        else:
            self.page_base_lineText_DublSlovo.delete('1.0', END)
            self.page_base_lineText_DublSlovo.insert(
                '1.0', f"файла с таким именем {name_file}  не существует!!!")
        # print(name_file)

    def read_simb(self):
        name_file = var_sit['name_file']
        kol_s = int(self.kol_sim.get("1.0", END).strip())
        start_s = int(self.start_simb.get("1.0", END).strip())
        # sys.path.append(name_file)
        if os.path.isfile(name_file):
            with open(name_file, "r", encoding='utf-8') as i_f:
                all_text = i_f.read()
            self.page_base_lineText_DublSlovo.delete('1.0', END)
            self.page_base_lineText_DublSlovo\
                .insert('1.0',
                        all_text[start_s:start_s + kol_s])
            var_sit['all_text'] = all_text[start_s:start_s + kol_s]
        else:
            self.page_base_lineText_DublSlovo.delete('1.0', END)
            self.page_base_lineText_DublSlovo.insert(
                '1.0', f"файла с таким именем {name_file}  не существует!!!")
        # print(name_file)

    def page_base_click_btn_clear(self):
        self.page_base_lineText_DublSlovo.delete(1.0, END)
        var_sit['all_text'] = ''
