from termcolor import colored


def baseConcat(dd:dict, ttt:list, key:int, ff1:int, ff2:int ):
    """

    """
    indItem = 0
    while indItem < len(ttt):
        if len(ttt[indItem]) == ff1 and indItem <(len(ttt) - 1):
            if len(ttt[indItem +1]) == ff2:
                frag = ttt[indItem] + ttt[indItem + 1]
                dd[key][frag] = ttt[indItem] + ' ' + ttt[indItem + 1]
                ttt[indItem] = frag
                ttt.pop(indItem + 1)
        indItem +=1
    return dd, ttt
    
def baseConcat33(dd:dict, ttt:list):
    """

    """
    indItem = 0
    while indItem < len(ttt):
        if len(ttt[indItem]) >= 3 and indItem <(len(ttt) - 1):
            if len(ttt[indItem +1]) >= 3:
                frag = ttt[indItem][-3:] + ttt[indItem + 1][0:3]
                dd[33][frag] = ttt[indItem][-3:] + ' ' + ttt[indItem + 1][0:3]
                ttt[indItem] = ttt[indItem] + ttt[indItem + 1]
                ttt.pop(indItem + 1)
        indItem +=1
    return dd, ttt 
    
#11
indItem = 0
ttt = ['d', 'c', 'b', 'hg', 'f', 'k', 'df', 'r', 'dff', 'r']
rez = ''
for k in ttt:
    rez +=k
print(colored(ttt, 'red'))
dd ={11:{}, 12:{}, 21:{}, 31:{},
     22:{}, 23:{},
     33:{}}
# 11
dd, ttt = baseConcat(dd, ttt, 11 , 1, 1)
print(ttt)
print(dd)
print()
# 12
dd, ttt = baseConcat(dd, ttt, 12 , 1, 2)
print(ttt)
print(dd)
print()
# 21
dd, ttt = baseConcat(dd, ttt, 12 , 2, 1)
print(ttt)
print(dd)
print()
# 31
dd, ttt = baseConcat(dd, ttt, 31 , 3, 1)
print(ttt)
print(dd)
print()
# 22
dd, ttt = baseConcat(dd, ttt, 22 , 2, 2)
print(ttt)
print(dd)
print()
# 23
dd, ttt = baseConcat(dd, ttt, 23 , 2, 3)
print(ttt)
print(dd)
# 33
dd, ttt = baseConcat33(dd, ttt)
print(ttt)
print(dd)
# 33
dd, ttt = baseConcat33(dd, ttt)
print(ttt)
print(rez)
print(dd)