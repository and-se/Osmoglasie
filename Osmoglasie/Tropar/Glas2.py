# Author Вячеслав Какоткин

from ..SyllableTree import *
from ..AccentsSearcher import *
from ..GlasBase import *
from ..Exceptions import *

class Glas2_Template(GlasTemplateBase):
    def CreateSchema(self): #Делаем правила перехода для графа и нумерацию колен
        return Glas2_Schema()

    def MarkupLine (self, line, schema_line): #Размечаем строку, зависит от колена
        tree = SyllableTree(line) #Разложим на слова-слоги
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

    #Обозначения: Sp - речитация. В полных это слоги меж 1ым и посл. акцентом
    def Markup_1(self, tree):
        """
        Колено полное. Схема: при Sp>=2: ...~\...\~...\
                              при Sp<2: ...\~...\
        """
        accents = AccentsSearcher(tree, "first last")
        if accents.lastAccent.num - accents.firstAccent.num - 1 >= 2: #Возможны ошибки
            accents.firstAccent.setWaveAccent().next.setDown()
        accents.lastAccent.setWaveAccent().prev.setDown()
        tree.last.setDown()
        return tree

    def Markup_2(self, tree):
        """
        Колено неполное, лишь посл. акцент. Схема: ...-/...
        """
        accents = AccentsSearcher(tree, "last")
        
        if len(accents.afterStressed) == 1:
            accents.lastAccent.setWaveAccent()
        else:
            accents.lastAccent.setPauseAccent().next.setUp()
            
        return tree

    def Markup_3(self, tree):
        """
        Колено полное. Схема: PreFirstAccentArea^SpeechArea^...\
        PreFirstAccentArea=None при len(beforeStressed)==0
                          =.../ при len(beforeStressed)>=1
        SpeechArea =\\...\ при Sp>=3
                   =\\ при Sp=2
                   =\ при Sp=1
        """
        accents = AccentsSearcher(tree, "first last")
        PreFirstAccentArea = len(accents.beforeStressed)
        SpeechArea = accents.lastAccent.num - accents.firstAccent.num - 1
        accents.firstAccent.setUpperAccent()
        if PreFirstAccentArea >= 1:
            accents.firstAccent.prev.setUp()
        if SpeechArea >= 1:
            accents.firstAccent.next.setDown()
        if SpeechArea >= 2:
            accents.firstAccent.next.next.setDown()
        if SpeechArea >= 3:
            accents.lastAccent.prev.setDown()
        accents.lastAccent.setUpperAccent()
        tree.last.setDown()
        return tree

    def Markup_K(self, tree):
        """
        Колено неполное, лишь посл. акцент. Схема: .../ \/ \...
        
        Если заударный слог 1, то ... / ~ .
        """
        accents = AccentsSearcher(tree, "last")
        
        accents.lastAccent.prev.setUp()
        
        if(len(accents.afterStressed) > 1):
            accents.lastAccent.setLowerAccent().next.setDown()
        else:
            accents.lastAccent.setWaveAccent()
            
        return tree

class Glas2_Schema(GlasSchemaBase):
    def __init__(self):
        self.current = None

    def CheckStringCount(self, n):
        if n < 3:
            raise SchemaException("Неправильное количество колен для 2 гласа")

    def Next(self, ostatok):
        if not self.current:
            self.CheckStringCount(ostatok)
            self.current = "1"
            return
        if self.current == "1":
            self.current = "2"
        elif self.current == "2":
            if ostatok == 1:
                raise SchemaException("С колена %s возможен переход только на конечное" % self.current)
            else:
                self.current = "3"
        elif self.current == "3":
            if ostatok == 1:
                raise SchemaException("С колена %s возможен переход только на конечное" % self.current)
            else:
                self.current = "2"

    def Last (self):
        if self.current == "2" or self.current == "3":
            self.current = "К"
            return
        raise SchemaException("С колена %s переход в конечное колено невозможен" % self.current)