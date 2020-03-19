# Exams-API-Script

A python script that retrieves api data about joining and passing the Matura exam in given provinces. By entering the appropriate commands, we can display the selected data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python 3.8.x

```
https://www.python.org/downloads/
```

requests

```
pip install requests
```

### Running

A step by step series of examples that tell you how to run a script

```
python script.py COMMAND
```


You can also add "kobiety" or "mężczyźni" to view results split by gender

```
python script.py COMMAND kobiety
```


Show basic help menu

```
--help
```


Importing data from api to database

```
--get_data
```


Displaying the average number of people who took the exam for a given province over the years, up to the given year

```
--1 TERRITORY YEAR
```


Displaying the percentage pass rate for a given province over the years, e.g. 

```
--2 TERRITORY YEAR
```


Providing the voivodship with the best pass rate in a given year 

```
--3 YEAR
```


Displaying voivodships that recorded a decrease in the success rate in the following year

```
--4
```


Comparison of two voivodships - for the two voivodships listed, listing which voivodship had better pass rates in each available year


```
--5 FIRST_TERRITORY SECOND_TERRITORY
```


Example

```
python script.py --1 pomorskie 2012 mężczyźni
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/) - The programming language used

## Authors

* **Jan Kacper Sawicki** - [szypkiwonsz](https://github.com/szypkiwonsz)

## Acknowledgments

* The script was made as a recruitment task for an internship
