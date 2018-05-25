from Project2 import Place


def test_properties():
    place = Place.Place("Krakow", "Poland", Place.Region.EAST_ASIA)
    assert place.city == "Krakow"
    assert place.country == "Poland"
    assert place.region == Place.Region.EAST_ASIA

# def test_bad_args():
#     place = Place.Place(56, 76, 12)