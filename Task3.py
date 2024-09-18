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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
The percentage should have 2 decimal digits
"""

# Part A
# Message is written outside of the loop
print("The numbers called by people in Bangalore have codes:")

areaCodes = set()
for call in calls:
  if call[0].startswith("(080)"):
  # This will seperate the numbers that start with (0
    if call[1].startswith("(0"):
      areaCode = call[1][0:call[1].find(')')+1]
  # This will seperate the numbers that start with 7, 8, or 9
    elif call[1].startswith(('7','8','9')):
      areaCode = call[1][0:4]
  # This will seperate the numbers that start with 140
    elif call[1].startswith("140"):
      areaCode = "140"
    areaCodes.add(areaCode)
# This will print the unique codes
for areaCode in sorted(areaCodes):
  print(areaCode)


# Part B
# Initializes variables
calls_from080 = 0
calls_to080 = 0

# Iterate through the rows
for row in calls:
  caller = row[0]
  reciever = row[1]

  # Check if caller starts with "(080)"
  if caller.startswith("(080)"):
    calls_from080 += 1

    # Check if reciever starts with "(080)"
    if reciever.startswith("(080)"):
      calls_to080 += 1

# Calculate the percentage
percentage = (calls_to080 / calls_from080) * 100

print(f"{percentage:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
