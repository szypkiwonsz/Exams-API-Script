import sys

from api import Api
from calculation import Calculation

args = sys.argv


class Script:

    def __init__(self, command, first_arg, second_arg, third_arg, fourth_arg):

        self.command = command
        self.first_arg = first_arg
        self.second_arg = second_arg
        self.third_arg = third_arg
        self.fourth_arg = fourth_arg

    @staticmethod
    def check_gender(argument):
        if argument == "kobiety" or argument == "mężczyźni" or argument == "":
            return True
        else:
            return False

    @staticmethod
    def check_year(argument):
        try:
            if 2009 < int(argument) < 2019:
                return True
            else:
                return False
        except ValueError as e:
            sys.exit("Arguments are invalid!")

    def empty_command(self):
        if len(self.command) == 0:
            print("This command not exist! Write: python script.py --help")

    def get_data(self):
        if self.first_arg == "--get_data":
            api = Api("https://api.dane.gov.pl/resources/17363/data", "exams_data.sqlite")
            if api.is_empty():
                api.get_insert_data()
            else:
                print("Database is already filled with data!")

    def first(self):
        if self.first_arg == "--1" and self.second_arg and self.third_arg and self.check_gender(self.fourth_arg) and self.check_year(self.third_arg):
            calculation = Calculation("exams_data.sqlite", self.second_arg, self.third_arg, self.fourth_arg)
            calculation.if_gender()
            calculation.joined()
            calculation.sum()
            calculation.count_years()
            calculation.average()
            calculation.print_result()
        else:
            pass

    def second(self):
        if self.first_arg == "--2" and self.second_arg and self.third_arg and self.check_gender(self.fourth_arg) and self.check_year(self.third_arg):
            calculation = Calculation("exams_data.sqlite", self.second_arg, self.third_arg, self.fourth_arg)
            calculation.if_gender()
            calculation.joined()
            calculation.passed()
            calculation.sum()
            calculation.percent()
            calculation.add_percent()
            calculation.print_result()
        else:
            pass

    def third(self):
        if self.first_arg == "--3" and self.second_arg and self.check_gender(self.fourth_arg) and self.check_year(self.second_arg):
            calculation = Calculation("exams_data.sqlite", None, self.second_arg, self.third_arg)
            calculation.if_gender()
            calculation.highest_pass()
            calculation.data = calculation.get_cleaned_value_from_list(calculation.data)
            calculation.print_result()
        else:
            pass

    def fourth(self):
        if self.first_arg == "--4":
            calculation = Calculation("exams_data.sqlite")
            calculation.gender = self.second_arg
            calculation.if_gender()
            calculation.get_value_for_regression()
            calculation.count_years_from_database()
            calculation.regression()
        else:
            pass

    def fifth(self):
        if self.first_arg == "--5" and self.second_arg and self.third_arg and self.check_gender(self.fourth_arg):
            calculation = Calculation("exams_data.sqlite", self.second_arg)
            calculation.territory_second = self.third_arg
            calculation.gender = self.fourth_arg
            calculation.if_gender()
            calculation.get_value_for_compare()
            calculation.compare()
        elif self.first_arg == "--help":
            print('Commands:')
            print('REMEMBER: FIRST YOU SHOULD FILL THE DATABASE WITH DATA. -> "--get_data"')
            print('Choosing to divide results by gender is not required but it is possible by adding the last command '
                  'as "kobiety" or "mężczyźni".')
            print(' --help -> show this basic help menu.')
            print(' --get_data -> Importing data from api to database.')
            print(' --1 TERRITORY YEAR -> displaying the average number of people who took the exam for a given '
                  'province over the years, up to the given year.')
            print(' --2 TERRITORY YEAR -> displaying the percentage pass rate for a given province over the years, e.g.')
            print(' --3 YEAR -> Providing the voivodship with the best pass rate in a given year.')
            print(' --4 -> Displaying voivodships that recorded a decrease in the success rate in the following year.')
            print(' --5 FIRST_TERRITORY SECOND_TERRITORY -> comparison of two voivodships - for the two voivodships '
                  'listed, listing which voivodship had better pass rates in each available year.')

    def check_command(self):
        if self.first_arg != "1" or self.first_arg != "2" or self.first_arg != "3" or self.first_arg != "4" \
             "" or self.first_arg != "5" or self.first_arg != "--help" or self.first_arg != "--get_data":
            return True


if __name__ == '__main__':

    if args[1:]:
        first_argument = args[1]
    else:
        first_argument = ""

    if args[2:]:
        second_argument = args[2]
    else:
        second_argument = ""

    if args[3:]:
        third_argument = args[3]
    else:
        third_argument = ""

    if args[4:]:
        fourth_argument = args[4]
    else:
        fourth_argument = ""

    script = Script(args[1:], first_argument, second_argument, third_argument, fourth_argument)

    script.empty_command()
    script.get_data()
    script.first()
    script.second()
    script.third()
    script.fourth()
    script.fifth()
