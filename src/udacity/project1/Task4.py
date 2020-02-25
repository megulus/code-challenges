"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

candidates = set()
non_candidates = set()




with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for t in texts:
        tFrom = t[0].strip()
        tTo = t[1].strip()
        non_candidates.add(tFrom)
        non_candidates.add(tTo)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for c in calls:
        cFrom = c[0].strip()
        cTo = c[1].strip()
        non_candidates.add(cTo)
        if cFrom not in non_candidates:
            candidates.add(cFrom)
        elif cFrom in non_candidates and cFrom in candidates:
            candidates.remove(cFrom)



candidatesList = sorted(candidates)
print('These numbers could be telemarketers:')
[print(x) for x in candidatesList]

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

