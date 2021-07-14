from gensim.models import KeyedVectors
import re
import zipfile
import os

class wordprocessing:
    slova={}
    lemmatizator = {}
    slovoStop = {}
    rullmas = []
    token=[]
    AllTizer=[]
    kolTiz=0
    wv=KeyedVectors

# Загрузка словаря
def load_slovar(filename):
    ishFile = open(filename, 'r')
    ishText = ishFile.readline()
    slova = {}
    while ishText:
        slovo = ishText.split(' ')
        slova[slovo[0].strip()] = int(slovo[1])
        ishText = ishFile.readline()
    return slova

# Загрузка лемматизатора
def load_lemmatizator(namefile):
    lemmatVoc = {}
    namefiledubl=os.path.basename(namefile).split(".")[0]+".lem"
    with zipfile.ZipFile(namefile) as myzip:
        with myzip.open(namefiledubl) as myfile:
            for line in myfile:
                linetxt =line.decode('utf-8')
                slovo = linetxt.split('@')
                lemmatVoc[slovo[0].strip()] = slovo[1].strip()
    return lemmatVoc


# Загрузка стоп слов
def load_stopSlova(namefile):
    stop_slovo = {}
    with open(namefile, 'r') as myfile:
        for linetxt in myfile :
            stop_slovo[linetxt.strip()] = "1"
    return stop_slovo


def rulls():
    rull_mas = []
    rull_mas.append(re.compile(r'[^а-я]+'))
    rull_mas.append(re.compile(r'\b[а-я][а-я]\s'))
    rull_mas.append(re.compile(r'\b[а-я][а-я]\b'))
    rull_mas.append(re.compile(r'\b[а-я]\s'))
    rull_mas.append(re.compile(r'\b[а-я]\b'))
    rull_mas.append(re.compile(r'[ ]+'))
    return rull_mas


# Процедура токенезации
def tocenizator(predlog_first, slovoStop, rullmas):
    """
    Токенезация предложений
    оставляются только текст на русском
    удаляются стоп слова, предлоги, и т.п.
    :param predlog_first:
    :param slovoStop: слоарь стоп слов
    :param rullmas - набор откомпелированных правил
    :return: list токенизированных слов в порядке их следования
    в предложении
    """
    slugstr = predlog_first.lower().strip()
    for rul in rullmas: slugstr = rul.sub(' ', slugstr)
    sluglist = slugstr.split()
    token = [x.strip() for x in sluglist if x not in slovoStop]

    return token  # возвращается список


# процедура лемматизации предложения
# на вход дается токенезированное предложение
# на выходе лемматизированное предложение

def lemmatizatorPred(ts,lemmatizator):
    lempred = ""
    for slovo in ts:
        krit = lemmatizator.get(slovo)
        if krit:
            lempred = lempred + krit.strip() + " "
    return lempred
