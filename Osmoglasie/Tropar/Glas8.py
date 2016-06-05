from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas8_Template(GlasTemplateBase):
    def CreateSchema(self):
        return Glas8_Schema()

    """
    Размечает строку на указанное колено
    """
    def MarkupLine (self, line, schema_line):
        if schema_line  != "1":
            raise MarkupException('Некорректный номер колена %s' % schema_line)
        #конструктор создаем элемент класса дерево
        tree = SyllableTree(line)

        #Нам нужен только последний акцент
        accents = AccentsSearcher(tree, "last")

        if len(tree) < 7:
            raise MarkupException("Слишком короткая строка: %s" % line)

        # Схема колена: . \ / / . \ ... v ... \
        # . - один слог; \ и / - спуск подъём; v - нисходящий акцент

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

class Glas8_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def Next(self, ostatok):
        self.current = "1"

    def Last (self):
        self.current = "1"
