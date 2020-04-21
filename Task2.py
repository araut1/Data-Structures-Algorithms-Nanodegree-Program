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

numberToTimeMap = {}

for callEntry in calls:

    caller = str(callEntry[0])
    receiver = str(callEntry[1])

    if caller in numberToTimeMap:
        temp = int(numberToTimeMap[caller])
        temp += int(callEntry[3])
        numberToTimeMap[caller] = temp
    else:
        numberToTimeMap[caller] = int(str(callEntry[3]))

    if receiver in numberToTimeMap:
        temp = int(numberToTimeMap[receiver])
        temp += int(callEntry[3])
        numberToTimeMap[receiver] = temp
    else:
        numberToTimeMap[receiver] = int(str(callEntry[3]))

maxTime=0
for numberKey in numberToTimeMap.keys():
    if numberToTimeMap[numberKey] > maxTime:
        maxNumber = numberKey
        maxTime = numberToTimeMap[numberKey]

str(maxNumber)
print(str(maxNumber) + " spent the longest time, " + str(maxTime) + " seconds, on the phone during September 2016.")