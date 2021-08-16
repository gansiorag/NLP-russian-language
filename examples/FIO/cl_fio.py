"""
This module make ricognition FIO

Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""
from fio import FIO

def proga():
    fio = FIO()
    print(fio.predict('Корнеев'))
    print(fio.predict('Вдохновение'))
    print(fio.predict('Вдохновляющий'))
    print(fio.predict('Спенсер'))

if __name__ == '__main__':
    proga()
