import Project2 as p
from Project2 import Attack

def test_properties():
    at = Attack.Attack(p.Date.Date(1, 2, 2003), p.Place.Place("1", "2", p.Place.Region.EASTERN_EUROPE),
                         p.AttackDetails.AttackDetails(p.AttackDetails.AttackType.ARMED_ASSAULT,
                                                       p.AttackDetails.TargetType.AIRPORTS_AIRCRAFT,
                                                       p.AttackDetails.WeaponType.BIOLOGICAL,
                                                       "motyw"),
                         p.AttackResult.AttackResult(True, True, 1, 2))
    assert at.date == p.Date.Date(1, 2, 2003)
    assert at.place.city == "1" and at.place.country == "2" and at.place.region == p.Place.Region.EASTERN_EUROPE
    assert at.attack_details == p.AttackDetails.AttackDetails(p.AttackDetails.AttackType.ARMED_ASSAULT,
                                                       p.AttackDetails.TargetType.AIRPORTS_AIRCRAFT,
                                                       p.AttackDetails.WeaponType.BIOLOGICAL,
                                                       "motyw")
    assert at.attack_result.is_successful == True and at.attack_result.is_suicide_committed == True and \
           at.attack_result.num_of_kills == 1 and at.attack_result.num_of_wounded == 2