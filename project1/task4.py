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

list_caller = []

for call in calls:
    list_caller.append(call[0])

set_caller = set(list_caller)
    
for text in texts:
    if text[0] in set_caller:
        set_caller.remove(text[0])
        
    if text[1] in set_caller:
        set_caller.remove(text[1])

for call in calls:
    if call[1] in set_caller:
        set_caller.remove(call[1])
    
list_telemarketers = list(set_caller)
print("These numbers could be telemarketers: ")
for caller in list_telemarketers:
    print(caller)

# Calculate Big O
'''
1. Creating the list_caller list by iterating through the calls list takes O(N) time, where N is the number of items in the calls list.
2. Creating the set_caller set from list_caller also takes O(N) time because it involves iterating through list_caller once to remove duplicates.
3. Iterating through the texts list to remove numbers from set_caller takes O(M) time, where M is the number of items in the texts list. 
In the worst case, all numbers in texts are unique, resulting in O(M) removal operations from set_caller.
4. Iterating through the calls list again to remove numbers from set_caller takes O(N) time, where N is the number of items in the calls list.
5. Converting set_caller to list_telemarketers takes O(N) time because it involves copying all unique numbers from the set to a list.
6. Printing the potential telemarketer numbers is also a linear operation because iterating through the list_telemarketers, so it takes O(N) time
'''