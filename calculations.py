import sys

from database import Database


class Calculations(Database):

    def __init__(self, name, territory=None, year=None, gender="", territory_second=None):
        super().__init__(name)
        self.territory = territory
        self.territory_second = territory_second
        self.year = year
        self.gender = gender
        self.people_joined = 0
        self.people_passed = 0
        self.data = None
        self.counted_years = 0
        self.data_second = None

    def check_gender(self):
        if self.gender.lower() == "kobiety" or self.gender.lower() == "mężczyźni":
            self.gender = "AND GENDER = '{}'".format(self.gender)

    def joined(self):
        self.query("SELECT PEOPLE FROM EXAM_DATA WHERE TERRITORY = '{}' AND YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'przystąpiło' {}".format(self.territory, self.year, self.gender))
        self.people_joined = sum([item[0] for item in self.cursor.fetchall()])

    def passed(self):
        self.query("SELECT PEOPLE FROM EXAM_DATA WHERE TERRITORY = '{}' AND YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'zdało' {}".format(self.territory, self.year, self.gender))
        self.people_passed = sum([item[0] for item in self.cursor.fetchall()])

    def highest_pass(self):
        self.query("SELECT TERRITORY, MAX(PEOPLE) FROM EXAM_DATA WHERE YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'zdało' AND TERRITORY != 'Polska' {}".format(self.year, self.gender))
        self.data = [item[0] for item in self.cursor.fetchall()]
        self.data = self.data[0]

    def count_years(self):
        try:
            return int(self.year[-1]) + 1
        except ValueError as e:
            sys.exit("Third argument is invalid!")

    def average(self):
        self.data = self.data // self.count_years()

    def print(self):
        print("{} - {}".format(self.year, self.data))

    def sum(self):
        self.data = self.people_joined + self.people_passed

    def add_percent(self):
        self.data = str(self.data)
        self.data += "%"

    def percent_passed(self):
        self.data = (self.people_passed * 100) // self.data

    def get_value_for_regression(self):
        self.query("SELECT TERRITORY, PEOPLE, YEAR FROM EXAM_DATA WHERE JOINED_AND_PASSED = 'zdało' {}".format
                   (self.gender))
        self.data = self.cursor.fetchall()

    @staticmethod
    def get_cleaned_value_from_list(data):
        data = data[0]
        return data

    def count_years_from_database(self):
        self.query("SELECT MAX(YEAR) FROM EXAM_DATA")
        self.year = self.cursor.fetchall()
        self.year = self.get_cleaned_value_from_list(self.year)
        self.year = str(self.get_cleaned_value_from_list(self.year))
        self.counted_years = self.count_years()

    @staticmethod
    def print_regression(territory, year_first, year_second):
        print("{}: {} -> {}".format(territory, year_first, year_second))

    def regression(self):
        check_people = 0
        if self.gender == "":
            for i in range(0, len(self.data), 2):
                get_sum = 0
                get_sum += self.data[i][1] + self.data[i+1][1]
                if check_people > get_sum and self.data[i-1][2] != 2018:
                    self.print_regression(str(self.data[i][0]), self.data[i-1][2], self.data[i][2])
                check_people = get_sum

        else:
            for i in range(len(self.data)):
                people = self.data[i][1]
                if check_people > people and self.data[i-1][2] != 2018 and self.data[i-1][2] != self.data[i][2]:
                    self.print_regression(str(self.data[i][0]), self.data[i-1][2], self.data[i][2])
                check_people = people

    def get_value_for_compare(self):
        self.query("SELECT TERRITORY, PEOPLE, YEAR FROM EXAM_DATA WHERE TERRITORY = '{}' AND JOINED_AND_PASSED = "
                   "'zdało' {}".format(self.territory, self.gender))
        self.data = self.cursor.fetchall()
        self.query("SELECT TERRITORY, PEOPLE, YEAR FROM EXAM_DATA WHERE TERRITORY = '{}' AND JOINED_AND_PASSED = "
                   "'zdało' {}".format(self.territory_second, self.gender))
        self.data_second = self.cursor.fetchall()

    def compare(self):
        if self.gender == "":
            for i in range(0, len(self.data), 2):
                get_sum = 0
                get_sum_second = 0
                get_sum += self.data[i][1] + self.data[i+1][1]
                get_sum_second += self.data_second[i][1] + self.data_second[i+1][1]

                if get_sum_second > get_sum:
                    print("{} - {}".format(self.data_second[i][2], self.data_second[i][0]))
                else:
                    print("{} - {}".format(self.data[i][2], self.data[i][0]))
        else:
            for i in range(len(self.data)):
                people = self.data[i][1]
                people_second = self.data_second[i][1]
                if people_second > people:
                    print("{} - {}".format(self.data_second[i][2], self.data_second[i][0]))
                else:
                    print("{} - {}".format(self.data[i][2], self.data[i][0]))
