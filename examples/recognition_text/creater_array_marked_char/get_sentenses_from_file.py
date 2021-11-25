"""
This module make
23/11/2021
Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
import copy

def show_image (img):
    plt.figure(figsize=(20,20))
    plt.imshow(img)
    plt.show()


def string_recog(in_img):
    ret, threshold_gray2 = cv2.threshold(in_img, 120, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    ## (5) find and draw the upper and lower boundary of each lines
    hist = cv2.reduce(threshold_gray2, 1, cv2.REDUCE_AVG).reshape(-1)
    # print(hist)
    th = 15
    H, W = in_img.shape[:2]
    uppers = [y for y in range(H - 1) if hist[y] <= th and hist[y + 1] > th]
    lowers = [y for y in range(H - 1) if hist[y] > th and hist[y + 1] <= th]
    rotated = cv2.cvtColor(threshold_gray2, cv2.COLOR_GRAY2BGR)
    array_high_str = []
    for upp_line, low_line in zip(uppers, lowers):
        array_high_str.append(low_line - upp_line)
    median_high_str = int(np.median(np.array(array_high_str)))
    array_high_str = []
    for upp_line, low_line in zip(uppers, lowers):
        if (low_line - upp_line) > 10:
            if (low_line - upp_line) < (median_high_str * 1.5):
                array_high_str.append([upp_line, low_line])
                cv2.line(rotated, (0, upp_line), (W, upp_line), (255, 0, 0), 1)
                cv2.line(rotated, (0, low_line), (W, low_line), (0, 255, 0), 1)
            else:
                delta = (low_line - upp_line)
                if delta < (median_high_str * 2.5):
                    delta = int(delta / 2)
                    array_high_str.append([upp_line, low_line - delta])
                    array_high_str.append([upp_line + delta, low_line])
                    cv2.line(rotated, (0, upp_line), (W, upp_line), (255, 0, 0), 1)
                    cv2.line(rotated, (0, low_line - delta), (W, low_line - delta), (0, 255, 0), 1)
                    cv2.line(rotated, (0, upp_line + delta), (W, upp_line + delta), (255, 0, 0), 1)
                    cv2.line(rotated, (0, low_line), (W, low_line), (0, 255, 0), 1)
                else:
                    delta = int(delta / 3)
                    array_high_str.append([upp_line, low_line - delta * 2])
                    array_high_str.append([upp_line + delta, low_line - delta])
                    array_high_str.append([upp_line + delta * 2, low_line])
                    cv2.line(rotated, (0, upp_line), (W, upp_line), (255, 0, 0), 1)
                    cv2.line(rotated, (0, low_line - delta * 2), (W, low_line - delta * 2), (0, 255, 0), 1)
                    cv2.line(rotated, (0, low_line - delta), (W, low_line - delta), (0, 255, 0), 1)
                    cv2.line(rotated, (0, low_line), (W, low_line), (0, 255, 0), 1)

    #show_image(rotated)
    return array_high_str


def get_words(input_img):
    """
    Этот модуль разделяет строку на слова
    """
    ret, threshold_gray = cv2.threshold(input_img, 120, 255, 0)
    #show_image(threshold_gray)
    binary = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)

    # Show pictures
    #show_image(binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    dilation = cv2.dilate(binary,kernel,iterations = 5)
    #show_image(dilation)
    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(cnts)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    ROI_number = 0
    list_contur_num = []
    list_contur_coord = []
    list_img_words = []
    k = -1
    #print(cnts)
    for c in cnts:
        #area = cv2.contourArea(c)
        k += 1
        list_contur_num.append(k)
        x,y,w,h = cv2.boundingRect(c)
        #print(x,y,w,h)
        list_contur_coord.append([x,y,w,h])
        out_word = copy.copy(input_img[y:y+h+1, x:x+w+1])
        list_img_words.append(out_word)
        #show_image(out_word)
    return list_img_words


def bordr(mas_list, proc):
    part = 100/proc
    max_ll = int(max(mas_list) - max(mas_list)/part)
    max_two = int(max(mas_list) - max(mas_list)/(part*2))
    return max_ll, max_two


def min_area(mas_list, bor,proc):
    mas_len_area =[]
    len_are = 0
    part = 100/proc
    for i_a in range(len(mas_list)):
        if mas_list[i_a] < bor:
            len_are +=1
        else:
            if len_are > 0:
                mas_len_area.append(len_are)
            len_are = 0
    #print(mas_len_area)
    median = 0
    median_err = 0
    if len(mas_len_area):
        median = np.median(np.array(mas_len_area))
        median_err = np.median(np.array(mas_len_area)) + np.median(np.array(mas_len_area))/part
    #print('median = ',median)
    return median, int(median_err)


def get_char(input_img):
    """
    Этот модуль разделяет слова на символы
    """
    ret, threshold_gray3 = cv2.threshold(input_img, 120, 255, 0)
    line_sum = []
    #bw = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    #print('=============== threshold_gray3 =================')
    #show_image(threshold_gray3)
    img_exp = copy.copy(threshold_gray3)
    y,x = threshold_gray3.shape
    for i_x in range(x) :
        sum_com =0
        for i_y in range(y) :
            sum_com = sum_com + threshold_gray3[i_y,i_x]
        line_sum.append(sum_com)
    #print(line_sum)
    bor, mmm = bordr(line_sum, 10)
    median_c, median_err = min_area(line_sum, bor,5)
    len_are = 0
    list_img_char = []
    if median_err>15:
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
                        if len_are > median_c*1.5:
                            list_img_char.append(threshold_gray3[0:y, x_start:x_start+int(len_are/2)])
                            list_img_char.append(threshold_gray3[0:y, x_start+int(len_are/2):x_start+len_are])
                            for i_y in range(y) :
                                img_exp[i_y,x_start+int(len_are/2)] = 120
                            #show_image(threshold_gray3[0:y, x_start:x_start+len_are])
                        else:
                            list_img_char.append(threshold_gray3[0:y, x_start:x_start+len_are])
                        x_start = 0
                        len_are = 0
                    for i_y in range(y) :
                        img_exp[i_y,i_x] = 120
        #show_image(img_exp)
    return list_img_char, img_exp


heighY=40


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
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    ret, threshold_gray = cv2.threshold(gray, 127, 255, 0)
    #show_image(threshold_gray)
    binary = cv2.adaptiveThreshold(threshold_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
    # Show pictures
    #show_image(binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    dilation = cv2.dilate(binary, kernel, iterations=6)
    #show_image(dilation)
    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    ddd = gray.copy()
    ROI_number = 0
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
    print('list_contur_coord == ', len(list_contur_coord))
    for coord in list_contur_coord:
        out = copy.copy(ish_img[coord[1]:coord[1] + coord[3] + 1, coord[0]:coord[0] + coord[2] + 1])
        #show_image(out)
        array_high_str = string_recog(out)
        ish_img_rgb_frag = copy.copy(ish_img_rgb[coord[1]:coord[1] + coord[3] + 1, coord[0]:coord[0] + coord[2] + 1])
        for high_str in array_high_str:
            ssttrr = copy.copy(ish_img_rgb_frag[high_str[0] - 2:high_str[1] + 6, 0:])
            sentense_servis = {'img_sent': ssttrr, 'words': []}
            #show_image(ssttrr)
            list_img_words = get_words(ssttrr)
            for word in list_img_words:
                list_img_char, word_def = get_char(word)
                word_i = {'word_img': word,
                        'word_def': word_def,
                        'sim_word': []}
                #print('list_img_char = ', len(list_img_char))
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
