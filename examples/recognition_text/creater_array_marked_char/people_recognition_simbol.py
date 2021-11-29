"""
This module make

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import cv2
from PIL import Image, ImageTk
from get_sentenses_from_file import sentenses
import os


"""
simbol = {'img_sim':[],
          'value_sim':''}

word = {'word_img':[],
        'word_def':[],
        'sim_word':[]}
sens = {'img_sent':[]
        'words':[]}
"""
heighY=100
sentenses_array = []
com_count_simbols, count_simbols = 0, 0
com_count_words, count_words = 0, 0
com_count_sentenses, count_sentenses = 0, -1
path_data =''

# page1 Начальные установки click Buttom
def page1_click_btn_Slovar():
    page1_lineNameFile.delete(1.0, END)
    name_file = askopenfilename(filetypes=(("JPG files", "*.jpg"), ("All files", "*.*")))
    page1_lineNameFile.insert(1.0, name_file)
    global sentenses_array, path_data
    path_data = os.getcwd()
    if path_data.find('creater_array_marked_char') >= 0 :
        path_data = path_data +'/'
    else:
        path_data = path_data + '/creater_array_marked_char'
    print(path_data)
    sentenses_array = sentenses(name_file)
    global com_count_sentenses, count_sentenses
    com_count_sentenses = len(sentenses_array)
    count_sentenses = 0
    print(len(sentenses_array))
    output_sentenses()


def output_sentenses():
    cv2image_sens = sentenses_array[count_sentenses]['img_sent']
    img_sens = Image.fromarray(cv2image_sens)
    #img_sens.show()
    imgtk_sens = ImageTk.PhotoImage(image=img_sens)
    image_label_sens.configure(image=imgtk_sens)
    image_label_sens.image = imgtk_sens
    output_word()


def click_btn_next_sentense():
    global count_sentenses
    global com_count_words, count_words
    count_sentenses += 1
    if count_sentenses == com_count_sentenses:
        messagebox.showinfo('Оповещение 1', 'Файл полностью обработан! \n Выберите другой файл!')
        page1_click_btn_Slovar()
    com_count_words, count_words = 0, 0
    com_count_words = len(sentenses_array[count_sentenses]['words'])
    print('sentens --- ', count_sentenses,com_count_words, count_words, sep = ' ---- ')
    output_sentenses()


def output_word():
    global count_sentenses
    global com_count_words, count_words
    global com_count_simbols, count_simbols
    words_array = sentenses_array[count_sentenses]['words'][count_words]
    #print((words_array['sim_word']))
    com_count_simbols = len(words_array['sim_word'])
    count_simbols = 0
    print('w-s', count_words, com_count_simbols, sep = ' ---- ')

    cv2image_word = words_array['word_img']
    img_word = Image.fromarray(cv2image_word)
    #img_sens.show()
    imgtk_word = ImageTk.PhotoImage(image=img_word)
    image_line_word.configure(text = "")
    image_line_word.text = ""
    image_line_word.configure(image=imgtk_word)
    image_line_word.image = imgtk_word

    cv2image_word_def = words_array['word_def']
    img_word_def = Image.fromarray(cv2image_word_def)
    #img_sens.show()
    imgtk_word_def = ImageTk.PhotoImage(image=img_word_def)
    label_word_sim.configure(text = "")
    label_word_sim.text = ""
    label_word_sim.configure(image=imgtk_word_def)
    label_word_sim.image = imgtk_word_def
    output_sim()


def click_btn_next_word():
    """
    word = {'word_img':[],
        'word_def':[],
        'sim_word':[]}

    :return:
    """
    global count_sentenses
    global com_count_words, count_words
    global com_count_simbols, count_simbols
    com_count_words = len(sentenses_array[count_sentenses]['words'])
    count_words += 1
    if count_words == com_count_words:
        click_btn_next_sentense()
    else:
        words_array = sentenses_array[count_sentenses]['words'][count_words]
        #print((words_array['sim_word']))
        com_count_simbols = len(words_array['sim_word'])
        count_simbols = 0
        print('w-s', count_words, com_count_simbols, sep = ' ---- ')
        output_word()


def output_sim():
    """
    simbol = {'img_sim':[],
              'value_sim':''}
    """
    # global com_count_words, count_words
    # global com_count_simbols, count_simbols
    sim_array = sentenses_array[count_sentenses]['words'][count_words]['sim_word']
    #print(sentenses_array[count_sentenses]['words'][count_words])
    com_count_simbols = len(sim_array)
    print('kol simb - ', com_count_simbols)
    print('w-simb', count_words, count_simbols, sep=' ---- ')
    cv2image_sim = sim_array[count_simbols]['img_sim']
    img_sim= Image.fromarray(cv2image_sim)
    # img_sens.show()
    imgtk_sim = ImageTk.PhotoImage(image=img_sim)
    image_line_sim.configure(text="")
    image_line_sim.text = ""
    image_line_sim.configure(image=imgtk_sim)
    image_line_sim.image = imgtk_sim


def get_num_max():
    num_max = 0
    with open(path_data +'data_set_simb/result_reconition_simb_gag.csv', 'r') as is_f:
        for line in is_f:
            if len(line.strip())>0 :
                numer_sim = int(line.split('^')[0].split('.')[0].split('_')[1])
                if numer_sim > num_max:
                    num_max = numer_sim
            else:
                break
    return num_max

def click_btn_wtite_sim():
    """
    simbol = {'img_sim':[],
              'value_sim':''}
    """
    # global com_count_words, count_words
    global com_count_simbols, count_simbols
    sim_array = sentenses_array[count_sentenses]['words'][count_words]['sim_word']
    #print(sentenses_array[count_sentenses]['words'][count_words])
    com_count_simbols = len(sim_array)
    print('kol simb - ', com_count_simbols)

    print('w-simb', count_words, count_simbols, sep=' ---- ')

    num_simb = str(get_num_max()+1)
    path_sim = path_data +'data_set_simb/'
    cv2.imwrite(path_sim + 'gag_'+num_simb + '.jpg', sim_array[count_simbols]['img_sim'])
    with open(path_sim + 'result_reconition_simb_gag.csv','a') as is_f:
        simbol_value = line_sim.get('1.0', END + '-1c')
        str_write = 'gag_'+num_simb + '.jpg^'+simbol_value+'\n'
        is_f.write(str_write)
    line_sim.delete(1.0, END)
    count_simbols += 1
    if count_simbols >= com_count_simbols:
        count_simbols -= 1
        line_sim.delete(1.0, END)
        click_btn_next_word()
    else:
        output_sim()


def click_btn_next_sim():
    """
    simbol = {'img_sim':[],
              'value_sim':''}
    """
    # global com_count_words, count_words
    global com_count_simbols, count_simbols
    sim_array = sentenses_array[count_sentenses]['words'][count_words]['sim_word']
    #print(sentenses_array[count_sentenses]['words'][count_words])
    com_count_simbols = len(sim_array)
    print('kol simb - ', com_count_simbols)

    print('w-simb', count_words, count_simbols, sep=' ---- ')
    count_simbols +=1
    if count_simbols >= com_count_simbols:
        line_sim.delete(1.0, END)
        click_btn_next_word()
    else:
        line_sim.delete(1.0, END)
        output_sim()


if __name__ == "__main__":
    window = Tk()
    window.title("Распознавание символов")
    window.geometry("1800x700")

    labelTitle = ttk.Label(window, text="Создание массива распознанных символов.")
    labelTitle.place(x=200, y=20, anchor="w", heigh=20, width=1000, bordermode=OUTSIDE)

    page1_lineNameFile = Text(window)
    page1_lineNameFile.place(x=10, y=70, anchor="w", heigh=60, width=1000, bordermode=OUTSIDE)

    page1_btn_Slovar = Button(window, text="Выберите файл с изображением текста", command=page1_click_btn_Slovar)
    page1_btn_Slovar.place(x=1020, y=70, anchor="w", heigh=30, width=300, bordermode=OUTSIDE)

    #if count_sentenses>0:
    #print(sentenses_array)
    image_label_sens = ttk.Label(window, text="Здесь будет ввыводиться текст предложения")
    image_label_sens.place(x=10, y=heighY + 50, anchor="w", heigh=100, width=1300, bordermode=OUTSIDE)

    btn_sentense = Button(window, text="следующее предложение", command=click_btn_next_sentense)
    btn_sentense.place(x=200, y=heighY + 50+ 50, anchor="w", heigh=30, width=300, bordermode=OUTSIDE)

    ################################  Поле со словами

    image_line_word  = ttk.Label(window, text="Здесь будет слова не разделенное на символы.")
    image_line_word.place(x=10, y=heighY*2 + 100, anchor="w", heigh=100, width=800, bordermode=OUTSIDE)

    label_word_sim = ttk.Label(window, text="слово по символам")
    label_word_sim.place(x=10, y=heighY*3  + 100, anchor="w", heigh=100, width=800, bordermode=OUTSIDE)
    #
    btn_word = Button(window, text="следующее слово", command=click_btn_next_word)
    btn_word.place(x=815, y=heighY*2 + 100, anchor="w", heigh=30, width=300, bordermode=OUTSIDE)


    ################################  Поле с символом
    image_line_sim = ttk.Label(window, text="Изображение символа.")
    image_line_sim.place(x=10, y=heighY * 4 + 100, anchor="w", heigh=100, width=200, bordermode=OUTSIDE)

    line_sim = Text(window)
    line_sim.place(x=215, y=heighY * 4 + 100, anchor="w", heigh=30, width=50, bordermode=OUTSIDE)

    btn_word = Button(window, text="Записать символ", command=click_btn_wtite_sim)
    btn_word.place(x=275, y=heighY * 4 + 100, anchor="w", heigh=30, width=300, bordermode=OUTSIDE)

    btn_next_simb = Button(window, text="Следующий символ", command=click_btn_next_sim)
    btn_next_simb.place(x=600, y=heighY * 4 + 100, anchor="w", heigh=30, width=300, bordermode=OUTSIDE)
    window.mainloop()