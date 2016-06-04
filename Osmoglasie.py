#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Танюшка
#
# Created:     15.05.2016
# Copyright:   (c) Танюшка 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from SyllableTree import *

"""
Разметить текст на глас указанного жанра песнопений (тропарный и т.д.)
"""
def Markup(text, glas, type):
    # Разбиваем на логические строки (по / и //)
    ls = GetLogicalStrings(text)

    # Получаем шаблон разметки на нужный глас
    markupper = GetGlasTemplate(glas, type)

    # Размечаем текст
    m_text = markupper.Markup(ls)

    # Возвращаем результат в виде текста с разметкой
    return str(m_text)

"""
Разбить текст на логические строки
"""
def GetLogicalStrings(text):
    k = text.split('//')
    if len(k) != 2:
        raise LogicalStringsException('Некорректное конечное колено')

    if '/' in k[1]:
        raise LogicalStringsException('Обозначено конечным не последнее колено')

    lines = k[0].split("/")

    return list(map(str.strip, lines + [k[1]]))

def GetGlasTemplate(glas, type):
    if glas == 8 and type == "тропарь":
        return Glas8_Template()

    raise NotImplementedError()

class Glas8_Template:
    def CreateSchema(self):
        return Glas8_Schema()

    """
    Размечает логические строки на глас
    """
    def Markup(self, strings):
        result = []
        schema = self.CreateSchema()
        # количество неразмеченных строк
        ost = len(strings)
        # размечаем все строки, кроме последней
        for s in strings[:-1]:
            # переход на следующее колено
            schema.Next(ost)
            ost = ost-1
            result.append(self.MarkupLine(s, schema.current))

        schema.Last()
        result.append(self.MarkupLine(strings[-1], schema.current))

        return result

    """
    Размечает строку на указанное колено
    """
    def MarkupLine (self, line, schema_line):
        if schema_line  != "1":
            raise MarkupException('Некорректный номер колена')
        #конструктор создаем элемент класса дерево
        tree = SyllableTree(line)
        #размечаем всё начало строки
        pointer= tree.first.next.setDown().next.setUp().next.setUp().next.next.setDown()
        #размечаем последний акцент

        # Если осталось мало слогов?
        ostatok = len(tree) - pointer.num -1
        if not ostatok:
            raise MarkupException("Слишком короткая строка: %s" % line)
        elif ostatok <= 2:
            pointer = pointer.next.setDown()
            if pointer != tree.last:
                pointer.next.setDown()
        else:
          ##tree.lastAccent.setLowerAccent()
          #размечаем последний слог
          tree.last.setDown()

  #Не разрешать переопределять значки в уже размеченных слогах

        return tree

class Glas8_Schema:
    def __init__(self):
        self.current = None

    def Next(self, ostatok):
        self.current = "1"

    def Last (self):
        self.current = "1"


class OsmoglasieException(Exception):
    def __init__(self, msg):
        self.message = msg

class LogicalStringsException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg

class MarkupException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg





if __name__ == "__main__":
    text = """С высоты{0} снизше{0}л еси{0} Благоутро{0}бне,/
погребе{0}ние прия{0}л еси{0} тридне{0}вное,/
да на{0}с свободи{0}ши страсте{0}й,//
Животе{0} и воскресе{0}ние на{0}ше. Гоc{0}поди, сла{0}ва Тебе{0}.
""".format(chr(0x301) if False else '')

    print(Markup(text, 8, "тропарь"))
