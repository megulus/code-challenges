"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

max_time = 0
most_time_spent = ''
cumulative_call_time = {}


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        num1 = call[0].strip()
        num2 = call[1].strip()
        duration = int(call[3].strip())
        if num1 in cumulative_call_time:
            cumulative_call_time[num1] += duration
        else:
            cumulative_call_time[num1] = duration
        if num2 in cumulative_call_time:
            cumulative_call_time[num2] += duration
        else:
            cumulative_call_time[num2] = duration
        if cumulative_call_time[num1] > max_time:
            max_time = cumulative_call_time[num1]
            most_time_spent = num1
        if cumulative_call_time[num2] > max_time:
            max_time = cumulative_call_time[num2]
            most_time_spent = num2
        

print(f'{most_time_spent} spent the longest time, {max_time} seconds, on the phone during September 2016.')


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

