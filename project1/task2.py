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
dict_telephone = {}
for call in calls:
    if call[0] not in dict_telephone:
        dict_telephone.update({call[0]: int(call[3])})
    else:
        dict_telephone[call[0]] += int(call[3])
        
    if call[1] not in dict_telephone:
        dict_telephone.update({call[1]: int(call[3])})
    else:
        dict_telephone[call[1]] += int(call[3])
  
longest_telephone = max(dict_telephone, key=dict_telephone.get)      
print(f"{longest_telephone} spent the longest time, {dict_telephone[longest_telephone]} seconds, on the phone during September 2016.")

# Calculate Big O
'''
1. Iterating through the calls list involves a loop that goes through each item in the list once. 
In each iteration, perform dictionary lookups and updates, both of which are typically O(1) operations on average. 
Therefore, the time complexity of this loop is O(N), where N is the number of items in the calls list.

2. Finding the telephone number that spent the longest time on the phone involves iterating 
through the keys in the dict_telephone dictionary to find the maximum value. 
This operation also has a time complexity of O(N), where N is the number of unique telephone numbers in the calls list.
'''