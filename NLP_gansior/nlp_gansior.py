"""
This module make

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
import re
from pprint import pprint
from test_data import test_one
from config_nlp import sentence_sep

class NLP_gansior():

    def __init__(self, first_text:str):
        self.first_text = first_text
        self.sentence = self.get_sentenses()

    def get_sentenses(self):
        # delete part with one simbols
        first_step= []
        servis_list = self.first_text.split('\n')
        servis_sentence = []
        for part in servis_list:
            if len(part) > 1 :
                if part.strip()[-1] not in sentence_sep:
                    servis_sentence.append(part.strip())
                else:
                    servis_sentence.append(part.strip())
                    work_sentence = ' '.join(servis_sentence)
                    work_sentence = work_sentence.replace('- ','')
                    first_step.append(re.sub(r'^\s+', ' ', work_sentence))
                    servis_sentence = []
        pprint(first_step)
        print(len(first_step))
        return first_step



if __name__ == '__main__':
    work_text = NLP_gansior(test_one)