# CSV Report Generator

This Python program reads one or more CSV files containing people's data (name, age, city) and generates a report of adults in a selected city. The report is sorted by age and shows the oldest person.

## How it works

1. User enters the CSV file(s) name.
2. The program lists all available cities from the data.
3. User selects a city.
4. Program filters adults, counts them, finds the oldest, and sorts the list by age.
5. Output is printed on the screen and saved to a CSV file.

## How to run

```bash
python main.py
Follow the instructions to enter file names and city.

Requirements:
- Python 3.x
- CSV files in the same folder or in data/ folder.

Example CSV format

name,age,city
Anna,22,Warszawa
Bartek,30,Kraków
Celina,17,Gdańsk
Darek,40,Warszawa
