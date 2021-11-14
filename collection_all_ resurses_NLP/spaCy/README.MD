# ----- spaCy -----
Билиотека spaCy - очень мощная библиотека, но почему-то, мало упоминается на 
русскоязычных ресурсах.<br>
Ссылка на сайт библиотеки - **https://spacy.io/** <br>
Для работы с русским языком ее надо настроить.<br>
Установка - **pip install -U spacy** <br>
Для работы с русским языком необходимо загрузить соответствующую модель:<br>
**python3 -m spacy download ru_core_news_sm**<br>
Можно работать с разными языками. Как это делать написано на странице -  
примеры по использованию основных инструментов этой библиотеки.<br>
Не смотря на мощь библиотеки, в ней **нет** реализации методов **Stemming**.
* https://spacy.io/usage/rule-based-matching
* https://colab.research.google.com/drive/1p75B2YAWSx7dCKVpS83tfghDXOgqXb_h?usp=sharing
* https://explosion.ai/demos/matcher
* https://habr.com/ru/post/504680/
* https://nlpub.ru/SpaCy#.D0.9D.D0.B0.D1.81.D1.82.D1.80.D0.BE.D0.B9.D0.BA.D0.B0_pipeline
* https://progi.pro/kak-dobavit-polzovatelskie-znaki-v-funkciyu-punktuacii-spacy-11695417
* https://webdevblog.ru/spacy-101-vse-chto-vam-nuzhno-znat-chast-1/