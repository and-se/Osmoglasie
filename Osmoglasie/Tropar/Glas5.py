# Author Диана Фоменко

from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas5_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas5_Schema()
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
        elif schema_line == "К":
            return self.Markup_K(tree)
        else:
            raise MarkupException('Некорректный номер колена %s' % schema_line)

    def Markup_1(self, tree):
        # Схема колена: ... - ... \ / ^ \ ...

        # Нам нужен первый и последний акценты
        # Сначала находим первый акцент,
        # который выражен остоновкой
        accents = AccentsSearcher(tree, "first")
        accents.firstAccent.setPauseAccent()

        # Потом находим последний акцент,
        # который предворяется последовательным спуском
        # и подъемом, после - следует спуск
        firstA = accents.firstAccent
        accents = AccentsSearcher(tree, "last")
        lastA = accents.lastAccent
        if (lastA.num - firstA.num < 3):
            return MarkupException("ОШИБКА! В колене недостаточно слогов")
        else:
            lastA.setUpperAccent().prev.setUp().prev.setDown()
            lastA.next.setDown()

        return tree

    def Markup_2(self, tree):
        # Схема колена: ... \ ^  ... \

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        accents.lastAccent.setUpperAccent().prev.setDown()
        tree.last.setDown()

        return tree

    def Markup_3(self, tree):
        # Схема колена: ... - ... v ...

        # Нам нужен первый и последний акценты
        # Сначала находим первый акцент,
        # который выражен остоновкой
        accents = AccentsSearcher(tree, "first last")
        accents.firstAccent.setPauseAccent()

        # Потом находим последний акцент,
        # он нисходящий
        firstA = accents.firstAccent

        lastA = accents.lastAccent
        lastA.setLowerAccent()

        return tree

    def Markup_K(self, tree):
        # Схему колена рассмотрим для каждого случая
        # в ней есть последний и предпоследний акценты

        accents = AccentsSearcher(tree, "prelast last")

        # Ставим предпоследний акцент и округу
        preLastA = accents.preLastAccent
        lastA = accents.lastAccent

        # Заударные слоги (т.е. слоги после последнего акцента)
        zaudarn = accents.afterStressed

        #Рассмотрим 3 случая для разного количетсва заударных
        # 1 случай: при одном заударном слоге
        if len(zaudarn) == 1:
            # между акцентами <= 1
            # разметка: ... ~ . ~ \
            if ((preLastA.next == lastA) or (preLastA.next.next == lastA)):
                preLastA.setWaveAccent()
                lastA.setWaveAccent().next.setDown()

            # между акцентами > 1 слог
            # разметка: ... v \ ... ~ \
            else:
                preLastA.setLowerAccent().next.setDown()
                lastA.setWaveAccent().next.setDown()

        # 2 случай: при двух заударных слогах
        elif len(zaudarn) == 2:
            # между акцентами <= 1
            # разметка: ... ~ . ~ / \
            if ((preLastA.next == lastA) or (preLastA.next.next == lastA)):
                preLastA.setWaveAccent()
                lastA.setWaveAccent().next.setUp().next.setDown()

            # между акцентами > 1 слог
            # разметка: ... v \ ... ~ / \
            else:
                preLastA.setLowerAccent().next.setDown()
                lastA.setWaveAccent().next.setUp().next.setDown()

        # 3 случай: при трех и более заударных слогах
        else:
            # между акцентами <= 1
            # разметка: ... ~ . v / ... / \
            if ((preLastA.next == lastA) or (preLastA.next.next == lastA)):
                preLastA.setWaveAccent()
                lastA.setLowerAccent().next.setUp()
                tree.last.setDown().prev.setUp()

            # между акцентами > 1 слог
            # разметка: ... v \ ... v / ... / \
            else:
                preLastA.setLowerAccent().next.setDown()
                lastA.setLowerAccent().next.setUp()
                tree.last.setDown().prev.setUp()

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

class Glas5_Schema(GlasSchemaBase):
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
            self.current = "1"

    def Last (self):
        self.current = "К"
