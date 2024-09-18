"""
Read file into texts and calls.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
"""
# Pulls directly from the first row of the text list and prints the calling number, recieving number, and date stamp
for list in texts:
    print("First record of texts, " + list[0] + " texts " + list[1] + " at time " + list[2] + "")
    break

# Defines the last row of the calls file and has it printed out
for list in calls:
    last_row = calls[-1]
    print("Last record of calls, " + last_row[0] + " calls " + last_row[1] + " at time " + last_row[2] + ", lasting " + last_row[3] + " seconds")
    break
