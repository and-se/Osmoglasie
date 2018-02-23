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

class SchemaException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg

class SyllableTreeException(OsmoglasieException):
    def __init__(self, msg):
        self.message = msg

