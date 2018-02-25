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
from .Exceptions import *
from . import Tropar
from . import Stihira

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
    if type != "тропарь" and type != "стихира":
        raise NotImplementedError()
        
    if type == "тропарь":
        if glas == 1:
            return Tropar.Glas1_Template()
        elif glas == 2:
            return Tropar.Glas2_Template()
        elif glas == 3:
            return Tropar.Glas3_Template()
        elif glas == 4:
            return Tropar.Glas4_Template()        
        elif glas == 5:
            return Tropar.Glas5_Template()
        elif glas == 6:
            return Tropar.Glas6_Template()        
        elif glas == 7:
            return Tropar.Glas7_Template()
        elif glas == 8:
            return Tropar.Glas8_Template()
            
    elif type == "стихира":
        if glas == 1:
            return Stihira.Glas1Stih_Template()            

    raise NotImplementedError()

