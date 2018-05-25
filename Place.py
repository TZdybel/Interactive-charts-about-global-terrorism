from enum import Enum


class Region(Enum):
    NORTH_AMERICA = 1
    CENTRAL_AMERICA_AND_CARIBBEAN = 2
    SOUTH_AMERICA = 3
    EAST_ASIA = 4
    SOUTHEAST_ASIA = 5
    SOUTH_ASIA = 6
    CENTRAL_ASIA = 7
    WESTERN_EUROPE = 8
    EASTERN_EUROPE = 9
    MIDDLE_EAST_AND_NORTH_AFRICA = 10
    SUB_SAHARAN_AFRICA = 11
    AUSTRALASIA_AND_OCEANIA = 12


class Place(object):
    """Class storing info about some place in the world"""

    def __init__(self,  city: str, country: str, region: Region):
        self.__city = city
        self.__country = country
        self.__region = region

    @property
    def country(self):
        return self.__country

    @property
    def region(self):
        return self.__region

    @property
    def city(self):
        return self.__city

    def __str__(self):
        return "{0}, {1} - {2}".format(self.__city, self.__country, self.__region.name)

