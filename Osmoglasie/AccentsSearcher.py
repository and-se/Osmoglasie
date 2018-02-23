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


    """
    Найти акценты.
    type содержит указания об искомых акцентах через пробел:
    last - последний
    first - первый
    prelast - предпослединй
    """
    def FindAccents (self, type):
        # Сбрасываем информацию об акцентах
        self.Reset()

        if type == "last":
            self._FindLastAccent()
        elif type == "prelast last":
            self._FindLastAccent()
            self._FindPreLastAccent()
        elif type == "first last":
            self._FindLastAccent()
            self._FindFirstAccent()
        else:
            raise NotImplemented(task)

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

    def _FindLastAccent(self):
        w = self.tree.lastWord

        # Если ударным является последний слог строки, переносим
        # последний акцент назад
        if w.stressedSyllable == self.tree.last:
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

    def _FindFirstAccent(self):
        w = self.tree.firstWord
        w = self._StandartForwardSearch(w)

        self.firstAccent = w.stressedSyllable

        # Проверка
        firstAc = self.firstAccent
        while firstAc != self.tree.last:
            if firstAc == self.lastAccent:
                break;
            else:
                firstAc = firstAc.next
        if firstAc != self.lastAccent:
            raise MarkupException("Первый акцент правее последнего!!!")


"""
        w = self.firstWord

        while w and not w.canBeAccent():
            w = w.next

        candidateFirst = w

        if candidateFirst.num >= candidateLast.num:
            candidateFirst = None

        #TODO предпоследний акцент
"""




