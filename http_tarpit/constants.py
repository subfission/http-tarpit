import enum
import logging


@enum.unique
class OperationMode(enum.Enum):
    clock = 1
    newline = 2
    urandom = 3
    null = 4
    slow_newline = 5

    def __str__(self):
        return self.name

    def __contains__(self, e):
        return e in self.__members__


class LogLevel(enum.IntEnum):
    debug = logging.DEBUG
    info = logging.INFO
    warn = logging.WARN
    error = logging.ERROR
    fatal = logging.FATAL
    crit = logging.CRITICAL

    def __str__(self):
        return self.name

    def __contains__(self, e):
        return e in self.__members__
