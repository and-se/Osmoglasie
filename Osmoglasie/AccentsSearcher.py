﻿from .SyllableTree import *
from .Exceptions import *

class AccentsSearcher:
    def __init__(self, tree, mode):
        self.tree = tree

        self.FindAccents(mode)

    unwanted = ["яко", "убо", "аще", "еси"]

    def Reset(self):
        self.firstAccent = None
        self.lastAccent = None
        self.preLastAccent = None

        # Заударные (после последнего акцента) и предударные (перед первым акцентом) слоги
        self.afterStressed = None
        self.beforeStressed = None


    """
    Найти акценты.
    type содержит указания об искомых акцентах через пробел:    
    first - первый
    prelast - предпослединй
    last - последний
    UseLastSyl - указание допустить постановку акцента на последний слог строки
    """
    def FindAccents (self, type):
        # Сбрасываем информацию об акцентах
        self.Reset()
        
        isLastSyllableAllowed = False
        
        if type.endswith(" UseLastSyl"):
            isLastSyllableAllowed = True
            type = type[:-11]            
            
        if self.TryFindManualAccents(type):
            return

        if type == "first":
            self._FindFirstAccent()
        elif type == "last":
            self._FindLastAccent(isLastSyllableAllowed)
        elif type == "prelast last":
            self._FindLastAccent(isLastSyllableAllowed)
            self._FindPreLastAccent()
        elif type == "first last":
            self._FindFirstAccent()
            self._FindLastAccent(isLastSyllableAllowed)
            #if self.firstAccent.num > self.lastAccent.num:
            #    raise MarkupException("Есть слишком короткая строка.")
        else:
            raise NotImplementedError(type)
            
    # Попытка найти расставленные вручную акценты
    def TryFindManualAccents(self, type):
        # Получим вручную расставленные акценты
        mAcc = [x for x in self.tree.syllables if x.isAccent]
        
        if not mAcc:
            return False
            
        # Список искомых акцентов
        targetAccs = type.split()

        # Если в строке есть ручной акцент, то все акценты в строке должны
        # быть расставлены вручную        
        if len(targetAccs) != len(mAcc):
            raise MarkupException("В строке '%s' расставлены не все требуемые акценты: %s" % (str(self.tree), type))
           
        for i in range(len(targetAccs)):
            if targetAccs[i] == "first":
                self.firstAccent = mAcc[i]
                self._BuildBeforeStressed()
            elif targetAccs[i] == "prelast":
                self.preLastAccent = mAcc[i]
            elif targetAccs[i] == "last":
                self.lastAccent = mAcc[i]
                self._BuildAfterStressed()
                
        return True

    def _StandartBackSearch(self, startWord):
        w = startWord

        # Пропускаем предлоги союзы и проч. несмысловые вещи
        while w and not w.canBeAccent():
            w = w.prev

        # Нашли кандидата
        candidate = w

        # TODO пропускаем несмысловой, пока один
        if candidate in self.unwanted:
            candidate = w.prev

        return candidate

    def _StandartForwardSearch(self, startWord):
        w = startWord

        # Пропускаем предлоги союзы и проч. несмысловые вещи
        while w and not w.canBeAccent():
            w = w.next

        # Нашли кандидат
        candidate = w

        # TODO пропускаем несмысловой, пока один
        if candidate in self.unwanted:
            candidate = w.next

        return candidate

    def _FindLastAccent(self, isLastSyllableAllowed):
        w = self.tree.lastWord

        # Если ударным является последний слог строкии это необходимо,
        # переносим последний акцент назад
        if w.stressedSyllable == self.tree.last and not isLastSyllableAllowed:
            w = w.prev

        w = self._StandartBackSearch(w)

        self.lastAccent = w.stressedSyllable

        #Тут добавим к случаю с firstAccent
        if self.firstAccent != None and self.firstAccent.num > self.lastAccent.num:
            raise MarkupException("В строке %s первый акцент оказался впереди последнего" % str(self.tree))

        # Заударные слоги        
        self._BuildAfterStressed()

            
    def _BuildAfterStressed(self):
        self.afterStressed = []
        syl = self.lastAccent.next

        while syl:
            self.afterStressed.append(syl)
            syl = syl.next
    

    def _FindPreLastAccent(self):
        start = self.lastAccent.parentWord

        #TODO двусоставные слова

        w = start.prev

        w = self._StandartBackSearch(w)

        if not w:
            raise MarkupException("Не удалось найти последний акцент в строке %s" % str(self.tree))

        self.preLastAccent = w.stressedSyllable

    def _FindFirstAccent(self):
        w = self.tree.firstWord
        w = self._StandartForwardSearch(w)
        self.firstAccent = w.stressedSyllable

        #Предударные слоги
        self._BuildBeforeStressed()
            
    def _BuildBeforeStressed(self):
        self.beforeStressed = []
        syl = self.tree.first
        while syl != self.firstAccent:
            self.beforeStressed.append(syl)
            syl = syl.next

    

"""
        w = self.firstWord

        while w and not w.canBeAccent():
            w = w.next

        candidateFirst = w

        if candidateFirst.num >= candidateLast.num:
            candidateFirst = None

        #TODO предпоследний акцент
"""




