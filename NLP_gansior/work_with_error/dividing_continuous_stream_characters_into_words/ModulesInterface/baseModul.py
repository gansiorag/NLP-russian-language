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

nameProjectStart = 'NLP-russian-language'
nameProject = 'NLP-russian-language/NLP_gansior/work_with_error'
cprint(os.getcwd(), 'green')
PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
cprint(PathPrj, 'blue')
sys.path.append(PathPrj)

geomPar = {'rootGeometry':"1750x700",
            'widthLabe':500,
            'widthBt' : 300,
            'heighY' : 10,
            'P2widthW' : 560
          }