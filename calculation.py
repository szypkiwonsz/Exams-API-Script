from database import Database


class Calculation(Database):

    def __init__(self, name, territory, year, gender=""):

        super().__init__(name)
        self.territory = territory
        self.year = year
        self.gender = gender
        self.data = None
        self.joined_people = 0
        self.passed_people = 0

    def print_result(self):

        print("{} - {}".format(self.year, self.data))

    def if_gender(self):

        if self.gender != "":
            self.gender = "AND GENDER = '{}'".format(self.gender)

    def average(self):

        years = int(self.year[-1]) + 1
        self.data = self.data // years

    def percent(self):

        self.data = (self.passed_people * 100) // self.data

    def sum(self):

        self.data = self.joined_people + self.passed_people

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
        print(self.data)