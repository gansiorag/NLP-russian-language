import zipfile
import os

# Загрузка лемматизатора
def load_lemmatizator(namefile):
    lemmatVoc = {}
    namefiledubl = os.path.basename(namefile).split(".")[0]+".lem"
    with zipfile.ZipFile(namefile) as myzip:
        with myzip.open(namefiledubl) as myfile:
            for line in myfile:
                linetxt = line.decode('utf-8')
                slovo = linetxt.split('@')
                lemmatVoc[slovo[0].strip()] = slovo[1].strip()
    return lemmatVoc


if __name__ == "__main__":
    vocc = load_lemmatizator('/home/al/Projects_My/recognition_text/work_with_text/lemmatizator27022019.zip')
    vocc_set = set()
    for kk in vocc:
        vocc_set.add(kk.lower().strip())
    print(len(vocc_set))
    f_r = open('/home/al/Projects_My/NLP-russian-language/NLP_gansior/FIO/datasets/rezult_names/base_vocab.txt', 'w')
    for kk in list(vocc_set):
        f_r.write(kk + '\n')
    f_r.close()