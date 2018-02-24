from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas7_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas7_Schema()

    def MarkupLine (self, line, schema_line):
        # разложим на слова-слоги
        tree = SyllableTree(line)

        if schema_line == "1":
          return self.Markup_1(tree)
        elif schema_line == "2":
           return self.Markup_2(tree)

        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)

    def Markup_1(self, tree):
        # Схема колена: ... \ v \ ... ///

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        beforeAccent = []
        syl = tree.first
        while syl != accents.lastAccent:
            beforeAccent.append(syl)
            syl = syl.next

        zaudarn = accents.afterStressed

        if len(beforeAccent)<1:
            raise MarkupException("Слишком мало слогов перед последним акцентом: %s" % line)


        if len(zaudarn) == 1:
           accents.lastAccent.setWaveAccent().next.setUp().prev.prev.setDown()
        elif len(zaudarn) == 2:
            accents.lastAccent.setWaveAccent().prev.setDown().next.next.setUp().next.setUp()
        elif len(zaudarn) == 3:
            accents.lastAccent.setWaveAccent().prev.setDown().next.next.setUp().next.setUp().next.setUp()
        else:
            tree.last.setUp().prev.setUp().prev.setUp()
            accents.lastAccent.setLowerAccent().prev.setDown().next.next.setDown()

        return tree

    def Markup_2(self, tree):
        # Схема колена: ... \ / ^  ... \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        beforeAccent = []
        syl = tree.first
        while syl != accents.lastAccent:
            beforeAccent.append(syl)
            syl = syl.next

        if len(beforeAccent)<1:
            raise MarkupException("Слишком мало слогов перед последним акцентом: %s" % line)

        accents.lastAccent.setUpperAccent().prev.setUp().prev.setDown()
        tree.last.setDown()

        return tree

class Glas7_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def CheckStringCount(self, n):


        if n%2==0 :
            raise SchemaException("Неправильное количество колен для 7 гласа")


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


    def Last (self):
        if self.current == "2":
            self.current = "1"
            return

        raise SchemaException("С колена %s переход в конечное колено невозможен" % self.current)