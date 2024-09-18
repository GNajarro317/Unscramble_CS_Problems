"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # Places the numbers found in the first and second column of the texts.csv into a single list
    text_numbers = [col[0] for col in texts] + [col[1] for col in texts]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # Places the numbers found in the first and second column of the calls.csv into a single list
    call_numbers = [col[0] for col in calls] + [col[1] for col in calls]

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
from collections import Counter
# Combines all the numbers collected from both files and counts the unique numbers
all_numbers = text_numbers + call_numbers
unique_numbers = len(Counter(all_numbers))
print(f"There are {unique_numbers} different telephone numbers in the records.")
