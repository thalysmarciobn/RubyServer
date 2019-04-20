from enum import Enum, unique


@unique
class Rules(Enum):
    session = 0
    sessionAndClient = 1
    client = 2