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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""

# Create sets of all phone number in texts and calls files
text_numbers = set([num for row in texts for num in [row[0], row[1]]])
call_numbers = set([num for row in calls for num in [row[0], row[1]]])

# Find phone number that are not in texts and not in the second column of calls
unique_numbers = sorted(text_numbers.union(call_numbers) - text_numbers - {row[1] for row in calls})

# Print the unique numbers
print("These numbers could be telemarketers:")
for num in unique_numbers:
    print(num)
