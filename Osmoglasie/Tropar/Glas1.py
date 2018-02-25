from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas1_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas1_Schema()

    def MarkupLine(self, line, schema_line):
        # разложим на слова-слоги
        tree = SyllableTree(line)

        if(schema_line == "1"):
            return self.Markup_1(tree)
        elif(schema_line == "1a"):
            return self.Markup_1a(tree)
        elif(schema_line == "2"):
            return self.Markup_2(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)


    def Markup_1(self, tree):
        #схема колена: ...~\...//^...
        # between 2 ~\/^     1 ~ . ^
        accents = AccentsSearcher(tree, "first last UseLastSyl");

        syllBetweenAccents = accents.lastAccent.num - accents.firstAccent.num - 1
        
        # Проверяем количество слогов между акцентами
        if syllBetweenAccents > 2:
            accents.firstAccent.setWaveAccent().next.setDown()
            accents.lastAccent.setUpperAccent().prev.setUp().prev.setUp()
        elif syllBetweenAccents == 2:
            accents.firstAccent.setWaveAccent().next.setDown()
            accents.lastAccent.setUpperAccent().prev.setUp()
        # если между первым и последним акцентами один или ни одного слога и при этом они не сливаются
        elif syllBetweenAccents in (0, 1) and accents.firstAccent != accents.lastAccent:
            accents.firstAccent.setWaveAccent()
            accents.lastAccent.setUpperAccent()
        else:
            line = ""
            for w in tree.words:
                line += w.word + " "
            raise SchemaException("Колено ''%s'' слишком короткое" % line)

        return tree


    def Markup_1a(self, tree):
        #схема колена: ...\/^...
        # check \ /
        accents = AccentsSearcher(tree, "last UseLastSyl")
        if (accents.lastAccent.num - tree.first.num) > 1:
            accents.lastAccent.setUpperAccent().prev.setUp().prev.setDown()
        else:
            line = ""
            for w in tree.words:
                line += w.word + " "
            raise SchemaException("Колено ''%s'' слишком короткое" % line)

        return tree


    def Markup_2(self, tree):
        # Сема колена: ...V...\

        accents = AccentsSearcher(tree, "last")
        accents.lastAccent.setLowerAccent()
        tree.last.setDown()

        return tree


class Glas1_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None


    def Next(self, ostatok):
        if self.current == None:
            self.current = "1"
            return

        if self.current == "1":
            if ostatok == 2:
                self.current = "1a"
            else:
                self.current = "2"
        elif self.current == "2":
            self.current = "1"

        else:
            raise SchemaException("С колена %s возможен переход только на конечное" % self.current)


    def Last(self):
        if self.current == "1" or self.current == "1a":
            self.current = "2"
        else:
            raise SchemaException("С колена %s переход на конечное колено невозможен" % self.current)