from enum import auto

from strenum import StrEnum


class SellerType(StrEnum):
    AGENCY = auto()
    DEVELOPER = auto()
    PRIVATE = auto()
    MUNICIPALITY = auto()
    BAILIFF = auto()
    KOWR = auto()
