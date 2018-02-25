class GlasTemplateBase:
    """
    Получить схему гласа (наследник GlasSchemaBase)
    """
    def CreateSchema(self):
        raise NotImplemented("abstract")

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
            ost = ost - 1
            result.append(self.MarkupLine(s, schema.current))

        schema.Last()
        result.append(self.MarkupLine(strings[-1], schema.current))

        return result

    """
    Размечает строку на указанное колено
    """
    def MarkupLine (self, line, schema_line):
        raise NotImplemented("abstract")

class GlasSchemaBase:

    def __init__(self):
        # Текущее колено, изначально никакое
        self.current = None

    """
    Перейти к следующему колену.
    ostatok - количество неразмеченных колен, изначально 0
    """
    def Next(self, ostatok):
        raise NotImplemented("abstract")

    """
    Перейти к последнему колену, если это возможно из текущей позиции.
    Иначе - исключение SchemaException
    """
    def Last(self):
        raise NotImplemented("abstract")
