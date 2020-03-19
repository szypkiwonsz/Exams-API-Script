import sys

from api import Api
from calculations import Calculations
from database import Database
args = sys.argv


class Arguments:
    def __init__(self, arguments):

        self.arguments = arguments
        self.first = ""
        self.second = ""
        self.third = ""
        self.fourth = ""

    def get_arguments(self):
        if len(self.arguments) == 1:
            self.first = self.arguments[0]

        elif len(self.arguments) == 2:
            self.first = self.arguments[0]
            self.second = self.arguments[1]

        elif len(self.arguments) == 3:
            self.first = self.arguments[0]
            self.second = self.arguments[1]
            self.third = self.arguments[2]

        else:
            self.first = self.arguments[0]
            self.second = self.arguments[1]
            self.third = self.arguments[2]
            self.fourth = self.arguments[3]

    def first_command(self):
        if self.first == "--1" and self.second != "" and self.third != "":
            return True

    def second_command(self):
        if self.first == "--2" and self.second != "" and self.third != "":
            return True

    def third_command(self):
        if self.first == "--3" and self.second != "":
            return True

    def fourth_command(self):
        if self.first == "--4":
            return True

    def fifth_command(self):
        if self.first == "--5" and self.second != "" and self.third != "":
            return True

    def help_command(self):
        if self.first == "--help":
            return True

    def get_data(self):
        if self.first == "--get_data":
            return True


if __name__ == '__main__':

    argument = Arguments(args[1:])
    argument.get_arguments()

    database = Database("exams_data.sqlite")
    if database.is_empty() and argument.first != "--get_data":
        print("First, you have to fill database with data! Command: --get_data")
        sys.exit()
    database.close()

    if argument.first_command():
        first_command = Calculations("exams_data.sqlite", argument.second, argument.third, argument.fourth)
        first_command.check_gender()
        first_command.joined()
        first_command.sum()
        first_command.average()
        first_command.print()
        first_command.close()

    elif argument.second_command():
        second_command = Calculations("exams_data.sqlite", argument.second, argument.third, argument.fourth)
        second_command.check_gender()
        second_command.joined()
        second_command.passed()
        second_command.sum()
        second_command.percent_passed()
        second_command.add_percent()
        second_command.print()
        second_command.close()

    elif argument.third_command():
        third_command = Calculations("exams_data.sqlite", None, argument.second, argument.third)
        third_command.check_gender()
        third_command.highest_pass()
        third_command.print()
        third_command.close()

    elif argument.fourth_command():
        fourth_command = Calculations("exams_data.sqlite", None, None, argument.third)
        fourth_command.check_gender()
        fourth_command.get_value_for_regression()
        fourth_command.count_years_from_database()
        fourth_command.regression()
        fourth_command.close()

    elif argument.fifth_command():
        fifth_command = Calculations("exams_data.sqlite", argument.second, None, argument.fourth, argument.third)
        fifth_command.check_gender()
        fifth_command.get_value_for_compare()
        fifth_command.compare()
        fifth_command.close()

    elif argument.get_data():
        api = Api("https://api.dane.gov.pl/resources/17363/data", "exams_data.sqlite")
        if api.is_empty():
            api.get_insert_data()
        else:
            print("Database is already filled with data!")

    elif argument.help_command():
        print('Commands:')
        print('REMEMBER: FIRST YOU SHOULD FILL THE DATABASE WITH DATA. -> "--get_data"')
        print('Choosing to divide results by gender is not required but it is possible by adding the last command '
              'as "kobiety" or "mężczyźni".')
        print(' --help -> show this basic help menu.')
        print(' --get_data -> Importing data from api to database.')
        print(' --1 TERRITORY YEAR -> displaying the average number of people who took the exam for a given '
              'province over the years, up to the given year.')
        print(
            ' --2 TERRITORY YEAR -> displaying the percentage pass rate for a given province over the years, e.g.')
        print(' --3 YEAR -> Providing the voivodship with the best pass rate in a given year.')
        print(' --4 -> Displaying voivodships that recorded a decrease in the success rate in the following year.')
        print(' --5 FIRST_TERRITORY SECOND_TERRITORY -> comparison of two voivodships - for the two voivodships '
              'listed, listing which voivodship had better pass rates in each available year.')
    else:
        print("This command not exist! Write: python script.py --help")
