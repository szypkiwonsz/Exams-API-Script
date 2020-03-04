### A python script that retrieves api data about joining and passing the Matura exam in given provinces. By entering the appropriate commands, we can display the selected data.

##### Avaible commands:

python script.py COMMAND

--help -> show basic help menu.

--get_data -> Importing data from api to database. 

--1 TERRITORY YEAR -> displaying the average number of people who took the exam for a given province over the years, up to the given year.

--2 TERRITORY YEAR -> displaying the percentage pass rate for a given province over the years, e.g.

--3 YEAR -> Providing the voivodship with the best pass rate in a given year.

--4 -> Displaying voivodships that recorded a decrease in the success rate in the following year.

--5 FIRST_TERRITORY SECOND_TERRITORY -> comparison of two voivodships - for the two voivodships listed, listing which voivodship had better pass rates in each available year.

##### Packages to install:
- pip install requests

##### Version of software used:
- Python 3.8.x
