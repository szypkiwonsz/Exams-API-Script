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

    def empty_command(self):
        if len(self.command) == 0:
            print("This command not exist! Write: python main.py --help")

    def get_data(self):
        if self.first_arg == "--get_data":
            api = Api("https://api.dane.gov.pl/resources/17363/data", "exams_data.sqlite")
            if api.is_empty():
                api.get_insert_data()
            else:
                print("Database is already filled with data!")

    def first(self):
        if self.first_arg == "--1" and self.second_arg and self.third_arg:
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
        if self.first_arg == "--2" and self.second_arg and self.third_arg:
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
        if self.first_arg == "--3":
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