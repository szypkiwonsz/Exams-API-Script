import sys

from api import Api

args = sys.argv
args = args[1:]


class Script:

    def __init__(self, command):

        self.command = command

    if len(args) == 0:
        print("This command not exist! Write: python main.py --help")

    else:
        if sys.argv[1] == "--get_data":
            api = Api("https://api.dane.gov.pl/resources/17363/data", "exams_data.sqlite")
            api.get_data()


if __name__ == '__main__':
    Script(sys.argv[1])
