"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# A dictionary that will store the total duration for each number
call_duration = {}

# Goes through the row in list
for row in calls:
    caller = row[0]
    receiver = row[1]
    duration = int(row[3])

    # Updates total duration for the caller
    if caller in call_duration:
        call_duration[caller] += duration
    else:
        call_duration[caller] = duration

    # Updates total duration for the receiver
    if receiver in call_duration:
        call_duration[receiver] += duration
    else:
        call_duration[receiver] = duration

# Finds the number with the longest call and its duration
longest_caller = max(call_duration, key=call_duration.get)
max_duration = call_duration[longest_caller]

print(f"{longest_caller} spent the longest time, {max_duration} seconds, on the phone during September 2016.")
