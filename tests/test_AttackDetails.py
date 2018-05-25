from Project2 import AttackDetails as ad


def test_properties():
    atckdet = ad.AttackDetails(ad.AttackType.ASSASSINATION, ad.TargetType.MILITARY, ad.WeaponType.BIOLOGICAL, "motyw")
    assert atckdet.attack_type == ad.AttackType.ASSASSINATION
    assert atckdet.target_type == ad.TargetType.MILITARY
    assert atckdet.weapon_type == ad.WeaponType.BIOLOGICAL
    assert atckdet.motive == "motyw"

def test_motyw_str():
    atckdet = ad.AttackDetails(ad.AttackType.ASSASSINATION, ad.TargetType.MILITARY, ad.WeaponType.BIOLOGICAL, "")
    atckdet1 = ad.AttackDetails(ad.AttackType.ASSASSINATION, ad.TargetType.MILITARY, ad.WeaponType.BIOLOGICAL)
    assert atckdet.motive == "Unknown"
    assert atckdet1.motive == "Unknown"

def test_equal():
    atckdet = ad.AttackDetails(ad.AttackType.ASSASSINATION, ad.TargetType.MILITARY, ad.WeaponType.BIOLOGICAL, "")
    atckdet1 = ad.AttackDetails(ad.AttackType.ASSASSINATION, ad.TargetType.MILITARY, ad.WeaponType.BIOLOGICAL)
    assert atckdet1 == atckdet
