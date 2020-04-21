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
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = set()

for caller in calls:
    telemarketers.add(caller[0])

for callReceiver in calls:
    telemarketers.discard(callReceiver[1])

for textSender in texts:
    telemarketers.discard(textSender[0])

for textReceiver in texts:
    telemarketers.discard(textReceiver[1])

print()
print("These numbers could be telemarketers: ")
print()

ans = set()
ans = sorted(telemarketers)

for i in ans:
    print(i)
