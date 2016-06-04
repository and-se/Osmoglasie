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
stressed = chr(0x301)

class SyllableTree:
    def __init__(self,text):
        self.first = None
        self.last = None
        self.count = None

        self.firstAccent = None
        self.lastAccent = None
        self.preLastAccent = None

        #self.BuildWord(text)
        self.Build(text)

    #построить дерево уровня "слова"
    def BuildWord(self,text):
        split = ' ;:.,?!'  # строка символов
        prev = 0
        s = []
        for i in range(len(text)):
            if text[i] in split:
                e = text[prev:i]
                if e != "":
                    s.append(e)
                prev =i+1
            elif (i == len(text)-1):
                s.append(text[prev:i+1])
                prev =i+1
        print(s)
        return s

    #построить дерево уровня "слоги"
    def Build(self, text):
        m = self.SplitToSyllables(text)

        print(m)

        self.syllables = []

        for i in range(len(m)):
            self.syllables.append(Syllable(m[i], i, isStressed = m[i][-1] == stressed))

        for i in range(len(self.syllables) - 1):
            self.LinkSyllables(self.syllables[i], self.syllables[i+1])

        self.first = self.syllables[0]
        self.last = self.syllables[-1]

        self.count = len(self.syllables)

        #self.FindAccents()

    def FindAccents (self):
        w = self.lastWord

        if w.stressedSyllable == self.last:
            w = w.prev

        while not w.stressedSyllable:
            w = w.prev







    #разбить на слоги
    def SplitToSyllables(self, text):
        poem = 'аеиоуыэюя'  # строка глассных
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
            #elif text[i] in poem and (i+1 == len(text)-1):
            #    m.append(text[prev:i+2])
            #    prev =i+1
        return m

    def LinkSyllables(self, a, b):
        a.next = b
        b.prev = a

    def __repr__(self):
        s = ""
        for i in self.syllables:
            s+= i.markup if i.markup else i.str

        return s



class Syllable:
    def __init__(self, str, num, next= None, prev = None, isStressed = False):
        self.str = str
        self.next = next
        self.prev = prev
        #self.isAccent = None
        self.num = num
        self.isStressed = isStressed
        self.markup = None

        # Определим ударение
        #y = None # значок ударения
        #if y in self.str:
        #    self.isStressed = True
        #else:
        #    self.isStressed = False

    def CheckMarkup(self):
        if self.markup:
            raise SyllableTreeException("Слог '%s' уже размечен" % self.str)

    def setUp(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x301)
        return self

    def setDown(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x300)
        return self

    def setLowerAccent(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x30C)
        return self

    def setUpperAccent(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x302)
        return self

    def waveAccent(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x305)
        return self

    def pauseAccent(self):
        self.CheckMarkup()
        self.markup = self.str+chr(0x303)
        return self

def main():
    a= SyllableTree('С высоты{0} снизше{0}л еси{0} Благоутро{0}бне'.format(stressed))

if __name__ == '__main__':
    main()

class SyllableTreeException(Exception):
    def __init__(self, msg):
        self.message = msg
