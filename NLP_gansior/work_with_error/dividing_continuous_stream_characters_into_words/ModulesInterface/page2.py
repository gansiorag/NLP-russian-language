from base64 import encode
import re
from collections import Counter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from datetime import datetime
import pickle
import json

import os
import sys

nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error'
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
sys.path.append(PathPrj)

from ModulesInterface.baseModul import geomPar
from testFeuch import connectLearn


dd = {33:{},
      32:{},
      31:{},
      23:{},
      23:{},
      22:{},
      21:{},
      13:{},
      12:{},
      11:{}
      }

    

def get_num(i:int):
    """ Get number 

    Args:
        i (int): this number

    Returns:
        [str]: if number 1 - 9 returne 01 - 09 
    """
    answer = ''
    if i<10: answer = '0' + str(i)
    else:
        answer = str(i)
    return answer

    
class Page2() :
    
    def __init__(self, Osn, page1) -> None:
        
        self.page1 = page1

        self.page2 = Frame(Osn)
        Osn.add(self.page2, text='  Разделение строки по словам  ')
            


        self.page2_label_Path3 = Label(self.page2, text="Результат")
        self.page2_label_Path3.place(x=1150, y=geomPar['heighY']+10, anchor="w", heigh=20, width=150, bordermode=OUTSIDE)
        

        self.page2_TextPath3 = Text(self.page2)
        self.page2_TextPath3.place(x=geomPar['P2widthW']*2 + 30, y=geomPar['heighY'] + 60, anchor="nw", heigh=500, width=geomPar['P2widthW'], bordermode=OUTSIDE)


        # First colunm ===================================================================
        
        
        self.page2_label_Nom2_Slovo = Label(self.page2, text="Исходный текст")
        self.page2_label_Nom2_Slovo.place(x=120, y=geomPar['heighY']+10, anchor="w", heigh=20, width=150, bordermode=OUTSIDE)
                       
        func1 = lambda: self.readAllSource()
        self.page2_read_bt = Button(self.page2, text="Прочитать весь файл", command=func1)
        self.page2_read_bt.place(x=10, y=geomPar['heighY'] + 40, anchor="w", heigh=30, width=170, bordermode=OUTSIDE)


        func3 = lambda: self.readSimb()
        self.page2_read_bt_pit = Button(self.page2, text="Прочитать симв", command=func3)
        self.page2_read_bt_pit.place(x=190, y=geomPar['heighY'] + 40, anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

        self.kolSimb = Text(self.page2)
        self.kolSimb.place(x = 345, y=geomPar['heighY'] + 25, anchor="nw", heigh=30, width=50, bordermode=OUTSIDE)
        
        func2 = lambda: self.page2_click_btn_clear()
        self.page2_btn_clear = Button(self.page2, text="Очистить", command=func2)
        self.page2_btn_clear.place(x=400, y=geomPar['heighY'] + 40 , anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

        self.page2_lineText_DublSlovo = Text(self.page2) # all text
        self.page2_lineText_DublSlovo.place(x=10, y=geomPar['heighY'] + 60, anchor="nw", heigh=500, 
                                            width=geomPar['P2widthW'], bordermode=OUTSIDE)

        
        botBg = 590
        
        # Two colunm ===================================================================
                
        self.page2_clear_Text = Text(self.page2)
        self.page2_clear_Text.place(x=geomPar['P2widthW']+20, y=geomPar['heighY'] + 60, anchor="nw", heigh=500, 
                                    width=geomPar['P2widthW'], bordermode=OUTSIDE)
        
        func4 = lambda: self.tokinez()
        self.btn_token = Button(self.page2, text="Токинезация", command=func4)
        self.btn_token.place(x=geomPar['P2widthW']+20, y=geomPar['heighY'] + 40 , anchor="w", heigh=30, width=110, bordermode=OUTSIDE)

        func5 = lambda: self.statText()
        self.btn_stat = Button(self.page2, text="Статистика", command=func5)
        self.btn_stat.place(x=geomPar['P2widthW']+20 + 115, y=geomPar['heighY'] + 40 , anchor="w", heigh=30, width=110, bordermode=OUTSIDE)

        func6 = lambda: self.page2_click_btn_Ras()
        self.page2_btn_Ras = Button(self.page2, text="Обучиться", command=func6)
        self.page2_btn_Ras.place(x=geomPar['P2widthW']+20, y=geomPar['heighY'] + botBg , anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

        func7 = lambda: self.page2_click_btn_Ras()
        self.page2_btn_Unm = Button(self.page2, text="Разделить", command=func7)
        self.page2_btn_Unm.place(x=geomPar['P2widthW']+180, y=geomPar['heighY'] + botBg , anchor="w", heigh=30, width=150, bordermode=OUTSIDE)


        # self.page2_btn_Kontext = Button(self.page2, text="Разделить текст", command=self.page2_click_btn_Kontext())
        # self.page2_btn_Kontext.place(x=340, y=geomPar['heighY']+botBg , anchor="w", heigh=30, width=150, bordermode=OUTSIDE)

    def statText(self):
        IsTxt = self.page2_clear_Text.get('1.0', END)
        stat = Counter()
        servList = IsTxt.strip().split(' ')
        for word in servList:
            stat[len(word)] +=1
        stat.most_common()
        print(stat)
        self.page2_TextPath3.delete('1.0', END)
        textOut = ' длина слова  -----  кол.слов\n'
        for k in stat.most_common():
            textOut +=(f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page2_TextPath3.insert('1.0', textOut)        

    def statTextList(self,textList):
        stat = Counter()
        for word in textList:
            stat[len(word)] +=1
        stat.most_common()
        print(stat)
        self.page2_TextPath3.delete('1.0', END)
        textOut = ' длина слова  -----  кол.слов\n'
        for k in stat.most_common():
            textOut +=(f'{k[0]:12}  -----  {k[1]:8}\n')
        self.page2_TextPath3.delete('1.0', END)
        self.page2_TextPath3.insert('1.0', textOut) 
        
        
    def tokinez(self):
        """
        This module clear document of all bad simbols and 
        changes them to empty simbols
        start 20/12/2021
        end 21/12/2021

        Args:
            name (str): full text in lower simbols

        Returns:
            [str]: text with empty simbols bitween words
        
        """
        
        is_txt = self.page2_lineText_DublSlovo.get('1.0',END).lower()
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
        tt = rul_ru.sub(' ',tt.strip())
        tt = ' '.join(tt.split('\n'))
        tt = tt.replace('\n', ' ')
        tt = tt.replace('”', ' ')
        tt = tt.replace('-', '')
        tt = tt.replace('‑', ' ')
        tt = tt.replace('"', ' ')
        tt =rul_two.sub(' ',tt)
        tt =rul_three.sub(' ',tt)
        ttt =tt.strip()
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
        nameFile = self.page1.nameFile.get("1.0", END).strip()
        #sys.path.append(nameFile)
        if os.path.isfile(nameFile):
            with open(nameFile, "r") as i_f:
                allText=i_f.read()
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0',allText)
        else:
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0',f"файла с таким именем {nameFile}  не существует!!!")
        print(nameFile)


    def readSimb(self):
        nameFile = self.page1.nameFile.get("1.0", END).strip()
        kolS = int(self.kolSimb.get("1.0", END).strip())
        #sys.path.append(nameFile)
        if os.path.isfile(nameFile):
            with open(nameFile, "r") as i_f:
                allText=i_f.read()
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0',allText[:kolS])
        else:
            self.page2_lineText_DublSlovo.delete('1.0', END)
            self.page2_lineText_DublSlovo.insert('1.0',f"файла с таким именем {nameFile}  не существует!!!")
        print(nameFile)

    # self.page2 Контекстный анализ слов click Buttom
    # def page2_click_btn_Kontext(self):
    #     is_str = self.page2_lineText_DublSlovo.get('1.0', END + '-1c')
    #     # разделение 3 - 3
    #     kk=0
    #     #print(dd[33])
    #     text_rez = ''
    #     ichar =0
    #     while ichar < len(is_str):
    #         frag =is_str[ichar:ichar+6]
    #         #print('frag1 = ', frag)
    #         if frag in dd[33]:
    #             text_rez += dd[33][frag]
    #             ichar += 3
    #         else:
    #             text_rez += is_str[ichar]
    #             ichar += 1

    #     #print('text_rez1 = ', text_rez)
    #     # разделение 3 - 2
    #     is_list = text_rez.split()
    #     text_rez = ''
    #     for frr in is_list:
    #         if len(frr)>5:
    #             kk = 5
    #             st =0
    #             while kk<=(len(frr) - 1):
    #                 frag = frr[st:kk]
    #                 #print(frag)
    #                 if frag in dd[32]:
    #                     frr = frr[:st+3] + ' ' + frr[st+3:]
    #                     st = st + 4
    #                     kk = st + 5
    #                 else:
    #                     #text_rez += frr[st]
    #                     st +=1
    #                     kk += 1
    #             text_rez += frr + ' '
    #         elif len(frr)==5:
    #             if frr in dd[32]:
    #                 text_rez +=(frr[:3] + ' ' + frr[3:])
    #         else:
    #             text_rez +=(frr + ' ')
    #     #print('text_rez 2 = ', text_rez)
    #     # разделение 2 - 3
    #     is_list = text_rez.split()
    #     text_rez = ''
    #     for frr in is_list:
    #         if len(frr)>5:
    #             kk = 5
    #             st =0
    #             while kk<=(len(frr) - 1):
    #                 frag = frr[st:kk]
    #                 #print(frag)
    #                 if frag in dd[23]:
    #                     frr = frr[:st+2] + ' ' + frr[st+2:]
    #                     st = st+3
    #                     kk = st+5
    #                 else:
    #                     st +=1
    #                     kk += 1
    #             text_rez += frr + ' '
    #         elif len(frr)==5:
    #             if frr in dd[23]:
    #                 text_rez +=(frr[:2] + ' ' + frr[2:])
    #             else:
    #                 text_rez +=(frr + ' ')
    #         else:
    #             text_rez +=(frr + ' ')
    #     #print('text_rez 3 = ', text_rez)
    #     # разделение 3 - 3 по словный проход
    #     is_list = text_rez.split()
    #     text_rez = ''
    #     for frr in is_list:
    #         if len(frr)>6:
    #             kk = 6
    #             st =0
    #             while kk<=(len(frr) - 1):
    #                 frag = frr[st:kk]
    #                 #print(frag)
    #                 if frag in dd[33]:
    #                     frr = frr[:st+3] + ' ' + frr[st+3:]
    #                     st = st+4
    #                     kk = st+6
    #                 else:
    #                     st +=1
    #                     kk += 1
    #             text_rez += frr + ' '
    #         elif len(frr)==6:
    #             if frr in dd[33]:
    #                 text_rez +=(frr[:3] + ' ' + frr[3:])
    #             else:
    #                 text_rez += frr + ' '
    #         else:
    #             text_rez +=(frr + ' ')

    #     print('len(text_rez 2 = ', len(text_rez.split(' ')))
    #     self.page2_lineText_TextData.delete(1.0, END)
    #     self.page2_lineText_TextData.insert(INSERT, text_rez)


    def page2_click_btn_clear(self):
        self.page2_lineText_DublSlovo.delete(1.0, END)


    def page2_click_btn_Ras(self):
        # learn and get dict fragment of diferetnt

        statis = Counter()
        ttt = self.tokinez().split()
        
        # lead module count dictionary
        dd, text_exp, ReserchText, ReserchText332 = connectLearn(ttt)
        
        self.statTextList(ReserchText332)
        print(ReserchText332)
        # kk = 0 
        # len_dd = Counter()
        # list_join = []
        # indItem = 0
        # while indItem < len(ttt):
        #     if len(ttt[indItem]) == 1 and indItem <(len(ttt) - 1):
        #         if len(ttt[indItem +1]) == 1:
        #             frag = ttt[indItem] + ttt[indItem + 1]
        #             dd[11][frag] = ttt[indItem] + ' ' + ttt[indItem + 1]
        #             ttt.pop(indItem + 1)
        #     indItem +=1
        # for tt in ttt: 
        #     frag =''
        #     if kk+1 < len(ttt):
        #         t_n = ttt[kk+1].strip()
        #         tt = tt.strip()
        #         if len(tt)>=3 and len(ttt[kk+1])>=3:
        #             if len(tt) == 3 and len(ttt[kk + 1])> 3:
        #                 frag = (tt + ttt[kk + 1][0:3])
        #             elif len(tt) == 3 and len(ttt[kk + 1]) == 3:
        #                 frag = (tt + ttt[kk + 1])
        #             elif len(tt) > 3 and len(ttt[kk + 1]) == 3:
        #                 frag = (tt[-3:] + ttt[kk + 1])
        #             elif len(tt) > 3 and len(ttt[kk + 1]) > 3:    
        #                 frag = (tt[-3:] + ttt[kk + 1][0:3])
        #             statis[frag] +=1
        #             dd[33][frag] = tt[-3:] + ' '
        #             len_dd[len(frag)] += 1
        #         else:
        #             list_join.append(tt +' '+ ttt[kk+1])

        #     kk += 1
        # for tt in list_join:
        #     serviis_list = tt.split()
        #     if len(serviis_list[0])>=3 and len(serviis_list[1])==2:
        #         dd[32][serviis_list[0][-3:]+serviis_list[1]] = serviis_list[0][-3:]+ ' ' + serviis_list[1]
        #     elif len(serviis_list[0]) ==2 and len(serviis_list[1])>=3:
        #         dd[23][serviis_list[0]+serviis_list[1][:3]] = serviis_list[0]+ ' ' + serviis_list[1][:3]
        # print('dd[32] = ', dd[32])
        # print('dd[23] = ',dd[23])     
        # print(list_join)
        # text_exp = ''.join(ttt)
        # print()
        # print(text_exp)
        # print('count words = ',len(ttt))
        
        # define name file rezult work
        strBase = {'nameFileIs':self.page1.nameFile.get("1.0", END).strip()}
        nameFile = self.page1.nameFile.get("1.0", END).strip().split('/')[-1].split('.')[0] + '_'
        PathPrjWork = PathPrj+'dividing_continuous_stream_characters_into_words/rezultResearch/'
        datFile= str(datetime.now()).replace('-', '_').replace(' ', '_').replace(':', '_').split('.')[0]
        nameFileStream = PathPrjWork + nameFile + 'Stream_' + datFile + '.txt'
        
        # print('count words = ',len(ttt))
        strBase['nameFileStream'] = nameFileStream
        FileStream = open(nameFileStream, 'w', encoding='utf-8')
        nameFileVoc = PathPrjWork + nameFile + 'Voc_' + datFile + '.picle'
        strBase['nameFileVoc'] = nameFileVoc
        FileVoc = open(nameFileVoc, 'wb')
        pickle.dump(dd, FileVoc)
        FileVoc.close()
        self.page2_clear_Text.delete('1.0', END)
        self.page2_clear_Text.insert('1.0', ReserchText['CountText'])
        json.dump(ReserchText,FileStream, ensure_ascii=False)
        FileStream.close()
        # self.page2_TextPath3.delete('1.0', END)
        # self.page2_TextPath3.insert('1.0', dd) 
        