# -*- coding: utf-8 -*-
# Портирован с Java по мотивам http://www.algorithmist.ru/2010/12/Porter_one-stemmer-russian.html
import re

class Porter_one:
    PERFECTIVEGROUND = re.compile(u"((ив|ивши|ившись|ыв|ывши|ывшись)|((?<=[ая])(в|вши|вшись)))$")
    REFLEXIVE = re.compile(u"(с[яь])$")
    ADJECTIVE = re.compile(u"(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$")
    PARTICIPLE = re.compile(u"((ивш|ывш|ующ)|((?<=[ая])(ем|нн|вш|ющ|щ)))$")
    VERB = re.compile(
        u"((ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)|((?<=[ая])(ла|на|ете|йте|ли|й|л|ем|н|ло|но|ет|ют|ны|ть|ешь|нно)))$")
    NOUN = re.compile(
        u"(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$")
    RVRE = re.compile(u"^(.*?[аеиоуыэюя])(.*)$")
    DERIVATIONAL = re.compile(u".*[^аеиоуыэюя]+[аеиоуыэюя].*ость?$")
    DER = re.compile(u"ость?$")
    SUPERLATIVE = re.compile(u"(ейше|ейш)$")
    I = re.compile(u"и$")
    P = re.compile(u"ь$")
    NN = re.compile(u"нн$")
    info = 'algorithm takes from https://gist.github.com/Kein1945/9111512'

    def stem(word):
        word = word.lower()
        word = word.replace(u'ё', u'е')
        m = re.match(Porter_one.RVRE, word)
        if m and m.groups():
            pre = m.group(1)
            rv = m.group(2)
            temp = Porter_one.PERFECTIVEGROUND.sub('', rv, 1)
            if temp == rv:
                rv = Porter_one.REFLEXIVE.sub('', rv, 1)
                temp = Porter_one.ADJECTIVE.sub('', rv, 1)
                if temp != rv:
                    rv = temp
                    rv = Porter_one.PARTICIPLE.sub('', rv, 1)
                else:
                    temp = Porter_one.VERB.sub('', rv, 1)
                    if temp == rv:
                        rv = Porter_one.NOUN.sub('', rv, 1)
                    else:
                        rv = temp
            else:
                rv = temp

            rv = Porter_one.I.sub('', rv, 1)

            if re.match(Porter_one.DERIVATIONAL, rv):
                rv = Porter_one.DER.sub('', rv, 1)

            temp = Porter_one.P.sub('', rv, 1)
            if temp == rv:
                rv = Porter_one.SUPERLATIVE.sub('', rv, 1)
                rv = Porter_one.NN.sub(u'н', rv, 1)
            else:
                rv = temp
            word = pre + rv
        return word

    stem = staticmethod(stem)


"""
The Snowball stemmer.
Pavel Perestoronin © 2013
"""

class Porter_two:
    # Helper regex strings.
    _vowel = "[аеиоуыэюя]"
    _non_vowel = "[^аеиоуыэюя]"
    info = 'algorithm takes from https://gist.github.com/eigenein/5418094'
    # Word regions.
    _re_rv = re.compile(_vowel)
    _re_r1 = re.compile(_vowel + _non_vowel)

    # Endings.
    _re_perfective_gerund = re.compile(r"(((?P<ignore>[ая])(в|вши|вшись))|(ив|ивши|ившись|ыв|ывши|ывшись))$")
    _re_adjective = re.compile(
        r"(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|"
        r"ую|юю|ая|яя|ою|ею)$"
    )
    _re_participle = re.compile(r"(((?P<ignore>[ая])(ем|нн|вш|ющ|щ))|(ивш|ывш|ующ))$")
    _re_reflexive = re.compile(r"(ся|сь)$")
    _re_verb = re.compile(
        r"(((?P<ignore>[ая])(ла|на|ете|йте|ли|й|л|ем|н|ло|но|ет|ют|ны|ть|ешь|"
        r"нно))|(ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|"
        r"ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю))$"
    )
    _re_noun = re.compile(
        r"(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|"
        r"ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$"
    )
    _re_superlative = re.compile(r"(ейш|ейше)$")
    _re_derivational = re.compile(r"(ост|ость)$")
    _re_i = re.compile(r"и$")
    _re_nn = re.compile(r"((?<=н)н)$")
    _re_ = re.compile(r"ь$")

    def stem(self, word):
        """
        Gets the stem.
        """

        rv_pos, r2_pos = self._find_rv(word), self._find_r2(word)
        word = self._step_1(word, rv_pos)
        word = self._step_2(word, rv_pos)
        word = self._step_3(word, r2_pos)
        word = self._step_4(word, rv_pos)
        return word

    def _find_rv(self, word):
        """
        Searches for the RV region.
        """

        rv_match = self._re_rv.search(word)
        if not rv_match:
            return len(word)
        return rv_match.end()

    def _find_r2(self, word):
        """
        Searches for the R2 region.
        """

        r1_match = self._re_r1.search(word)
        if not r1_match:
            return len(word)
        r2_match = self._re_r1.search(word, r1_match.end())
        if not r2_match:
            return len(word)
        return r2_match.end()

    def _cut(self, word, ending, pos):
        """
        Tries to cut the specified ending after the specified position.
        """

        match = ending.search(word, pos)
        if match:
            try:
                ignore = match.group("ignore") or ""
            except IndexError:
                # No ignored characters in pattern.
                return True, word[:match.start()]
            else:
                # Do not cut ignored part.
                return True, word[:match.start() + len(ignore)]
        else:
            return False, word

    def _step_1(self, word, rv_pos):
        match, word = self._cut(word, self._re_perfective_gerund, rv_pos)
        if match:
            return word
        _, word = self._cut(word, self._re_reflexive, rv_pos)
        match, word = self._cut(word, self._re_adjective, rv_pos)
        if match:
            _, word = self._cut(word, self._re_participle, rv_pos)
            return word
        match, word = self._cut(word, self._re_verb, rv_pos)
        if match:
            return word
        _, word = self._cut(word, self._re_noun, rv_pos)
        return word

    def _step_2(self, word, rv_pos):
        _, word = self._cut(word, self._re_i, rv_pos)
        return word

    def _step_3(self, word, r2_pos):
        _, word = self._cut(word, self._re_derivational, r2_pos)
        return word

    def _step_4(self, word, rv_pos):
        _, word = self._cut(word, self._re_superlative, rv_pos)
        match, word = self._cut(word, self._re_nn, rv_pos)
        if not match:
            _, word = self._cut(word, self._re_, rv_pos)
        return word


if __name__ == '__main__':
    print(Porter_one.stem(u'устойчивость'))
    example_words = ['получила', 'историческое', 'образованием', 'написали', 'несколько', 'десятков', 'исторических',
                     'романов']
    for word in example_words:
        print(word + ' -> ' + Porter_one.stem(word))
    print('-'*30)
    ps = Porter_two()
    for word in example_words:
        print(word + ' -> ' + ps.stem(word))