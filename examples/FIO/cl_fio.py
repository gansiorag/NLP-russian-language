"""
This module make

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
import pickle
import zipfile
from nltk.util import ngrams


def from_word_list_to_sentenses(ish_str: str):
    servis_list = []
    servis_list.append(ish_str.lower())
    dd = list(ish_str.lower())
    ngg = list(ngrams(dd, 4))
    for nn in ngg:
        word = ''.join(nn)
        servis_list.append(word)
    return [' '.join(servis_list)]


class FIO():
    def __init__(self):
        # source file names
        namefile_FIO = '/home/al/PycharmProjects/NLP-russian-language/examples/FIO/model_FIO.zip'
        namefile_vect = '/home/al/PycharmProjects/NLP-russian-language/examples/FIO/model_transform_FIO.zip'
        namefile_tfitf = '/home/al/PycharmProjects/NLP-russian-language/examples/FIO/model_tfidf_FIO.zip'

        zfn = 'model_FIO.pkl'
        with open(zfn, 'rb') as myfile:
            self.clf = pickle.load(myfile)

        with open('model_transform_FIO.pkl', 'rb') as myfile:
            self.vectorizer = pickle.load(myfile)

        with open('model_tfidf_FIO.pkl', 'rb') as myfile:
            self.tfidf_transformer  = pickle.load(myfile)

    def predict(self, fio:str) -> list:
        fio_sentence = from_word_list_to_sentenses(fio)
        X_train_new = self.vectorizer.transform(fio_sentence)
        X_new_tfidf = self.tfidf_transformer.transform(X_train_new)
        predicted = self.clf.predict(X_new_tfidf)
        return predicted


def proga():
    fio = FIO()
    print(fio.predict('Корнеев'.lower()))

if __name__ == '__main__':
    proga()
