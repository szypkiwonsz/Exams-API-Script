from database import Database


class Calculation(Database):

    def __init__(self, name, territory=None, year=None, gender=""):

        super().__init__(name)
        self.territory = territory
        self.year = year
        self.gender = gender
        self.data = None
        self.joined_people = 0
        self.passed_people = 0
        self.counted_years = 0

    def print_result(self):

        print("{} - {}".format(self.year, self.data))

    def if_gender(self):

        if self.gender != "":
            self.gender = "AND GENDER = '{}'".format(self.gender)

    def count_years(self):

        self.counted_years = int(self.year[-1]) + 1

    def average(self):

        self.data = self.data // self.counted_years

    def add_percent(self):
        self.data = str(self.data)
        self.data += "%"

    def percent(self):

        self.data = (self.passed_people * 100) // self.data

    def sum(self):

        self.data = self.joined_people + self.passed_people

    @staticmethod
    def get_cleaned_value_from_list(data):
        data = data[0]
        return data

    def joined(self):

        self.query("SELECT PEOPLE FROM EXAM_DATA WHERE TERRITORY = '{}' AND YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'przystąpiło' {}".format(self.territory, self.year, self.gender))
        self.joined_people = sum([item[0] for item in self.cursor.fetchall()])

    def passed(self):

        self.query("SELECT PEOPLE FROM EXAM_DATA WHERE TERRITORY = '{}' AND YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'zdało' {}".format(self.territory, self.year, self.gender))
        self.passed_people = sum([item[0] for item in self.cursor.fetchall()])

    def highest_pass(self):

        self.query("SELECT TERRITORY, MAX(PEOPLE) FROM EXAM_DATA WHERE YEAR <= '{}' AND JOINED_AND_PASSED = "
                   "'zdało' AND TERRITORY != 'Polska' {}".format(self.year, self.gender))
        self.data = [item[0] for item in self.cursor.fetchall()]

    def get_value_for_regression(self):

        self.query("SELECT TERRITORY, PEOPLE, YEAR FROM EXAM_DATA WHERE JOINED_AND_PASSED = 'zdało' {}".format(self.gender))
        self.data = self.cursor.fetchall()

    def count_years_from_database(self):

        self.query("SELECT MAX(YEAR) FROM EXAM_DATA")

        self.year = self.cursor.fetchall()
        self.year = self.get_cleaned_value_from_list(self.year)
        self.year = str(self.get_cleaned_value_from_list(self.year))
        self.count_years()

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

    # def get_value_for_compare(self):
    #
    #     self.query("SELECT TERRITORY, PEOPLE, YEAR FROM EXAM_DATA WHERE TERRITORY =  JOINED_AND_PASSED = 'zdało' {}".format(self.gender))
    #     self.data = self.cursor.fetchall()
    #
    # def compare(self):

