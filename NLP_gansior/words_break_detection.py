import re
from collections import Counter

def get_stat_break(name:str):
    rul_one = re.compile(r'\s[а-я]\s')
    rul_two = re.compile(r'[.,?!«»;:“)(№0-9]')
    rul_three = re.compile(r'\s+')
    ttt =''
    with open(name, 'r') as i_f:
        for line in i_f:
            if line.strip():
                tt = rul_one.sub(' ',line.strip().lower())
                tt = ' '.join(tt.split('\n'))
                tt = tt.replace('\n', ' ')
                tt = tt.replace('”', ' ')
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
    answer = ''
    if i<10: answer = '0' + str(i)
    else:
        answer = str(i)
    return answer
        

if __name__ == '__main__':
    # for i in range(1,19):
    #     num = get_num(i)
    #     n_f = f'/media/al/work1/NLP/Datasets/И.В. Сталин. Собрание сочинений в 18 томах/{num}.txt'
    #     get_stat_break(n_f)
    n_f = f'/media/al/work1/NLP/Datasets/И.В. Сталин. Собрание сочинений в 18 томах/01.txt'
    get_stat_break(n_f)
    statis = Counter()
    ttt = get_stat_break(n_f).split()
    kk = 0 
    dd = {}
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

    # print(statis.most_common(100))
    # print(len(statis))
    # print(len_dd)
    #print(dd)
    text_exp = ''.join(ttt)
    print(text_exp[:500])
    print()
    text_rez = ''
    kk = 0 
    
    for tt in text_exp:
        frag =''
        if kk<(len(text_exp)-6):
            for ik in range(6):
                frag += text_exp[kk + ik]
            #print(frag)
            if frag in dd:
                text_rez += dd[frag]
                kk += 3
            else:
                text_rez += text_exp[kk]
                kk += 1
        #if kk >100: break
    print(text_rez[0:600])