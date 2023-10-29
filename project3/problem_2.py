def rotated_array_search(input_list, number):
    left, right = 0, len(input_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if input_list[mid] == number:
            return mid
        
        if input_list[left] <= input_list[mid]:
            # Left half is sorted
            if input_list[left] <= number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if input_list[mid] < number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Test cases
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])