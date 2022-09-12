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


def baseConcat(dd:dict, ReserchText:list, key:int, lengthFirstWord:int, ff2:int ):
    """

    """
    indItem = 0
    while indItem < len(ReserchText):
        if len(ReserchText[indItem]) == lengthFirstWord and indItem <(len(ReserchText) - 1):
            if len(ReserchText[indItem +1]) == ff2:
                frag = ReserchText[indItem] + ReserchText[indItem + 1]
                dd[key][frag] = ReserchText[indItem] + ' ' + ReserchText[indItem + 1]
                ReserchText[indItem] = frag
                ReserchText.pop(indItem + 1)
        indItem +=1
    return dd, ReserchText
    
def baseConcat33(dd:dict, ReserchText:list):
    """

    """
    indItem = 0
    while indItem < len(ReserchText):
        if len(ReserchText[indItem]) >= 3 and indItem <(len(ReserchText) - 1):
            if len(ReserchText[indItem +1]) >= 3:
                frag = ReserchText[indItem][-3:] + ReserchText[indItem + 1][0:3]
                dd[33][frag] = ReserchText[indItem][-3:] + ' ' + ReserchText[indItem + 1][0:3]
                ReserchText[indItem] = ReserchText[indItem] + ReserchText[indItem + 1]
                ReserchText.pop(indItem + 1)
        indItem +=1
    return dd, ReserchText 


def connectLearn(ReserchText:list)->str:
    rez = ''
    for k in ReserchText:
        rez +=k
    cprint(ReserchText, 'red')
    dd ={11:{}, 12:{}, 21:{}, 31:{},
        22:{}, 23:{},
        33:{}}
    # 11
    dd, ReserchText = baseConcat(dd, ReserchText, 11 , 1, 1)

    # 12
    dd, ReserchText = baseConcat(dd, ReserchText, 12 , 1, 2)

    # 21
    dd, ReserchText = baseConcat(dd, ReserchText, 21 , 2, 1)
 
    # 31
    dd, ReserchText = baseConcat(dd, ReserchText, 31 , 3, 1)
  
    # 22
    dd, ReserchText = baseConcat(dd, ReserchText, 22 , 2, 2)
  
    # 23
    dd, ReserchText = baseConcat(dd, ReserchText, 23 , 2, 3)
 
    # 33
    dd, ReserchText = baseConcat33(dd, ReserchText)
    #print(ReserchText)
    #print(dd)
    # 33
    # dd, ReserchText = baseConcat33(dd, ReserchText)
    # print(ReserchText)
    # print(rez)
    # print(dd)
    return dd, rez


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