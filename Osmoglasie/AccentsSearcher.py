from .SyllableTree import *
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

        # Заударные слоги (после последнего акцента)
        self.afterStressed = None

        # Слоги между первым и последним акцентами
        self.FLbetweenStressed = None

    """
    Найти акценты.
    type содержит указания об искомых акцентах через пробел:
    last - последний
    first - первый
    prelast - предпослединй
    UseLastSyl - указание допустить постановку акцента на последний слог строки
    """
    def FindAccents (self, type):
        # Сбрасываем информацию об акцентах
        self.Reset()

        # Специальный случай для первого колена первого гласа
        # где можно ставить акцент на последний слог строки
        aboutLastAcc = "no requirements"
        if "UseLastSyl" in type:
            aboutLastAcc = "UseLastSyl"
            type = type[:-11]
        if type == "last":
            self._FindLastAccent(aboutLastAcc)
        elif type == "prelast last":
            self._FindLastAccent(aboutLastAcc)
            self._FindPreLastAccent()
        elif type == "first last":
            self._FindLastAccent(aboutLastAcc)
            self._FindFirstAccent()
            if self.firstAccent.num > self.lastAccent.num:
                raise MarkupException("Есть слишком короткая строка.")
        else:
            raise NotImplemented(type)

    def _StandartBackSearch(self, startWord):
        w = startWord

        # Пропускаем предлоги союзы и проч. несмысловые вещи
        while w and not w.canBeAccent():
            w = w.prev

        # Нашли кандидат
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


    def _FindFirstAccent(self):
        w = self.tree.firstWord

        w = self._StandartForwardSearch(w)

        self.firstAccent = w.stressedSyllable

        #Межударные слоги
        self.FLbetweenStressed = []

        if self.firstAccent != self.lastAccent:
            syl = self.firstAccent.next
            # Пока не дошли до последнего акцента
            while syl != self.lastAccent:
                self.FLbetweenStressed.append(syl)
                syl = syl.next



    def _FindLastAccent(self, glas):
        w = self.tree.lastWord

        # Если ударным является последний слог строкии это необходимо,
        # переносим последний акцент назад
        if w.stressedSyllable == self.tree.last and glas != "UseLastSyl":
            w = w.prev

        w = self._StandartBackSearch(w)

        self.lastAccent = w.stressedSyllable

        # Заударные слоги
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









"""
        w = self.firstWord

        while w and not w.canBeAccent():
            w = w.next

        candidateFirst = w

        if candidateFirst.num >= candidateLast.num:
            candidateFirst = None

        #TODO предпоследний акцент
"""




