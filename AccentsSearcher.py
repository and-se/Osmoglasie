from SyllableTree import *

class AccentsSearcher:
    def __init__(self, tree, mode):
        self.tree = tree

        self.FindAccents(mode)

    unwanted = ["яко", "убо", "аще", "еси"]

    def Reset(self):
        self.firstAccent = None
        self.lastAccent = None
        self.preLastAccent = None

    """
    Найти акценты.
    type содержит указания об искомых акцентах черех пробле:
    last - последний
    first - первый
    preLast - предпослединй

    Поиск происходит в порядке перечисления акцентов в type
    """
    def FindAccents (self, type):
        # Сбрасываем информацию об акцентах
        self.Reset()

        if type == "last":
            self.FindLastAccent()
        else:
            raise NotImplemented(task)



    def FindLastAccent(self):
        w = self.tree.lastWord

        # Если ударным является последний слог строки, переносим
        # последний акцент назад
        if w.stressedSyllable == self.tree.last:
            w = w.prev

        # Пропускаем предлоги союзы и проч. несмысловые вещи
        while w and not w.canBeAccent():
            w = w.prev

        # Нашли кандидат на последний акцент
        candidateLast = w

        if candidateLast in self.unwanted:
            candidateLast = w.prev

        self.lastAccent = candidateLast.stressedSyllable
"""
        w = self.firstWord

        while w and not w.canBeAccent():
            w = w.next

        candidateFirst = w

        if candidateFirst.num >= candidateLast.num:
            candidateFirst = None

        #TODO предпоследний акцент
"""




