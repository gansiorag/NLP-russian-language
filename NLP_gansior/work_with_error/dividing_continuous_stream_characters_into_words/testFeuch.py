'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/02/01
Ending 2022//
    
'''

from termcolor import cprint
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
'''
from collections import Counter

def statTextList(textList):
    stat = Counter()
    for word in textList:
        stat[len(word)] +=1
    stat.most_common()
    # ' длина слова  -----  кол.слов'
    textOut = []
    for k in stat.most_common():
        textOut.append([k[0],k[1]])
    return textOut
        
def baseConcat(dd:dict, ReserchText:list, key:int, lengthFirstWord:int, ff2:int ):
    """_summary_

    Args:
        dd (dict): _description_
        ReserchText (list): _description_
        key (int): _description_
        lengthFirstWord (int): _description_
        ff2 (int): _description_

    Returns:
        _type_: _description_
    """
    indItem = 0
    while indItem < len(ReserchText['CountText']):
        if len(ReserchText['CountText'][indItem]) == lengthFirstWord and indItem <(len(ReserchText['CountText']) - 1):
            if len(ReserchText['CountText'][indItem +1]) == ff2:
                frag = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                if frag in dd[key]:
                    dd[key][frag]['k_l'] += 1
                    ReserchText['CountText'][indItem] = frag
                    ReserchText['CountText'].pop(indItem + 1)
                else:
                    dd[key][frag] = {'txt':'', 'k_l':0}
                    dd[key][frag]['txt'] = ReserchText['CountText'][indItem] + ' ' + ReserchText['CountText'][indItem + 1]
                    dd[key][frag]['k_l'] = 1
                    ReserchText['CountText'][indItem] = frag
                    ReserchText['CountText'].pop(indItem + 1)
        indItem +=1
    ReserchText[key]['CountText'] = ReserchText['CountText'].copy()
    ReserchText[key]['stat'] = statTextList(ReserchText['CountText'])
    return dd, ReserchText

def baseConcatLong(dd:dict, ReserchText:list, lengthFirstWord:int, ff2:int ):
    """_summary_

    Args:
        dd (dict): _description_
        ReserchText (list): _description_
        key (int): _description_
        lengthFirstWord (int): _description_
        ff2 (int): _description_

    Returns:
        _type_: _description_
    """
    indItem = 0
    key = lengthFirstWord*10 + ff2
    while indItem < len(ReserchText['CountText']):
        match key:
            case 44:
                if len(ReserchText['CountText'][indItem]) >= 4 and indItem <(len(ReserchText['CountText']) - 1):
                    if len(ReserchText['CountText'][indItem +1]) >= 4:
                        frag = ReserchText['CountText'][indItem][-4:] + ReserchText['CountText'][indItem + 1][:4]
                        if frag in dd[key]:
                            dd[key][frag]['k_l'] += 1
                        else:
                            dd[key][frag] = {'txt':'', 'k_l':1}
                            dd[key][frag]['txt'] = ReserchText['CountText'][indItem] + ' ' + ReserchText['CountText'][indItem + 1]
                        ReserchText['CountText'][indItem] = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                        ReserchText['CountText'].pop(indItem + 1)
            case 14,24,34:
                if len(ReserchText['CountText'][indItem]) in [1,2,3] and indItem <(len(ReserchText['CountText']) - 1):
                    if len(ReserchText['CountText'][indItem +1]) >= 4:
                        frag = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1][:4]
                        if frag in dd[key]:
                            dd[key][frag]['k_l'] += 1
                        else:
                            dd[key][frag] = {'txt':'', 'k_l':1}
                            dd[key][frag]['txt'] = ReserchText['CountText'][indItem] + ' ' + ReserchText['CountText'][indItem + 1][:4]
                        ReserchText['CountText'][indItem] = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                        ReserchText['CountText'].pop(indItem + 1)
            case _ :
                if len(ReserchText['CountText'][indItem]) == lengthFirstWord and indItem <(len(ReserchText['CountText']) - 1):
                    if len(ReserchText['CountText'][indItem +1]) == ff2:
                        frag = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                        if frag in dd[key]:
                            dd[key][frag]['k_l'] += 1
                        else:
                            dd[key][frag] = {'txt':'', 'k_l':1}
                            dd[key][frag]['txt'] = ReserchText['CountText'][indItem] + ' ' + ReserchText['CountText'][indItem + 1]
                        ReserchText['CountText'][indItem] = frag
                        ReserchText['CountText'].pop(indItem + 1)
        indItem +=1
    ReserchText[key]['CountText'] = ReserchText['CountText'].copy()
    ReserchText[key]['stat'] = statTextList(ReserchText['CountText'])
    return dd, ReserchText
    
def baseConcat33(dd:dict, ReserchText:list):
    """

    """
    indItem = 0
    while len(ReserchText['CountText']) > 1:
        if len(ReserchText['CountText'][indItem]) >= 3 and indItem <(len(ReserchText) - 1):
            if len(ReserchText['CountText'][indItem +1]) >= 3:
                frag = ReserchText['CountText'][indItem][-3:] + ReserchText['CountText'][indItem + 1][0:3]
                if frag in dd[33]:
                    dd[33][frag]['k_l'] += 1
                    ReserchText['CountText'][indItem] = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                    ReserchText['CountText'].pop(indItem + 1)
                else:
                    dd[33][frag] = {'txt':'', 'k_l':1}
                    dd[33][frag]['txt'] = ReserchText['CountText'][indItem][-3:] + ' ' + ReserchText['CountText'][indItem + 1][0:3]
                    ReserchText['CountText'][indItem] = ReserchText['CountText'][indItem] + ReserchText['CountText'][indItem + 1]
                    ReserchText['CountText'].pop(indItem + 1)
    ReserchText[33]['CountText'] = ReserchText['CountText'].copy()
    ReserchText[33]['stat'] = statTextList(ReserchText['CountText'])   
    return dd, ReserchText 


def connectLearn(FirstText:list)->str:
    rez = ''
    for k in FirstText:
        rez +=k
        
    Reserches={'FirstText':FirstText.copy(),
               'CountText':FirstText.copy(),
                11:{'CountText':[],
                   'stat':[]},
                12:{'CountText':[],
                   'stat':[]}, 
                13:{'CountText':[],
                   'stat':[]},
                14:{'CountText':[],
                   'stat':[]},
               
                22:{'CountText':[],
                   'stat':[]},
                23:{'CountText':[],
                   'stat':[]},
                24:{'CountText':[],
                   'stat':[]},
                33:{'CountText':[],
                   'stat':[]},
                34:{'CountText':[],
                   'stat':[]},
                44:{'CountText':[],
                   'stat':[]},
               'rez':rez}
    
    cprint(Reserches['FirstText'], 'red')
    dd ={11:{}, 12:{}, 13:{}, 14:{},
        22:{}, 23:{}, 24:{}, 33:{}, 34:{}, 44:{}, 331:{}, 332:{},
        }
    # 11
    dd, Reserches = baseConcat(dd, Reserches, 1, 1)

    # 12
    dd, Reserches = baseConcat(dd, Reserches, 1, 2)

    # 13
    dd, Reserches = baseConcat(dd, Reserches, 1, 3)
 
    # 14
    dd, Reserches = baseConcat(dd, Reserches, 1, 4)
  
    # 22
    dd, Reserches = baseConcat(dd, Reserches, 2, 2)
  
    # 23
    dd, Reserches = baseConcat(dd, Reserches, 2, 3)
    
    # 24
    dd, Reserches = baseConcat(dd, Reserches, 2, 4)
    
    # 33
    dd, Reserches = baseConcat(dd, Reserches, 3, 3)
    
    # 34
    dd, Reserches = baseConcat(dd, Reserches, 3, 4)
    
    # 44
    dd, Reserches = baseConcat(dd, Reserches, 4, 4)
    
    # 331 long 3
    dd, Reserches = baseConcatLong(dd, Reserches, 331 , 3, 1)
    
    # 332 long 3
    dd, Reserches = baseConcatLong(dd, Reserches, 332 , 3, 2)

    # 33
    dd, Reserches = baseConcat33(dd, Reserches)
    #print(ReserchText)
    #print(dd)
    # 33
    # dd, ReserchText = baseConcat33(dd, ReserchText)
    # print(ReserchText)
    # print(rez)
    # print(dd)
    return dd, rez, Reserches, Reserches[332]


def baseSeparator(is_list:str, baseDict:dict, indDict:int, firstStep:int, secondStep:int):
    # # разделение 2 - 1
    is_list = is_list.strip().split()
    text_rez = ''
    for frr in is_list:
        if len(frr)>(firstStep + secondStep):
            kk = firstStep + secondStep
            st =0
            frrControl = ''
            #print(len(frr))
            while kk<=(len(frr)):
                frag = frr[st:kk]
                #print(frag, st, kk)
                if frag in baseDict[indDict]:
                    frrControl += frr[st:st + firstStep]
                    text_rez += frr[st:st + firstStep] + ' '
                    st = st+firstStep
                    kk = st+1
                else:
                    text_rez += frr[st]
                    frrControl += frr[st]
                    st +=1
                    kk += 1
            if len(frrControl) < len(frr):
                text_rez += frr[len(frrControl):]
        elif len(frr)==(firstStep + secondStep):
            if frr in baseDict[indDict]:
                text_rez += baseDict[indDict][frr] + ' '
            else:
                text_rez +=(frr + ' ')
        else:
            text_rez +=(' '+ frr + ' ')
    return text_rez


def separatorWords(sourceText:str, dictFr:dict) ->list:
    # разделение 3 - 3
    kk=0
    #print(dd[33])
    text_rez = ''
    ichar =0
    while ichar < len(sourceText):
        frag =sourceText[ichar:ichar+6]
        #print('frag1 = ', frag)
        if frag in dictFr[33]:
            text_rez += sourceText[ichar: ichar +3] + ' '
            ichar += 3
        else:
            text_rez += sourceText[ichar]
            ichar += 1
    print('text_rez 33 = ', text_rez)
    
    # # разделение 2 - 3
    text_rez = baseSeparator(text_rez, dictFr, 23, 2, 3)
    print('text_rez 23 = ', text_rez)
    
    # # разделение 2 - 2
    text_rez = baseSeparator(text_rez, dictFr, 22, 2, 2)
    print('text_rez 22 = ', text_rez)

    # # разделение 3 - 1
    text_rez = baseSeparator(text_rez, dictFr, 31, 3, 1)
    print('text_rez 31 = ', text_rez)
    
    # # разделение 2 - 1
    text_rez = baseSeparator(text_rez, dictFr, 21, 2, 1)
    print('text_rez 2 1 = ', text_rez)
    
    # # разделение 1 - 2
    text_rez = baseSeparator(text_rez, dictFr, 12, 1, 2)
    print('text_rez 1 2 = ', text_rez)
    
    # # разделение 1 - 1
    text_rez = baseSeparator(text_rez, dictFr, 11, 1, 1)
    print('text_rez 1 1 = ', text_rez)
    
    
    return text_rez
    
    
    
if __name__ == '__main__':
    name=''
    indItem = 0
    IshText = ['d', 'c', 'b', 'hg', 'f', 'k', 'df', 'r', 'dff', 'r']
    ReserchText = IshText.copy()
    dictFr, RezText = connectLearn(ReserchText)
    cprint(f'{RezText}' , 'red', attrs=['bold'])
    cprint(f'{dictFr}' , 'blue', attrs=['bold'])
    DubleText = separatorWords(RezText, dictFr)
    cprint(f'{DubleText}' , 'red', attrs=['bold'])
    cprint(f'{IshText}' , 'green', attrs=['bold'])
    s = 'python'
    print(s[:8])