from enum import auto

from strenum import StrEnum


class PropertyType(StrEnum):
    APARTMENT = auto()
    HOUSE = auto()
    LAND = auto()
