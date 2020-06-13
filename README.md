# Exams-API-Script

A python script that retrieves api data about joining and passing the Matura exam in given provinces. By entering the appropriate commands, we can display the selected data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Libraries and Packages

```
pip install -r requirements.tx
```
---
### Avaible commands

How to enter commands

```
python script.py --[command]
```
---
You can also add "kobiety" or "mężczyźni" to view results split by gender

```
python script.py [command] kobiety
```
---
Show basic help menu

```
python script.py --help
```
---
Importing data from api to database

```
python script.py --get_data
```
---
Displaying the average number of people who took the exam for a given province over the years, up to the given year

```
python script.py --1 [territory] [year]
```
---
Displaying the percentage pass rate for a given province over the years, e.g. 

```
python script.py --2 [territory] [year]
```
---
Providing the voivodeship with the best pass rate in a given year 

```
python script.py --3 [year]
```
---
Displaying provinces that recorded a decrease in the success rate in the following year

```
python script.py --4
```
---
Comparison of two provinces - for the two provinces listed, listing which voivodship had better pass rates in each available year

```
python script.py --5 [first_territory] [second_territory]
```
---
Example

```
python script.py --1 pomorskie 2012 mężczyźni
```
---

### Running

A step by step series of examples that tell you how to run a script

```
Download project
```
```
Install requirements
```
```
Run terminal with choosen folder "Exams-API-Script>"
```
```
Type selected command
```
---
## Built With

* [Python 3.8](https://www.python.org/) - The programming language used

## Authors

* **Jan Kacper Sawicki** - [szypkiwonsz](https://github.com/szypkiwonsz)

## Acknowledgments

* The script was made as a recruitment task for an internship
