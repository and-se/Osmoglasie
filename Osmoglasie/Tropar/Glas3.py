from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *


class Glas3_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas3_Schema()

    """
    Размечает строку на указанное колено
    """

    def MarkupLine(self, line, schema_line):

        # разложим на слова-слоги
        tree = SyllableTree(line)

        if schema_line == "1":
            return self.Markup_1(tree)
        elif schema_line == "2":
            return self.Markup_2(tree)
        elif schema_line == "3":
            return self.Markup_3(tree)
        elif schema_line == "К":
            return self.Markup_K(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)


    def Markup_1(self, tree):
        # Схема колена: ... \ / ~ ...

        # Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        if accents.lastAccent.prev.prev == None:
            raise MarkupException("Слишком маленькие колена для реализации 3 гласа")
        accents.lastAccent.prev.prev.setDown().next.setUp().next.setWaveAccent()

        return tree


    def Markup_2(self, tree):
        # Схема колена: ... \ / ^ ... \
        # Нам нужен только последний акцент

        accents = AccentsSearcher(tree, "last")
        if accents.lastAccent.prev.prev == None:
            raise MarkupException("Слишком маленькие колена для реализации 3 гласа")

        accents.lastAccent.prev.prev.setDown().next.setUp().next.setUpperAccent()
        # размечаем последний слог
        tree.last.setDown()

        return tree


    def Markup_3(self, tree):
        # Схема колена: ... v ... / \ \
        # Нам нужен только последний акцент

        accents = AccentsSearcher(tree, "last")

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed
        # Количество заударных слогов
        if len(zaudarn) < 2:
            accents.lastAccent.setWaveAccent().next.setDown()
        elif len(zaudarn) < 3:
            accents.lastAccent.setWaveAccent().next.setDown().next.setDown()
        else:
            accents.lastAccent.setLowerAccent()
            tree.last.prev.prev.setUp().next.setDown().next.setDown()

        return tree


    def Markup_K(self, tree):
        # Схема колена: ... - ... \ \ ^ / / \ \ / ... \
        # т.е. есть последний и предпоследний акценты

        accents = AccentsSearcher(tree, "prelast last")

        # Ставим предпоследний акцент
        preLastA = accents.preLastAccent
        lastA = accents.lastAccent

        if preLastA.next == lastA:
            preLastA.setWaveAccent()
        elif preLastA.next.next == lastA:
            preLastA.setWaveAccent().next.setDown()
        else:
            preLastA.setPauseAccent()
            lastA.prev.prev.setDown().next.setDown()


        # Ставим последний акцент
        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed

        if len(zaudarn) < 2:
            lastA.setWaveAccent().next.setDown()
        elif len(zaudarn) < 3:
            lastA.setWaveAccent().next.setUp().next.setDown()
        elif len(zaudarn) < 4:
            lastA.setWaveAccent().next.setDown().next.setUp().next.setDown()
        elif len(zaudarn) < 5:
            lastA.setWaveAccent().next.setDown().next.setDown().next.setUp().next.setDown()
        elif len(zaudarn) < 6:
            lastA.setWaveAccent().next.setUp().next.setDown().next.setDown().next.setUp().next.setDown()
        else:
            lastA.setUpperrAccent().next.setUp().next.setUp().next.setDown().next.setDown().next.setUp()
            # размечаем последний слог
            tree.last.setDown()
        return tree


class Glas3_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None
        self.firstRound = True

    def Next(self, ostatok):
        if not self.current:
            self.current = "1"
            return

        if self.current == "1":
            if ostatok == 1:
                raise SchemaException("Возможен переход только на конечное колено")
            elif self.firstRound:
                self.current = "3"
                self.firstRound = False
            else:
                self.current = "2"

        elif self.current == "2":
            self.current = "3"

        elif self.current == "3":
            self.current = "1"

        else:
            raise SchemaException("С колена %s возможен переход только на конечное" % self.current)


    def Last(self):
        self.current = "К"
