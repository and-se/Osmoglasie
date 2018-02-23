from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas6_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas6_Schema()
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
        elif schema_line == "2а":
            return self.Markup_2a(tree)
        elif schema_line == "К":
            return self.Markup_K(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)

    def Markup_1(self, tree):
        # Схема колена: ... v ... /

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        accents.lastAccent.setLowerAccent()
        tree.last.setUp()

        return tree

    def Markup_2(self, tree):
        # Схема колена: ... — \ ... /

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent().next.setUp()
        else:
            accents.lastAccent.setPauseAccent().next.setDown()
            tree.last.setUp()

        return tree

    def Markup_2a(self, tree):
        # Схема колена: ... — \ ... \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent().next.setDown()
        else:
            accents.lastAccent.setPauseAccent().next.setDown()
            tree.last.setDown()

        return tree

    def Markup_3(self, tree):
        # Схема колена: ... v ... \ \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent().next.setDown()
        else:
            accents.lastAccent.setLowerAccent()
            tree.last.setDown().prev.setDown()

        return tree

    def Markup_K(self, tree):
        # Схема колена: ... / ^ ... \ v \ ... /
        # т.е. есть последний и предпоследний акценты

        accents = AccentsSearcher(tree, "prelast last")

        # Ставим предпоследний акцент и округу
        preLastA = accents.preLastAccent
        lastA = accents.lastAccent

        preLastA.prev.setUp()

        if preLastA.next == lastA:
            preLastA.setWaveAccent()
        else:
            preLastA.setUpperAccent()

        # Ставим последний акцент

        if lastA.prev != preLastA:
            lastA.prev.setDown()

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed

        if len(zaudarn) < 2:
            lastA.setWaveAccent().next.setUp()
        else:
            lastA.setLowerAccent().next.setDown()
            tree.last.setUp()

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

class Glas6_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def CheckStringCount(self, n):
        t1 = (n-1)/3 #без 2а   n = 3p + 1
        t2 = (n-3)/3 #с 2а     n = 3p + 3

        if t1 != int(t1) and t2 != int(t2) and n != 3:
            raise SchemaException("Неправильное количество колен для 6 гласа")


    def Next(self, ostatok):
        if not self.current:
            self.CheckStringCount(ostatok)
            self.current = "1"
            return

        if self.current == "1":
            if ostatok == 2:
                self.current = "2а"
            else:
                self.current = "2"

        elif self.current == "2":
            self.current = "3"

        elif self.current == "3":
            self.current = "1"

        else:
            raise SchemaException("С колена %s возможен переход только на конечное" % self.current)


    def Last (self):
        if self.current == "3" or self.current == "2а":
            self.current = "К"
            return

        raise SchemaException("С колена %s переход в конечное колено невозможен" % self.current)
