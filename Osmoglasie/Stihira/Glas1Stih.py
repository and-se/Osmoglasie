# Author Анастасия Елетина

from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas1Stih_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas1Stih_Schema()
    """
    Размечает строку на указанное колено
    """
    def MarkupLine (self, line, schema_line):
        # разложим на слова-слоги
        tree = SyllableTree(line)

        if schema_line  == "1":
            return self.Markup_1(tree)
        elif schema_line == "2":
            return self.Markup_2(tree)
        elif schema_line == "3":
            return self.Markup_3(tree)
        elif schema_line == "4":
            return self.Markup_4(tree)
        elif schema_line == "К":
            return self.Markup_K(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)

    def Markup_1(self, tree):
        # Схема колена: ... ~ \ ... \ ^ ...\\
        #Сначала нам нужен первый акцент
        #Первая часть " ... ~ \ ":
        accents = AccentsSearcher(tree, "first")
        accents.firstAccent.setWaveAccent().next.setDown()
        #Вторая часть "... \ ^ ...\\":
        # Ставим последний акцент
        firstA = accents.firstAccent
        accents = AccentsSearcher(tree, "last")
        lastA = accents.lastAccent
        if (firstA == lastA)  or (firstA.next == lastA):
            raise MarkupException("ОШИБКА! В колене недостаточно слогов: %s" % tree)
        else:

            # Заударные слоги (т.е. слоги после последнего акцента)
            zaudarn = accents.afterStressed

            if lastA.num - firstA.num > 2:
                lastA.prev.setDown()

            if len(zaudarn) < 2:
                lastA.setWaveAccent()
                tree.last.setDown()
            else:

                lastA.setUpperAccent()
                tree.last.prev.setDown()
                tree.last.setDown()
            return tree



    def Markup_2(self, tree):
        # Схема колена: ... \ ^ / ... \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        accents.lastAccent.prev.setDown()
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent()
            tree.last.setDown()
        else:
            accents.lastAccent.setUpperAccent().next.setUp()
            tree.last.setDown()

        return tree

    def Markup_3(self, tree):
        # Схема колена:  — ... v ... \

        #Нам нужен первый и последний акценты
        accents = AccentsSearcher(tree, "first")
        accents.firstAccent.setPauseAccent()
        accents = AccentsSearcher(tree, "last")
        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        accents.lastAccent.setLowerAccent()
        tree.last.setDown()

        return tree

    def Markup_4(self, tree):
        # Схема колена: ... v / ... ^ \ ... \

        #Нам нужен только последний и предпоследний акценты

        accents = AccentsSearcher(tree, "prelast last")

        # Ставим предпоследний акцент и округу
        preLastA = accents.preLastAccent
        lastA = accents.lastAccent

        if preLastA.next == lastA:
            preLastA.setWaveAccent()
        else:
            preLastA.setLowerAccent().next.setUp()

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed

        if len(zaudarn) < 2:
            lastA.setWaveAccent().next.setDown()
        else:
            lastA.setUpperAccent()
            lastA.next.setDown()
            tree.last.setDown()

        return tree

    def Markup_K(self, tree):
        # Схема колена:  ... v \ ... \
        # т.е. есть последний акцент

        accents = AccentsSearcher(tree, "last")

        lastA = accents.lastAccent

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed

        if len(zaudarn) < 2:
            lastA.setWaveAccent().next.setDown()
        else:
            lastA.setLowerAccent().next.setDown()
            tree.last.setDown()

        return tree

"""
        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        if len(tree) < 7:
            raise MarkupException("Слишком короткая строка: %s" % line)

        #размечаем всё начало строки
        pointer= tree.first.next.setDown().next.setUp().next.setUp().next.next.setDown()
        #размечаем последний акцент

        # Если осталось мало слогов?
        ostatok = len(tree) - pointer.num -1
        if not ostatok:
            raise MarkupException("Слишком короткая строка: %s" % line)
        elif ostatok <= 2:
            if pointer.next == accents.lastAccent:
                pointer = pointer.next.setLowerAccent()
            else:
                pointer = pointer.next.setDown()
            if pointer != tree.last:
                pointer.next.setDown()
        else:
          accents.lastAccent.setLowerAccent()
          #размечаем последний слог
          tree.last.setDown()

  #Не разрешать переопределять значки в уже размеченных слогах

        return tree
"""

class Glas1Stih_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def Next(self, ostatok):
        if not self.current:
            self.current = "1"
            return

        if self.current == "1":
            self.current = "2"

        elif self.current == "2":
            self.current = "3"

        elif self.current == "3":
            self.current = "4"

        elif self.current == "4":
            self.current = "1"


    def Last (self):
        self.current = "К"
        return