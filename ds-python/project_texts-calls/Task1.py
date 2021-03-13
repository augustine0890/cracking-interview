"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def add_number(file: list, tel_numners: set) -> set:
    for column in [0, 1]:
        temp_numbers = [data[column] for data in file]
        tel_numners.update(temp_numbers)
    return tel_numners

tel_numbers = set()

tel_numbers = add_number(calls, tel_numbers)
tel_numbers = add_number(texts, tel_numbers)

print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))