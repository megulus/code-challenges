"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(texts[0])
    firstRecordTexts = texts[0]
    fromText = firstRecordTexts[0].strip()
    toText = firstRecordTexts[1].strip()
    timeText = firstRecordTexts[2].strip()
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    lastRecordCalls = calls[len(calls) - 1]
    fromCall = lastRecordCalls[0].strip()
    toCall = lastRecordCalls[1].strip()
    timeCall = lastRecordCalls[2].strip()
    durationCall = lastRecordCalls[3].strip()

print(f'First record of texts, {fromText} texts {toText} at time {timeText}')
print(f'Last record of calls, {fromCall} calls {toCall} at time {timeCall}, lasting {durationCall} seconds')





"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

