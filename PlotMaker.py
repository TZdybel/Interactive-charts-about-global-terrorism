import matplotlib.pyplot as plt
import Date as d, Place as p, AttackDetails as ad
import operator
import numpy as np
from pylab import *


class PlotMaker(object):

    # def __init__(self):
    #     pass

    @staticmethod
    def percentageOfAttacksInEachRegion(attacks: []):
        fig = plt.figure(figsize=(9, 9))
        slices = [0] * 12
        # regions = ["North America", "Central America and Caribbean", "South America", "East Asia", "Southeast Asia",
        #            "South Asia", "Central Asia", "Western Europe", "Eastern Europe", "Middle East and North Africa",
        #            "Sub-Saharan Africa", "Australasia and Oceania"]
        regions = []
        for value in p.Region:
            regions.append(value.name)
        for attack in attacks:
            slices[attack.place.region.value - 1] += 1
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'tab:orange', 'tab:purple', 'tab:pink', 'tab:gray', 'tab:olive',
                  '#0F0F0F']
        plt.pie(slices, labels=regions, startangle=25, colors=colors, autopct='%1.1f%%', pctdistance=0.7)
        plt.title("Percentage of terrorist attacks\nsplited by region")
        plt.subplots_adjust(left=0.06, bottom=0.15, right=0.84, top=0.90, wspace=1, hspace=0)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), shadow=True, ncol=2)
        plt.show()

    @staticmethod
    def countriesWithMostCasualtiesBetween(date1: d.Date, date2: d.Date, attacks: []):
        if date2 < date1:
            print("End data must be after starting date")
            return
        fig = plt.figure(figsize=(9, 9))
        all_countries = {}
        for attack in attacks:
            if date1 <= attack.date <= date2:
                if attack.place.country in all_countries:
                    casualties = all_countries[attack.place.country]
                    all_countries[attack.place.country] = attack.attack_result.num_of_kills + casualties
                else:
                    all_countries[attack.place.country] = attack.attack_result.num_of_kills

        sorted_dict = sorted(all_countries.items(), key=operator.itemgetter(1))
        sorted_dict.reverse()

        countries_list = []
        casualties = []
        for x in range(10):
            countries_list.append(sorted_dict[x][0])
            casualties.append(sorted_dict[x][1])

        countries = np.arange(len(countries_list))
        plt.bar(countries, casualties, width=0.5)
        plt.xticks(countries, countries_list, rotation=45)
        plt.subplots_adjust(top=0.95, bottom=0.15)
        plt.title("Countries with most casualties between {0} and {1}".format(date1, date2))
        plt.yticks(np.arange(min(casualties), max(casualties) + 1, max(casualties) // 10), rotation=45)
        plt.xlabel("Country")
        plt.ylabel("Casualties")
        plt.show()

    @staticmethod
    def numberOfAttacksOverTheYears(attacks: []):
        years = [x for x in range(1970, 2017)]
        numOfAttacks = [0 for x in range(1970, 2017)]
        for attack in attacks:
            idx = years.index(attack.date.year)
            numOfAttacks[idx] += 1

        fig = plt.figure(figsize=(9, 9))
        plt.plot(years, numOfAttacks, color='r')
        plt.fill_between(years, numOfAttacks, 0, facecolor='r')
        plt.title("Number of terrorist attacks between 1970 and 2016")
        plt.xticks(np.arange(min(years), max(years)+1, 5), rotation=45)
        plt.xlabel("Year")
        plt.ylabel("Number of attacks")
        plt.margins(x=0, y=0)
        plt.show()

    @staticmethod
    def numberOfAttacksInRegionWithWeapon(attacks: [], region: p.Region, weapontype: ad.WeaponType):
        all_cities = {}
        for attack in attacks:
            if attack.place.region == region and attack.attack_details.weapon_type == weapontype:
                if attack.place.city in all_cities:
                    all_cities[attack.place.city] += 1
                else:
                    all_cities[attack.place.city] = 1

        sorted_dict = sorted(all_cities.items(), key=operator.itemgetter(1))
        sorted_dict.reverse()

        val = []
        labels = []
        if len(sorted_dict) < 10:
            rang = len(sorted_dict)
        else:
            rang = 10
        for x in range(rang):
            if sorted_dict[x][0] == "Unknown":
                continue
            else:
                labels.append(sorted_dict[x][0])
                val.append(sorted_dict[x][1])
        pos = arange(len(val)) + .5  # the bar centers on the y axis

        fig = plt.figure(figsize=(9, 9))
        plt.barh(pos, val, align='center', color="tab:orange")
        plt.yticks(pos, labels)
        plt.xlabel('Number of attacks')
        plt.title("Number of attacks in {0} with use of {1}".format(region.name, weapontype.name))
        plt.grid(True)
        plt.show()
