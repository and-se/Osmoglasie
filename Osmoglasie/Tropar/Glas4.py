# Author Тихон Сысоев

from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas4_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas4_Schema()
    """
    Размечает строку на указанное колено
    """
    def MarkupLine (self, line, schema_line):
        # разложим на слова-слоги
        tree = SyllableTree(line)

        if schema_line   == "1":
            return self.Markup_1(tree)
        elif schema_line == "2":
            return self.Markup_2(tree)
        elif schema_line == "К":
            return self.Markup_K(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)

    def Markup_1(self, tree):
        # Схема колена: ... — / ... \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent().next.setDown()
        else:
            accents.lastAccent.setPauseAccent().next.setUp()
            tree.last.setDown()

        return tree

    def Markup_2(self, tree):
        # Схема колена: ... ^ ... \ ^ ... \
        # т.е. есть первый и последний акценты

        #Нам нужен первый и последний акценты
        accents = AccentsSearcher(tree, "first last")

        # Слоги между первым и последним акцентами
        betweenStressed = []
        syl = accents.firstAccent

        while syl != accents.lastAccent:
            betweenStressed.append(syl)
            syl = syl.next

        # Количество таких слогов
        if len(betweenStressed) < 1:
            accents.firstAccent.setUpperAccent()
            accents.lastAccent.setUpperAccent()
        else:
            accents.firstAccent.setUpperAccent()
            accents.lastAccent.setUpperAccent().prev.setDown()
        tree.last.setDown()

        return tree

    def Markup_K(self, tree):
        # Схема колена: ... — \ ... /

        # Нам нужен только последний акцент
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

class Glas4_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def CheckStringCount(self, n):
        t1 = (n - 1) / 2
        # n%2 == 1
        if t1 != int(t1):
            raise SchemaException("Неправильное количество колен для 4 гласа")

    def Next(self, ostatok):
        if not self.current:
            self.CheckStringCount(ostatok)
            self.current = "1"
            return

        if self.current == "1":
            self.current = "2"

        elif self.current == "2":
            self.current = "1"

        else:
            raise SchemaException("С колена %s возможен переход только на конечное" % self.current)

    def Last(self):
        if self.current == "2":
            self.current = "К"
            return

        raise SchemaException("С колена %s переход в конечное колено невозможен" % self.current)
