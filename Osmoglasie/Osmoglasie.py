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
from .SyllableTree import *
from .AccentsSearcher import *
from . import Tropar

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
    r_list = [str(x) for x in m_text[:-1]]

    return "/ ".join(r_list) + "// " + str(m_text[-1])


"""
Разбить текст на логические строки
"""
def GetLogicalStrings(text):
    k = text.split('//')
    if len(k) != 2:
        raise LogicalStringsException('Не обозначено конечное колено или их больше одного')

    if '/' in k[1]:
        raise LogicalStringsException('Обозначено конечным не последнее колено')

    lines = k[0].split("/")

    return list(map(str.strip, lines + [k[1]]))

def GetGlasTemplate(glas, type):
    if glas == 8 and type == "тропарь":
        return Tropar.Glas8_Template()

    raise NotImplementedError()


class OsmoglasieException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

class LogicalStringsException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg

class MarkupException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg
