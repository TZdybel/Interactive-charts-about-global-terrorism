import AttackResult as ar, Date as d, Place as p, AttackDetails as ad


class Attack(object):

    def __init__(self, date: d.Date, place: p.Place, attack_details: ad.AttackDetails, attack_result: ar.AttackResult):
        self.__date = date
        self.__place = place
        self.__attack_details = attack_details
        self.__attack_result = attack_result

    @property
    def date(self):
        return self.__date

    @property
    def place(self):
        return self.__place

    @property
    def attack_details(self):
        return self.__attack_details

    @property
    def attack_result(self):
        return self.__attack_result

    def __str__(self):
        return "Date - {0}\nPlace - {1}\nAttack Details - {2}\nAttack Result - {3}".format(self.date.__str__(),
                                                                                           self.place.__str__(),
                                                                                           self.attack_details.__str__(),
                                                                                           self.attack_result.__str__())
