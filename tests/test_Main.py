from Project2 import Main
from Project2 import AttackDetails


def test_enum_getter():
    assert Main.getTypeFromEnum(1, AttackDetails.AttackType) == AttackDetails.AttackType.ASSASSINATION
    assert Main.getTypeFromEnum(5, AttackDetails.WeaponType) == AttackDetails.WeaponType.FIREARMS
    assert Main.getTypeFromEnum(6, AttackDetails.TargetType) == AttackDetails.TargetType.AIRPORTS_AIRCRAFT
    assert Main.getTypeFromEnum(23, AttackDetails.TargetType) == AttackDetails.TargetType.OTHER_OR_UNKNOWN


def test_load_data():
    attacks = []
    Main.load_data(attacks)
    assert len(attacks) == 170350