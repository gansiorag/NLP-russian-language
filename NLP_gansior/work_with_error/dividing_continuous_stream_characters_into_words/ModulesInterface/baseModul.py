'''
 This module make

Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022//
Ending 2022//

'''

# import sys
# import os
# from termcolor import cprint


# nameProjectStart = 'NLP-russian-language'
# nameProject = 'NLP-russian-language/NLP_gansior/work_with_error/dividing_continuous_stream_characters_into_words'
# cprint(os.getcwd(), 'green')
# PathPrj = os.getcwd().split(nameProjectStart)[0] + nameProject + '/'
# cprint(PathPrj, 'blue')
# sys.path.append(PathPrj)

geom_par = {'rootGeometry': "1750x900",
            'widthLabe': 500,
            'widthBt': 300,
            'heigh_y': 10,
            'P2widthW': 560
            }

var_sit = {'name_file': '',
           'all_text': '',
           'token_text': {'text': '',
                          'stat_1+N': {},
                          #   'stat_1+N': {'com': 0,
                          #                'source 1+1': {'com': 0},
                          #                'source 1+2': {'com': 0},
                          #                'source 1+3': {'com': 0},
                          #                'source 1+4': {'com': 0},
                          #                'source 1+lg': {'com': 0}}
                          'stat_2+N': {},
                          #   'stat_2+N': {'com': 0,
                          #                'source 2+2': {'com': 0},
                          #                'source 2+3': {'com': 0},
                          #                'source 2+4': {'com': 0},
                          #                'source 2+lg': {'com': 0}
                          'stat_3+N': {},
                          #   'stat_3+N': {'com': 0,
                          #                'source 3+3': {'com': 0},
                          #                'source 3+4': {'com': 0},
                          #                'source 3+lg': {'com': 0}
                          'stat_4+N': {},
                          #   'stat_4+N': {'com': 0,
                          #                'source 4+4': {'com': 0},
                          #                'source 4+lg': {'com': 0}
                          'stat_lg+lg': {}
                          },
           'stat_word_token_text': [],
           'stat_len_word_token_text': [],
           'text_exp': '',
           'result_text': '',
           'searched_text': {'text': '',
                             'stat_1+N': {},
                             'stat_2+N': {},
                             'stat_3+N': {},
                             'stat_4+N': {},
                             'stat_lg+lg': {},                               
                             },
           'stat_result_text': [],
           'stat_simb_all_text': {},
           'dict_model': [],
           'source 1+1': {'com': 0},
           'source 1+2': {'com': 0},
           'source 1+3': {'com': 0},
           'source 1+4': {'com': 0},
           'source 1+lg': {'com': 0}
           }
