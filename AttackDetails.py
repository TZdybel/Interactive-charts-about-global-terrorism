from enum import Enum


class AttackType(Enum):
    ASSASSINATION = 1
    ARMED_ASSAULT = 2
    BOMBING_OR_EXPLOSION = 3
    HIJACKING = 4
    HOSTAGE_WITH_BARRICADE_INCIDENT = 5
    HOSTAGE_TAKING = 6
    INFRASTRUCTURE_ATTACK = 7
    UNARMER_ASSAULT = 8
    OTHER_OR_UNKNOWN = 9


class TargetType(Enum):
    GOVERNMENT = 2  #ALSO 7
    POLICE = 3
    MILITARY = 4
    AIRPORTS_AIRCRAFT = 6
    EDUCATIONAL_INSTITUTION = 8
    JOURNALISTS_AND_MEDIA = 10
    PRIVATE_CITIZENS_AND_PROPERTY = 14
    TRANSPORTATION = 19
    UTILITIES = 21
    OTHER_OR_UNKNOWN = 13


class WeaponType(Enum):
    BIOLOGICAL = 1
    CHEMICAL = 2
    RADIOLOGICAL = 3
    FIREARMS = 5
    EXPLOSIVES = 6
    FAKE_WEAPONS = 7
    INCENDIARY = 8
    MELEE = 9
    VEHICLE = 10
    SABOTAGE_EQUIPMENT = 11
    OTHER_OR_UNKNOWN = 12  #ALSO 13


class AttackDetails(object):
    """Class containing info about attack type, weapon and possible motive"""

    def __init__(self, attack_type: AttackType, target_type: TargetType, weapon_type: WeaponType, motive: str="Unknown"):
        self.__attack_type = attack_type
        self.__target_type = target_type
        if motive == '':
            motive = "Unknown"
        self.__motive = motive
        self.__weapon_type = weapon_type

    @property
    def attack_type(self):
        return self.__attack_type

    @property
    def target_type(self):
        return self.__target_type

    @property
    def motive(self):
        return self.__motive

    @property
    def weapon_type(self):
        return self.__weapon_type

    def __str__(self):
        return "Attack type: {0}, Target type: {1}, Weapon type: {2}, Possible motive: {3}".format(self.__attack_type.name, self.__target_type.name, self.__weapon_type.name, self.__motive)

    def __eq__(self, other):
        return self.attack_type == other.attack_type and self.target_type == other.target_type and \
               self.weapon_type == other.weapon_type and self.motive == other.motive