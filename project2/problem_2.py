import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
      suffix (str): Suffix of the file name to be found.
      path (str): Path of the file system.

    Returns:
      A list of file paths with the given suffix.
    """
    # Initialize a list to store the matching file paths
    result = []

    if not os.path.exists(path):
      print("The specified path does not exist")
      return result
    
    # Iterate through the contents of the directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path) and item.endswith(suffix):
            # If the item is a file and has the desired suffix, add it to the result
            result.append(item_path)
        elif os.path.isdir(item_path):
            # If the item is a directory, recursively search in that directory
            result.extend(find_files(suffix, item_path))

    return result

# Test the find_files function with your test cases
# Test Case 1: Search for ".c" files in the provided test directory
testdir_files = find_files(".c", "./testdir")
print(testdir_files)
# Expected output: 
# ['./testdir\\subdir1\\a.c', './testdir\\subdir3\\subsubdir1\\b.c', './testdir\\subdir5\\a.c', './testdir\\t1.c']

# Test Case 2: Search for ".h" files in the provided test directory
testdir_h_files = find_files(".h", "./testdir")
print(testdir_h_files)
# Expected output: 
# ['./testdir\\subdir1\\a.h', './testdir\\subdir3\\subsubdir1\\b.h', './testdir\\subdir5\\a.h', './testdir\\t1.h']

# Test Case 3: Search for ".txt" files in the current directory (empty result)
current_dir_txt_files = find_files(".txt", ".")
print(current_dir_txt_files)
# Expected output: 
# []

# Test Case 4: Search for ".py" files in a non-existent directory
non_existent_dir_files = find_files(".py", "./non_existent_directory")
print(non_existent_dir_files)
# Expected output: 
# No files found for the given extension
