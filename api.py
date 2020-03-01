import requests

from database import Database


class Api(Database):

    def __init__(self, api_link, name=None):

        super().__init__(name)
        self.api_link = api_link

    # Retrieves information about the number of pages of data needed to download all data.
    def number_of_pages(self):

        data = requests.get(self.api_link).json()
        link = data["links"]["last"]

        return int(link[-2:]) + 1

    def get_data(self):

        for pages in range(1, self.number_of_pages()):
            data = requests.get(self.api_link + "?page={}".format(pages)).json()

            # Getting all data from each page.
            for i in range(len(data['data'])):
                territory = data["data"][i]["attributes"]["col1"]
                joined_or_passed = data["data"][i]["attributes"]["col2"]
                gender = data["data"][i]["attributes"]["col3"]
                year = int(data["data"][i]["attributes"]["col4"])
                number_of_people = int(data["data"][i]["attributes"]["col5"])

                self.cursor.execute(
                    "INSERT INTO EXAM_DATA (TERRITORY, JOINED_AND_PASSED, GENDER, YEAR, PEOPLE) VALUES "
                    "(?, ?, ?, ?, ?)", (territory, joined_or_passed, gender, year, number_of_people))

        self.close()





