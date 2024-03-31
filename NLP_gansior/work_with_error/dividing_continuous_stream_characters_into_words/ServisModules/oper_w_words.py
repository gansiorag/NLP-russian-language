from collections import Counter
from copy import deepcopy as cp


def del_word_len_1(i_txt: str):
    """_summary_

    Args:
        i_txt (str): _description_

    Returns:
        _type_: _description_
    """
    r_txt = ''
    s_txt = i_txt.split()
    a_txt_list = []
    lk = 0

    # 1 + 1
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 1 and len(s_txt[lk + 1]) == 1:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])
    # 1 + 2
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 1 and len(s_txt[lk + 1]) == 2:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 1 + 3
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 1 and len(s_txt[lk + 1]) == 3:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 1 + 4
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 1 and len(s_txt[lk + 1]) == 4:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 1 + lg
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 1 and len(s_txt[lk + 1]) > 4:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 2 + 2
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 2 and len(s_txt[lk + 1]) == 2:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 2 + 3
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 2 and len(s_txt[lk + 1]) == 3:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 2 + 4
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 2 and len(s_txt[lk + 1]) == 4:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    # 2 + lg
    s_txt = cp(a_txt_list)
    a_txt_list = []
    lk = 0
    while (lk < (len(s_txt) - 1)):
        if len(s_txt[lk]) == 2 and len(s_txt[lk + 1]) >4:
            a_txt_list.append(s_txt[lk] + s_txt[lk + 1])
            lk += 2
        else:
            a_txt_list.append(s_txt[lk])
            lk += 1
    if lk == (len(s_txt) - 1):
        a_txt_list.append(s_txt[-1])

    r_txt = ' '.join(a_txt_list).strip()

    return r_txt


def stat_combi_n_n(is_txt: str):
    """AI is creating summary for stat_combi_n_n

    Args:
        is_txt (str): [description]
    """
    stat = {}
    stat['source 1+1'] = Counter()
    stat['source 1+2'] = Counter()
    stat['source 1+3'] = Counter()
    stat['source 1+4'] = Counter()
    stat['source 1+lg'] = Counter()
    tt = is_txt.split()
    ki = 0
    # print('tt = ', tt)
    for word in tt[: -1]:
        dword = tt[ki + 1]
        if len(word) == 1 and len(dword) == 1:
            stat['source 1+1'][word + '_' + dword] += 1
            stat['source 1+1']['com'] += 1
        if len(word) == 1 and len(dword) == 2:
            stat['source 1+2'][word + '_' + dword] += 1
            stat['source 1+2']['com'] += 1
        if len(word) == 1 and len(dword) == 3:
            stat['source 1+3'][word + '_' + dword] += 1
            stat['source 1+3']['com'] += 1
        if len(word) == 1 and len(dword) == 4:
            stat['source 1+4'][word + '_' + dword] += 1
            stat['source 1+4']['com'] += 1
        if len(word) == 1 and len(dword) > 4:
            stat['source 1+lg'][word + '_' + dword] += 1
            stat['source 1+lg']['com'] += 1
        # if len(word) == 1 and len(dword) == 2:
        #     stat['source 1+2']['com'] += 1

        ki += 1

    text_out = ' сочетание  -----  кол.\n'
    text_out += ("source 1+1 кол-во слов  -----  " +
                 f"{stat['source 1+1']['com']:8}\n")
    for k in stat['source 1+1']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 1+1'][k]:8}\n")
            stat[k] = stat['source 1+1'][k]

    text_out += ("source 1+2 кол-во слов  -----  " +
                 f"{stat['source 1+2']['com']:8}\n")
    for k in stat['source 1+2']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 1+2'][k]:8}\n")
            stat['source 1+2'][k] = stat['source 1+2'][k]

    text_out += ("source 1+3 кол-во слов  -----  " +
                 f"{stat['source 1+3']['com']:8}\n")
    for k in stat['source 1+3']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 1+3'][k]:8}\n")
            stat['source 1+3'][k] = stat['source 1+3'][k]

    text_out += ("source 1+4 кол-во слов  -----  " +
                 f"{stat['source 1+4']['com']:8}\n")
    for k in stat['source 1+4']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 1+4'][k]:8}\n")
            stat['source 1+4'][k] = stat['source 1+4'][k]

    text_out += ("source 1+lg кол-во слов  -----  " +
                 f"{stat['source 1+lg']['com']:8}\n")
    for k in stat['source 1+lg']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 1+lg'][k]:8}\n")
            stat['source 1+lg'][k] = stat['source 1+lg'][k]

    return text_out, stat


def stat_combi_2_n(is_txt: str):
    """AI is creating summary for stat_combi_n_n

    Args:
        is_txt (str): [description]
    """
    stat = {}
    stat['source 2+2'] = Counter()
    stat['source 2+3'] = Counter()
    stat['source 2+4'] = Counter()
    stat['source 2+lg'] = Counter()
    tt = is_txt.split()
    ki = 0
    # print('tt = ', tt)
    for word in tt[: -1]:
        dword = tt[ki + 1]
        if len(word) == 2 and len(dword) == 2:
            stat['source 2+2'][word + '_' + dword] += 1
            stat['source 2+2']['com'] += 1
        if len(word) == 2 and len(dword) == 3:
            stat['source 2+3'][word + '_' + dword] += 1
            stat['source 2+3']['com'] += 1
        if len(word) == 2 and len(dword) == 4:
            stat['source 2+4'][word + '_' + dword] += 1
            stat['source 2+4']['com'] += 1
        if len(word) == 2 and len(dword) > 4:
            stat['source 2+lg'][word + '_' + dword] += 1
            stat['source 2+lg']['com'] += 1
        # if len(word) == 1 and len(dword) == 2:
        #     stat['source 1+2']['com'] += 1

        ki += 1

    text_out = ' сочетание  -----  кол.\n'
    text_out += ("source 2+2 кол-во слов  -----  " +
                 f"{stat['source 2+2']['com']:8}\n")
    for k in stat['source 2+2']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 2+2'][k]:8}\n")
            stat[k] = stat['source 2+2'][k]

    text_out += ("source 2+3 кол-во слов  -----  " +
                 f"{stat['source 2+3']['com']:8}\n")
    for k in stat['source 2+3']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 2+3'][k]:8}\n")
            stat['source 2+3'][k] = stat['source 2+3'][k]

    text_out += ("source 2+4 кол-во слов  -----  " +
                 f"{stat['source 2+4']['com']:8}\n")
    for k in stat['source 2+4']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 2+4'][k]:8}\n")
            stat['source 2+4'][k] = stat['source 2+4'][k]

    text_out += ("source 2+lg кол-во слов  -----  " +
                 f"{stat['source 2+lg']['com']:8}\n")
    for k in stat['source 2+lg']:
        if k != 'com':
            text_out += (f"{k}  -----  " + f"{stat['source 2+lg'][k]:8}\n")
            stat['source 2+lg'][k] = stat['source 2+lg'][k]

    return text_out, stat
