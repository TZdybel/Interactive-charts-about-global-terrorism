import Attack as att, AttackResult as ar, Date as d, Place as p, PlotMaker as pm, AttackDetails as ad
import csv


def getTypeFromEnum(type: int, enum):
    for value in enum:
        if value.value == type:
            return value
    return enum.OTHER_OR_UNKNOWN


def load_data(attacks: []) -> int:
    try:
        with open('/home/tzdybel/PycharmProjects/projekt2/Project2/globalterrorismdb.csv', 'r', encoding="ISO-8859-1") as csvfile:
            print("Loading data...")
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row[3] == 'iday':
                    continue

                try:
                    attkres = ar.AttackResult(bool(row[26]), bool(row[27]), int(row[98]), int(row[101]))
                except ValueError:
                    attkres = ar.AttackResult(bool(row[26]), bool(row[27]), 0, 0)

                date = d.Date(int(row[3]), int(row[2]), int(row[1]))
                place = p.Place(row[12], row[8], getTypeFromEnum(int(row[9]), p.Region))
                attkdet = ad.AttackDetails(getTypeFromEnum(int(row[28]), ad.AttackType),
                                           getTypeFromEnum(int(row[34]), ad.TargetType),
                                           getTypeFromEnum(int(row[81]), ad.WeaponType),
                                           row[64])

                attack = att.Attack(date, place, attkdet, attkres)
                attacks.append(attack)
    except FileNotFoundError:
        print("File name is invalid")
        # exit(1)

    print("Loaded " + len(attacks).__str__() + " records!")
    return len(attacks)

def get_attributes():
    print("Select weapon type you want to search for:")
    print("1 - biological")
    print("2 - chemical")
    print("3 - radiological")
    print("5 - firearms")
    print("6 - explosives")
    print("7 - fake weapons")
    print("8 - incendiary")
    print("9 - melee")
    print("10 - vehicle")
    print("11 - sabotage equipment")
    print("12 - other or unknown")
    try:
        weapontypeInt = int(input())
        if weapontypeInt < 1 or weapontypeInt > 12 or weapontypeInt == 4:
            raise ValueError
    except ValueError:
        print("Bad argument entered, exiting")
        return -1, -1
    print("Select region you want to research")
    print("1 - North America")
    print("2 - Central America and Caribbean")
    print("3 - South America")
    print("4 - East Asia")
    print("5 - Southeast Asia")
    print("6 - South Asia")
    print("7 - Central Asia")
    print("8 - Western Europe")
    print("9 - Eastern Europe")
    print("10 - Middle East and North Africa")
    print("11 - Sub-saharan Africa")
    print("12 - Australasia and Oceania")
    try:
        regionInt = int(input())
        if regionInt < 1 or regionInt > 12:
            raise ValueError
    except ValueError:
        return -1, -1
    weapontype = getTypeFromEnum(weapontypeInt, ad.WeaponType)
    region = getTypeFromEnum(regionInt, p.Region)
    return weapontype, region



if __name__ == '__main__':
    attacks = []
    load_data(attacks)
    time_to_end = False
    while(not time_to_end):
        print("Select which chart you want to see")
        print("1 - Percentage of terrorist attacks splited by region")
        print("2 - Countries with most casualties between selected dates")
        print("3 - Number of terrorist attacks between 1970 and 2016")
        print("4 - Number of attacks in selected region with selected weapon")
        print("Other value ends program")
        selection = 0
        try:
            selection = int(input())
        except ValueError:
            print("Ending...")
            time_to_end = True
            continue

        if selection == 1:
            pm.PlotMaker.percentageOfAttacksInEachRegion(attacks)
        elif selection == 2:
            print("Input start date in %d/%m/%y format")
            date1 = input()
            print("Input ending date in %d/%m/%y format")
            date2 = input()
            try:
                day, month, year = date1.split("/")
                start = d.Date(int(day), int(month), int(year))
                day, month, year = date2.split("/")
                end = d.Date(int(day), int(month), int(year))
            except ValueError:
                print("Wrong input or format, try again")
                continue
            pm.PlotMaker.countriesWithMostCasualtiesBetween(start, end, attacks)
        elif selection == 3:
            pm.PlotMaker.numberOfAttacksOverTheYears(attacks)
        elif selection == 4:
            weapontype, region = get_attributes()
            if weapontype == -1 or region == -1:
                print("Bad argument entered, exiting")
            pm.PlotMaker.numberOfAttacksInRegionWithWeapon(attacks, region, weapontype)
        else:
            print("Ending...")
            time_to_end = True
