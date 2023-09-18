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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Initialize variables to store the counts
total_calls_from_bangalore = 0
calls_to_bangalore = 0
codes_called = set()

# Iterate through the calls data
for call in calls:
    # print(call)
    caller, receiver, _, _ = call
    if caller.startswith('(080)'):
        total_calls_from_bangalore += 1
        if receiver.startswith('(080)'):
            calls_to_bangalore += 1
        elif receiver.startswith('('):
            area_code = receiver.split(')')[0] + ')'
            codes_called.add(area_code)
        elif receiver.startswith(('7', '8', '9')):
            mobile_prefix = receiver[:4]
            codes_called.add(mobile_prefix)
        elif receiver.startswith('140'):
            codes_called.add('140')

# Calculate the percentage
percentage_calls_to_bangalore = (calls_to_bangalore / total_calls_from_bangalore) * 100

# Sort the codes_called set lexicographically
sorted_codes_called = sorted(codes_called)

# Print the results
print("The numbers called by people in Bangalore have codes:")
for code in sorted_codes_called:
    print(code)

print(f"{percentage_calls_to_bangalore:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


# Calculate Big O
'''
- The loop that iterates through the 'calls' data has a complexity of O(n), where n is the number of calls.
- Inside the loop, there are various operations that have a constant time complexity, denoted as O(1).
- Sorting the 'codes_called' set using sorted() has a time complexity of O(m * log(m)), where m is the number of distinct codes.
- Printing the sorted codes and the percentage calculation are also O(1).
'''