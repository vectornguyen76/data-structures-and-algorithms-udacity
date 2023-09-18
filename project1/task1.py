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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:

"""
list_telephone = []
for text in texts:
    list_telephone.append(text[0])
    list_telephone.append(text[1])

for call in calls:
    list_telephone.append(call[0])
    list_telephone.append(call[1])
    
print(f"There are {len(set(list_telephone))} different telephone numbers in the records.")

# Calculate Big O
'''
1. Iterating through the texts list involves a loop that goes through each item in the list once. 
The same applies to the loop for the calls list. Each iteration of these loops involves appending two elements to the list_telephone. 
Therefore, the time complexity for these loops is O(N), where N is the total number of elements in both texts and calls combined.

2. Creating a set from the list_telephone using set(list_telephone) takes O(N) time in the worst case 
because it needs to iterate through all elements to identify unique values.

3. Finally, calculating the length of the set using len(set(list_telephone)) is a constant-time operation and can be considered O(1).
'''