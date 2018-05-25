class AttackResult(object):

    def __init__(self, is_successful: bool, is_suicide_committed: bool, num_of_kills: int, num_of_wounded: int):
        # try:
        if num_of_kills < 0 or num_of_wounded < 0:
            raise ValueError
        # except ValueError:
        #     print("Numbers cannot be less than 0")
        #     exit(1)
        self.__is_successful = is_successful
        self.__is_suicide_committed = is_suicide_committed
        self.__num_of_kills = num_of_kills
        self.__num_of_wounded = num_of_wounded

    @property
    def is_successful(self):
        return self.__is_successful

    @property
    def is_suicide_committed(self):
        return self.__is_suicide_committed

    @property
    def num_of_kills(self):
        return self.__num_of_kills

    @property
    def num_of_wounded(self):
        return self.__num_of_wounded

    def __str__(self):
        return "Was successful: {0}, was suicide committed: {1}, number of killed: {2}, number of wounded: {3}".format(
            self.__is_successful, self.__is_suicide_committed, self.__num_of_kills, self.__num_of_wounded)
