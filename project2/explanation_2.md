# Problem 2: File Recursion

The `find_files` function is designed to recursively search for all files beneath a given path that have a specified suffix in their file names. It operates on the provided directory path and returns a list of file paths matching the criteria.

## Implementation Details

1. **Function Signature**
   ```python
   def find_files(suffix, path):
   ```

   The function takes two parameters: `suffix` (the file name suffix to search for, e.g., ".c" or ".h") and `path` (the root directory path to start the search from).

2. **Result List Initialization**
   
   Before starting the search, an empty list called `result` is initialized to store the matching file paths.

3. **Directory Iteration**
   
   The function iterates through the contents of the directory specified by the `path` parameter using `os.listdir(path)`. For each item found in the directory:

   - It constructs the full path to the item using `os.path.join(path, item)` and stores it in the `item_path` variable.

4. **File and Directory Handling**

   - If the `item` is a file (determined using `os.path.isfile(item_path)`) and its name ends with the specified `suffix`, it is considered a match, and its path is added to the `result` list.
   - If the `item` is a directory (determined using `os.path.isdir(item_path)`), the function recursively calls itself with the `item_path` as the new search directory. The results of this recursive call are then extended into the `result` list.

5. **Returning the Result**
   
   After all the recursive searches have been completed, the function returns the `result` list, which contains all the file paths that match the given suffix under the specified directory.

## Time and Space Efficiency

- **Time Efficiency**: The function has time complexity that depends on the number of files and directories in the search hierarchy. In the worst case, it visits every file and directory once, resulting in O(N) time complexity, where N is the total number of files and directories.
  
- **Space Efficiency**: The space efficiency of the function is mainly determined by the `result` list, which stores the file paths. The size of this list depends on the number of files matching the criteria. In the worst case, if all files match, the space complexity would be O(N) where N is the number of matching files.

The test cases are used to validate the correctness of the function and its ability to handle different scenarios, including empty results and the presence of subdirectories.