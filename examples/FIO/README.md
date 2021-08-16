# Распознавание фамилии имени и отчества
Скопируюте файлы model_FIO.zip, model_tfidf_FIO.zip, model_transform_FIO.zip<br>
Из файла fio.py импортируйте класс FIO <br>
Класс к которому относится слово получаете следующим образом:<br>
from fio import FIO <br>
fio=FIO()<br>
class_word = fio.predict('Иванов')<br>
print(class_word) =====>>>> фамилия<br>
