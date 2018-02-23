#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Танюшка
#
# Created:     29.05.2016
# Copyright:   (c) Танюшка 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from .Exceptions import *

stressed = chr(0x301)#ударение

def ClearStr(s):
    return s.replace(stressed, '')

# Двусоставные слова, числом указан номер слога с "невидимым" ударением
compoundWordStems = {
"человеколюб" : 2,
"многомилостив" : 1
}
#дерево слогов
class SyllableTree:
    def __init__(self,text):
        self.syllables = []

        self.first = None
        self.last = None

        self.words = []

        self.firstWord = None
        self.lastWord = None

        self.Build(text)

    def __len__(self):
        return len(self.syllables)

    def Build(self, text):
        self.BuildWords(text)
        self.BuildSyllables()

    def BuildWords(self, text):
        # Разбиваем текст на слова
        s = self.SplitToWordsWithPunctuation(text)

        # Если строка начинается с пунктуации, отбрасываем, т.к. так не бывает (пусть)
        if len(s) and not s[0][0]:
            del s[0]

        # Каждому слову сопостовляем экземпляр класса words
        self.words = [Word(x[0], punctuation = x[1]) for x in s]

        # Перевязываем слова между собой (next-prev)
        self.LinkItems(self.words)

        if self.words:
            self.firstWord = self.words[0]
            self.lastWord = self.words[-1]

    splitSymbols = ' ;:.,?!'

    """
    Разбить на слова вместе с пунктуацией
    Возвращает список пар (слово, знаки пунктуации после него)
    """
    def SplitToWordsWithPunctuation(self,text):
        split = self.splitSymbols

        s = []

        wS = 0
        i = 0

        while i < len(text):
            if text[i] in split:
                w = text[wS:i]

                pS = i
                while i < len(text) and text[i] in split:
                    i+=1

                p = text[pS:i]
                wS = i

                s.append((w, p))

            elif i == len(text) - 1:
                s.append((text[wS:], None))

            i+=1


        return s

    def LinkItems(self, arr):
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
            arr[i+1].prev = arr[i]

            arr[i].num = i
            arr[i+1].num = i+1


    def BuildSyllables(self):
        for w in self.words:
            syl = [Syllable(x, w) for x in self.SplitToSyllables(w.word)]

            if syl:
                w.firstSyllable = syl[0]
                w.lastSyllable = syl[-1]

                for s in syl:
                    if stressed in s.str:
                        w.stressedSyllable = s
                        break

                self.syllables += syl

        self.LinkItems(self.syllables)

        if (self.syllables):
            self.first = self.syllables[0]
            self.last = self.syllables[-1]

    poemSymbols = 'аеиоуыэюя' + 'аеиоуыэюя'.upper()  # строка глассных

    #разбить на слоги
    def SplitToSyllables(self, text):
        poem = self.poemSymbols
        prev = 0
        m = []
        for i in range(len(text)):
            if text[i] in poem:
                #< len(text)-1:
                k = i+1
                if i+1 < len(text) and text[i+1] == stressed:
                    k=k+1
                m.append(text[prev:k])
                prev = k
            elif i == len(text)-1 and m:
                m[-1] += text[prev:]


            #elif text[i] in poem and (i+1 == len(text)-1):
            #    m.append(text[prev:i+2])
            #    prev =i+1

        return m

    def __repr__(self):
        s = ""
        for w in self.words:
            s += str(w)

        return s



class Syllable:
    def __init__(self, str, parentWord, num = None, next= None, prev = None, isStressed = False):
        self.str = str
        self.cleanStr = ClearStr(self.str)
        self.next = next
        self.prev = prev
        #self.isAccent = None
        self.num = num
        self.isStressed = isStressed
        self.markup = None
        self.parentWord = parentWord

        # Определим ударение
        #y = None # значок ударения
        #if y in self.str:
        #    self.isStressed = True
        #else:
        #    self.isStressed = False

    def CheckMarkup(self):
        if self.markup:
            raise SyllableTreeException("Слог '%s' в слове '%s' уже размечен" % (self.str, self.parentWord))

    def _setMarkup(self, char):
        self.CheckMarkup()

        # Ищем вхождение гласной

        for i in range(len(self.cleanStr)):
            if self.cleanStr[i] in SyllableTree.poemSymbols:
                # Ставим знак
                self.markup = self.cleanStr[:i+1] + char + self.cleanStr[i+1:]
                return

        raise SyllableTreeException("В слоге '%s' не найдена гласная" % self.str)




    def setUp(self):
        self._setMarkup(chr(0x301))
        return self

    def setDown(self):
        self._setMarkup(chr(0x300))
        return self

    def setLowerAccent(self):
        self._setMarkup(chr(0x30C))
        #self._setMarkup(chr(0x2c7))
        return self

    def setUpperAccent(self):
        self._setMarkup(chr(0x302))
        #self._setMarkup(chr(0x2c6))
        return self

    def setWaveAccent(self):
        self._setMarkup(chr(0x303))
        return self

    def setPauseAccent(self):
        self._setMarkup(chr(0x305))
        #self._setMarkup(chr(0x2C9))
        return self

    def __str__(self):
        return self.markup or self.cleanStr

    def __repr__(self):
        return "Syllable('%s', %s, prev=%s, next=%s)" % (str(self), self.num, self.prev, self.next)

class Word:
    def __init__(self, w, num = None, punctuation = None, next = None, prev = None):
        self.word = w
        self.num = num

        self.next = None
        self.prev = None

        self.firstSyllable = None
        self.lastSyllable = None
        self.stressedSyllable = None

        # Знаки пунктуации после слова
        self.punctuation = punctuation

    def GetSyllables(self):
        x = self.firstSyllable

        while x and x.prev != self.lastSyllable:
            yield x
            x = x.next

    def __str__(self):
        if not self.firstSyllable:
            return self.word + (self.punctuation or '')
        else:
            return "".join(str(x) for x in self.GetSyllables()) + (self.punctuation or '')


    def __repr__(self):
        return "Word('%s', %s, next=%s, prev=%s)" % (str(self), self.stressedSyllable, self.next, self.prev)

    def canBeAccent(self):
        # У предлогов и союзов не должно стоять ударение
        return self.stressedSyllable != None



    # является ли слово двусоставным
    #def isCompound(self):
        #ClearStr(self.word).lower() in compoundWordStems.keys()


    def __eq__(self, other):
        if isinstance(other, str):
            return ClearStr(self.word) == other

        return NotImplemented


def main():
    s = ' ,,С высоты{0} снизше{0}л?? еси{0}, Благоутро{0}бне!!'.format(stressed)

    a = SyllableTree(s)

    print(a)

if __name__ == '__main__':
    main()