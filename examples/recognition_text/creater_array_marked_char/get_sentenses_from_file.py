"""
This module make
23/11/2021
Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
import copy
from collections import Counter

def show_image (img):
    plt.figure(figsize=(20,20))
    plt.imshow(img)
    plt.show()


def force_clear_paran(name_is_file, param:int):
    gray_c = cv2.imread(name_is_file, 0)
    ret, threshold_gray_c = cv2.threshold(gray_c, param, 255, 0)
    show_image(threshold_gray_c)
    com_num_row = threshold_gray_c.shape[0]
    list_hist_c = []
    cc_cc_c = Counter()
    for y_list in range(threshold_gray_c.shape[0]):
        summ_string = 0
        for x_list in range(threshold_gray_c.shape[1]):
           summ_string += threshold_gray_c[y_list, x_list]
        list_hist_c.append(summ_string)
        cc_cc_c[summ_string]+=1
    return float(cc_cc_c[max(list_hist_c)]/com_num_row)


def string_recog(in_img):
    ret, threshold_gray2 = cv2.threshold(in_img, 120, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    #show_image(threshold_gray2)
    ## (5) find and draw the upper and lower boundary of each lines
    hist = cv2.reduce(threshold_gray2, 1, cv2.REDUCE_AVG).reshape(-1)
    th = 15
    H, W = in_img.shape[:2]
    uppers = [y for y in range(H - 1) if hist[y] <= th and hist[y + 1] > th]
    lowers = [y for y in range(H - 1) if hist[y] > th and hist[y + 1] <= th]
    rotated = cv2.cvtColor(threshold_gray2, cv2.COLOR_GRAY2BGR)
    array_high_str = []
    int_err = 6
    if len(uppers) > 0 and len(lowers) > 0:
        for upp_line, low_line in zip(uppers, lowers):
            array_high_str.append(low_line - upp_line)
        median_high_str = int(np.median(np.array(array_high_str)))
        array_high_str = []
        if median_high_str < 27: median_high_str = 28
        last_low = 0
        for upp_line, low_line in zip(uppers, lowers):
            if (low_line - upp_line) > 27:
                if (low_line - upp_line) < (median_high_str * 1.5):
                    array_high_str.append([upp_line - int_err, low_line])
                    cv2.line(rotated, (0, upp_line - int_err), (W, upp_line - int_err), (255, 0, 0), 1)
                    cv2.line(rotated, (0, low_line + int_err), (W, low_line + int_err), (0, 255, 0), 1)
                    if low_line > last_low: last_low = low_line
                else:
                    delta = (low_line - upp_line)
                    if delta < (median_high_str * 2.5):
                        delta = int(delta / 2)
                        array_high_str.append([upp_line - int_err, low_line - delta])
                        array_high_str.append([upp_line + delta - int_err, low_line])
                        cv2.line(rotated, (0, upp_line - int_err), (W, upp_line - int_err), (255, 0, 0), 1)
                        cv2.line(rotated, (0, low_line - delta + int_err), (W, low_line - delta + int_err), (0, 255, 0), 1)
                        cv2.line(rotated, (0, upp_line + delta - int_err), (W, upp_line + delta - int_err), (255, 0, 0), 1)
                        cv2.line(rotated, (0, low_line), (W, low_line), (0, 255, 0), 1)
                        if low_line > last_low: last_low = low_line
                    else:
                        delta = int(delta / 3)
                        array_high_str.append([upp_line - int_err, low_line - delta * 2])
                        array_high_str.append([upp_line + delta - int_err, low_line - delta])
                        array_high_str.append([upp_line + delta * 2 - int_err, low_line])
                        cv2.line(rotated, (0, upp_line - int_err), (W, upp_line - int_err), (255, 0, 0), 1)
                        cv2.line(rotated, (0, low_line - delta * 2), (W, low_line - delta * 2), (0, 255, 0), 1)
                        cv2.line(rotated, (0, low_line - delta - int_err), (W, low_line - delta - int_err), (255, 0, 0), 1)
                        cv2.line(rotated, (0, low_line), (W, low_line), (0, 255, 0), 1)
                        if low_line > last_low: last_low = low_line
        if last_low > 10:
            array_high_str.append([last_low + 2, H - 3])
            cv2.line(rotated, (0, last_low + 2), (W, last_low + 2), (255, 0, 0), 1)
            cv2.line(rotated, (0, H - 3), (W, H - 3), (0, 255, 0), 1)

    #show_image(rotated)
    return array_high_str


def critery_empty_str(inp_img):
    summ_string = 0
    ret, threshold_gray_v = cv2.threshold(inp_img, 120, 255, 0)
    max_pic = inp_img.shape[0]*inp_img.shape[1]*255
    for y_list in range(inp_img.shape[0]):
        for x_list in range(inp_img.shape[1]):
           summ_string += threshold_gray_v[y_list, x_list]
    if summ_string < max_pic : return True
    return False


def get_words(input_img):
    """
    Этот модуль разделяет строку на слова
    """
    list_img_words = []
    ret, threshold_gray = cv2.threshold(input_img, 120, 255, 0)
    binary = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilation = cv2.dilate(binary, kernel, iterations=5)
    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    ROI_number = 0
    list_contur_num = []
    list_contur_coord = []
    k =-1
    for c in cnts:
        # area = cv2.contourArea(c)
        k +=1
        list_contur_num.append(k)
        x, y, w, h = cv2.boundingRect(c)
        list_contur_coord.append([x, y, w, h])
        out_word = copy.copy(input_img[y:y + h + 1, x:x + w + 1])
        list_img_words.append(out_word)
        # show_image(out_word)
    return list_img_words


def bordr(mas_list, proc):
    part = 100/proc
    max_ll = int(max(mas_list) - max(mas_list)/part)
    max_two = int(max(mas_list) - max(mas_list)/(part*2))
    return max_ll, max_two


def min_area(mas_list, bor, proc, max_y):
    mas_len_area = []
    len_are = 0
    part = 100 / proc
    for i_a in range(len(mas_list)):
        if mas_list[i_a] < max_y:
            len_are += 1
        else:
            if len_are > 5:
                mas_len_area.append(len_are)
            len_are = 0
    median = 0
    median_err = 0
    if len(mas_len_area):
        median = np.median(np.array(mas_len_area))
        median_err = np.median(np.array(mas_len_area)) + np.median(np.array(mas_len_area)) / part
    return median, int(median_err)

def force_clear_word(gray):
    ret, threshold_gray = cv2.threshold(gray, 170, 255, 0)
    #show_image(threshold_gray)
    com_num_row = threshold_gray.shape[1]
    list_hist = []
    cc_cc = Counter()
    for x_list in range(threshold_gray.shape[1]):
        summ_string = 0
        for y_list in range(threshold_gray.shape[0]):
           summ_string += threshold_gray[y_list, x_list]
        list_hist.append(summ_string)
        cc_cc[summ_string]+=1
    return float(cc_cc[max(list_hist)]/com_num_row)


def multi_simb(img_exp,list_img_char, threshold_gray3,y, x_start,len_are, num_mul):
    if num_mul<100:
        for k in range(num_mul):
            list_img_char.append(threshold_gray3[0:y,x_start+int(len_are*k/num_mul):x_start+int(len_are*(k+1)/num_mul)])
            for i_y in range(y) :
                img_exp[i_y,x_start+int(len_are*k/num_mul)] = 120
    else:
        n_m_l = int(len_are/31)
        for k in range(n_m_l):
            list_img_char.append(threshold_gray3[0:y,x_start+int(len_are*k/n_m_l):x_start+int(len_are*(k+1)/n_m_l)])
            for i_y in range(y) :
                img_exp[i_y,x_start+int(len_are*k/n_m_l)] = 120


def get_char(input_img):
    """
    Этот модуль разделяет слова на символы
    """
    param = 150
    ret, threshold_gray3 = cv2.threshold(input_img, param, 255, 0)
    crit = force_clear_word(threshold_gray3)
    if crit < 0.35 : param = 170
    ret, threshold_gray3 = cv2.threshold(input_img, param, 255, 0)
    line_sum = []
    #bw = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    #show_image(threshold_gray3)
    img_exp = copy.copy(threshold_gray3)
    y,x = threshold_gray3.shape
    max_y = y*255
    for i_x in range(x) :
        sum_com =0
        for i_y in range(y) :
            sum_com = sum_com + threshold_gray3[i_y,i_x]
        line_sum.append(sum_com)
    bor, mmm = bordr(line_sum, 10)
    median_c, median_err = min_area(line_sum, bor,5,max_y)
    len_are = 0
    list_img_char = []
    if median_err>12:
        x_start = 0
        for i_x in range(x) :
            if line_sum[i_x] <= bor:
                if x_start == 0:
                    x_start = i_x
                len_are +=1
            else:
                if len_are <= median_err and len_are>0 and line_sum[i_x]<mmm:
                    len_are +=1
                else:
                    if len_are> 0:
                        if len_are > 32 and len_are < 69:
                            list_img_char.append(threshold_gray3[0:y, x_start:x_start+int(len_are/2)])
                            list_img_char.append(threshold_gray3[0:y, x_start+int(len_are/2):x_start+len_are])
                            for i_y in range(y) :
                                img_exp[i_y,x_start+int(len_are/2)] = 120
                            #show_image(threshold_gray3[0:y, x_start:x_start+len_are])
                        elif len_are > 69 and len_are < 100:
                            multi_simb(img_exp, list_img_char, threshold_gray3, y, x_start,len_are, 3)
                        elif len_are >= 100 and len_are < 130:
                            multi_simb(img_exp, list_img_char, threshold_gray3, y, x_start,len_are, 4)
                        elif len_are >= 130:
                            multi_simb(img_exp, list_img_char, threshold_gray3, y, x_start,len_are, 120)
                        else:
                            list_img_char.append(threshold_gray3[0:y, x_start:x_start+len_are])
                        x_start = 0
                        len_are = 0
                    for i_y in range(y) :
                        img_exp[i_y,i_x] = 120
        #show_image(img_exp)
    return list_img_char, img_exp


heighY=40


def force_clear(gray):
    ret, threshold_gray = cv2.threshold(gray, 170, 255, 0)
    com_num_row = threshold_gray.shape[0]
    list_hist = []
    cc_cc = Counter()
    for y_list in range(threshold_gray.shape[0]):
        summ_string = 0
        for x_list in range(threshold_gray.shape[1]):
           summ_string += threshold_gray[y_list, x_list]
        list_hist.append(summ_string)
        cc_cc[summ_string]+=1
    return float(cc_cc[max(list_hist)]/com_num_row)


def sentenses(name_jpg:str):
    """

    :param name_jpg: name file with text
    :return: array sentenses in text
    simbol = {'img_sim':[],
          'value_sim':''}

    word = {'word_is':[],
            'word_def':[],
            'sim_word':[simbol]}

    sentenses = {'img_sent': ish_img_rgb_frag, 'words': [word]}
    sentenses_array = [ sentenses, ]
    """

    sentenses_array = []
    gray = cv2.imread(name_jpg, 0)
    param = 0
    koef = force_clear(gray)
    if koef < 0.35:
        param = 170 - int((0.35 - koef) * 100 * 5)
    else:
        param = 120
    ret, threshold_gray = cv2.threshold(gray, param, 255, 0)
    list_hist = []
    for y_list in range(threshold_gray.shape[0]):
        summ_string = 0
        for x_list in range(threshold_gray.shape[1]):
            summ_string += threshold_gray[y_list, x_list]
        list_hist.append(summ_string)
    border = int(max(list_hist) * 0.98)
    for y_list in range(threshold_gray.shape[0]):
        summ_string = 0
        for x_list in range(threshold_gray.shape[1]):
            summ_string += threshold_gray[y_list, x_list]
        if summ_string > border:
            for x_list in range(threshold_gray.shape[1]):
                threshold_gray[y_list, x_list] = 255
    binary = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilation = cv2.dilate(binary, kernel, iterations=6)
    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    ddd = gray.copy()
    list_contur_num = []
    list_contur_coord = []
    k = -1
    for c in cnts:
        area = cv2.contourArea(c)
        k += 1
        if area > 10000:
            list_contur_num.append(k)
            x, y, w, h = cv2.boundingRect(c)
            list_contur_coord.append([x, y, w, h])
            cv2.rectangle(ddd, (x, y), (x + w, y + h), (36, 255, 12), 3)

    ish_img = cv2.imread(name_jpg, 0)
    ish_img_rgb = cv2.imread(name_jpg, 0)
    for coord in list_contur_coord:
        out = copy.copy(ish_img[coord[1]:coord[1] + coord[3] + 1, coord[0]:coord[0] + coord[2] + 1])
        array_high_str = string_recog(out)
        ish_img_rgb_frag = copy.copy(ish_img_rgb[coord[1]:coord[1] + coord[3] + 1, coord[0]:coord[0] + coord[2] + 1])
        for high_str in array_high_str:
            ssttrr = copy.copy(ish_img_rgb_frag[high_str[0] - 2:high_str[1] + 6, 0:])
            if critery_empty_str(ssttrr):
                sentense_servis = {'img_sent': ssttrr, 'words': []}
                #show_image(ssttrr)
                list_img_words = get_words(ssttrr)
                for word in list_img_words:
                    list_img_char, word_def = get_char(word)
                    word_i = {'word_img': word,
                            'word_def': word_def,
                            'sim_word': []}
                    for im_s in list_img_char:
                        simbol = {'img_sim': im_s,
                                  'value_sim': ''}
                        word_i['sim_word'].append(simbol)
                    sentense_servis['words'].append(word_i)
                sentenses_array.append(sentense_servis)
    return sentenses_array


if __name__ == '__main__':
    name_file = '/examples/recognition_text/creater_array_marked_char/data_set_jpg/doc00030020210414100706_001.jpg'
    sentenses_array = sentenses(name_file)
    print(len(sentenses_array))
