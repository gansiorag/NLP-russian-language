'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//
    
'''
    
from termcolor import cprint
import inspect
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
    
    
Shows which module is currently running
cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
'''
    
import os
import sys
import glob
import zipfile
from collections import Counter
 
nameProjectStart = 'workWithDataSet'
nameProject = 'workWithDataSet'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + '/' + nameProject + '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)
    
def basesWork(namePathStart, namePathRez):
    listFiles = glob.glob(namePathStart + '/*.zip')
    print(listFiles)
    for nn in listFiles:
        print(nn)
        with zipfile.ZipFile(nn, 'r') as zip_ref:
            zip_ref.extractall(namePathRez)
    
    
def prog2():
    pass
    
    
if __name__ == '__main__':
    namePathStart='/media/al/Seagate Backup Plus Drive/Библиотека Либрусек. Часть 1/'
    namePathRez='/media/al/Seagate Backup Plus Drive/Библиотека Либрусек. Часть 1/unzipFiles6/'
    basesWork(namePathStart, namePathRez)
    prog2()