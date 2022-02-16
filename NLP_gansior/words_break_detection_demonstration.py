'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/02/15
Ending 2022//
    
'''
    

import re
from collections import Counter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

dd = {}

# page2 Контекстный анализ слов click Buttom
def page2_click_btn_Kontext():
    is_str = page2_lineText_DublSlovo.get('1.0', END + '-1c')
    kk=0
    text_rez = ''
    for tt in is_str:
        frag =''
        if kk<(len(is_str)-6):
            for ik in range(6):
                frag += is_str[kk + ik]
            #print(frag)
            if frag in dd:
                text_rez += dd[frag]
                kk += 3
            else:
                text_rez += is_str[kk]
                kk += 1
    print(text_rez)
    page2_lineText_TextData.delete(1.0, END)
    page2_lineText_TextData.insert(INSERT, text_rez)


def page2_click_btn_Ras():
    is_text = page2_lineText_DublSlovo.get('1.0', END + '-1c')
    print(is_text)
    get_stat_break(is_text)
    statis = Counter()
    ttt = get_stat_break(is_text).split()
    kk = 0 
    len_dd = Counter()
    for tt in ttt:
        frag =''
        if kk+1 < len(ttt):
            t_n = ttt[kk+1].strip()
            tt = tt.strip()
            if len(tt)>=3 and len(ttt[kk+1])>=3:
                if len(tt) == 3 and len(ttt[kk + 1])> 3:
                    frag = (tt + ttt[kk + 1][0:3])
                elif len(tt) == 3 and len(ttt[kk + 1]) == 3:
                    frag = (tt + ttt[kk + 1])
                elif len(tt) > 3 and len(ttt[kk + 1]) == 3:
                    frag = (tt[-3:] + ttt[kk + 1])
                elif len(tt) > 3 and len(ttt[kk + 1]) > 3:    
                    frag = (tt[-3:] + ttt[kk + 1][0:3])
                statis[frag] +=1
                dd[frag] = tt[-3:] + ' '
                len_dd[len(frag)] += 1
        kk += 1
    text_exp = ''.join(ttt)
    print()
    print(text_exp)
    page2_lineText_DublSlovo.delete(1.0, END)
    page2_lineText_DublSlovo.insert(INSERT, text_exp)



def get_stat_break(is_txt:str):
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
    
    rul_one = re.compile(r'\s[а-я]\s')
    rul_two = re.compile(r'[.,?!«»;:“)(№0-9]')
    rul_three = re.compile(r'\s+')
    ttt =''
    tt = rul_one.sub(' ',is_txt.strip().lower())
    tt = ' '.join(tt.split('\n'))
    tt = tt.replace('\n', ' ')
    tt = tt.replace('”', ' ')
    tt = tt.replace('‑', ' ')
    tt = tt.replace('"', ' ')
    tt =rul_two.sub(' ',tt)
    tt =rul_three.sub(' ',tt)
    ttt +=(tt.strip() + ' ')
    ttt = ttt.replace(' в ', ' ')
    ttt = ttt.replace(' г ', ' ')
    ttt = ttt.replace(' iv ', ' ')
    ttt = ttt.replace(' iii ', ' ')
    ttt = ttt.replace(' iii ', ' ')
    ttt = ttt.replace(' ‑го ', ' ')
    ttt = ttt.replace(' – ', ' ')
    ttt = ttt.replace(' i ', ' ')
    ttt = rul_one.sub(' ', ttt)
    ttt = rul_three.sub(' ',ttt)
    return ttt.strip()
    

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
        

if __name__ == '__main__':
    """
    Get list of documents and work with them.
    Result - file csv with two fields field one - six simbols - [xxxxxx] field two - [xxx xxx]
    
    """
    
    # for i in range(1,19):
    #     num = get_num(i)
    #     n_f = f'/media/al/work1/NLP/Datasets/И.В. Сталин. Собрание сочинений в 18 томах/{num}.txt'
    #     get_stat_break(n_f)
    # n_f = f'/media/al/work1/NLP/Datasets/И.В. Сталин. Собрание сочинений в 18 томах/01.txt'
    # get_stat_break(n_f)
    # statis = Counter()
    # ttt = get_stat_break(n_f).split()
    # kk = 0 
    # dd = {}
    # len_dd = Counter()
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
    #             dd[frag] = tt[-3:] + ' '
    #             len_dd[len(frag)] += 1
    #     kk += 1
    # text_exp = ''.join(ttt)
    # print(text_exp[:500])
    # print()
    # text_rez = ''
    # kk = 0 
    
    # for tt in text_exp:
    #     frag =''
    #     if kk<(len(text_exp)-6):
    #         for ik in range(6):
    #             frag += text_exp[kk + ik]
    #         #print(frag)
    #         if frag in dd:
    #             text_rez += dd[frag]
    #             kk += 3
    #         else:
    #             text_rez += text_exp[kk]
    #             kk += 1
    #     #if kk >100: break
    # print(text_rez[0:600])

    root = Tk()
    root.title("Контекстный анализ слов и коротких фраз")
    root.geometry("1050x700")
    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Открыть...")
    filemenu.add_command(label="Новый")
    filemenu.add_command(label="Сохранить...")
    filemenu.add_command(label="Выход")

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="Помощь")
    helpmenu.add_command(label="О программе")

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)

    Osn = ttk.Notebook()
    page1 = Frame(Osn)
    page2 = Frame(Osn)
    page3 = Frame(Osn)
    Osn.add(page1, text='  Начальные установки  ')
    Osn.add(page2, text='  Разделение строки по словам  ')
    Osn.add(page3, text='  Исправление ошибок в словаре  ')
    Osn.pack(padx=2, pady=3, fill=BOTH, expand=1)

    # page1 Начальные установки
    widthLabe = 500
    widthBt = 300
    heighY = 10

 
    page2_label_Nom2_Slovo = Label(page2, text="Исходный текст")
    page2_label_Nom2_Slovo.place(x=120, y=heighY+10, anchor="w", heigh=20, width=150, bordermode=OUTSIDE)

    page2_label_Nom3_Slovo = Label(page2, text="Результат")
    page2_label_Nom3_Slovo.place(x=630, y=heighY+10, anchor="w", heigh=20, width=150, bordermode=OUTSIDE)

    page2_lineText_DublSlovo = Text(page2)
    page2_lineText_DublSlovo.place(x=10, y=heighY + 40, anchor="nw", heigh=500, width=500, bordermode=OUTSIDE)
    
    page2_lineText_TextData = Text(page2)
    page2_lineText_TextData.place(x=520, y=heighY + 40, anchor="nw", heigh=500, width=500, bordermode=OUTSIDE)

    page2_btn_Ras = Button(page2, text="Обучиться", command=page2_click_btn_Ras)
    page2_btn_Ras.place(x=10, y=heighY + 560, anchor="w", heigh=30, width=200, bordermode=OUTSIDE)

    page2_btn_Kontext = Button(page2, text="Разделить текст", command=page2_click_btn_Kontext)
    page2_btn_Kontext.place(x=280, y=heighY+560, anchor="w", heigh=30, width=200, bordermode=OUTSIDE)

    
root.mainloop()