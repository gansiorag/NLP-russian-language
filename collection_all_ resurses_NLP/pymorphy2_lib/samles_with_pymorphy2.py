import pymorphy2
from pprint import pprint

morph = pymorphy2.MorphAnalyzer()
word = morph.parse('Григорьевичом')[0]
print(word)
print(word.tag)
print(word.normal_form)
pprint(word.lexeme)
for k in word.lexeme:
    print(k.word)

print(list('Григорьевичом'))
