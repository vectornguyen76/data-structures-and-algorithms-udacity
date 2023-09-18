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

# Initialize sets to store numbers that make outgoing calls and numbers involved in texts or incoming calls
outgoing_calls = set()
text_receivers = set()
text_senders = set()
incoming_call_receivers = set()

# Populate the sets based on the data from 'texts' and 'calls' lists
for call in calls:
    outgoing_calls.add(call[0])
    incoming_call_receivers.add(call[1])

for text in texts:
    text_senders.add(text[0])
    text_receivers.add(text[1])

# Identify possible telemarketers (outgoing calls - (text senders + incoming call receivers))
possible_telemarketers = outgoing_calls - (text_senders | incoming_call_receivers)

# Sort the possible telemarketers lexicographically
sorted_possible_telemarketers = sorted(possible_telemarketers)

# Print the results
print("These numbers could be telemarketers:")
for number in sorted_possible_telemarketers:
    print(number)

# Calculate Big O
'''
- Initializing the sets has a constant time complexity, O(1).
- Populating the sets based on 'calls' and 'texts' data has time complexities of O(n) and O(m), respectively, where n is the number of calls, and m is the number of texts.
- Identifying possible telemarketers involves set operations (subtraction and union), which take O(n + m) time.
- Sorting the 'sorted_possible_telemarketers' set using sorted() has a time complexity of O(k * log(k)), where k is the number of possible telemarketers.
- Printing the results has a time complexity of O(k), where k is the number of possible telemarketers.
'''