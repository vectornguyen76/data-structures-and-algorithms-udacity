# Problem 4: Active Directory

This code provides a Python class `Group` and a function `is_user_in_group` that checks whether a user is a member of a group or any of its subgroups.

## Class Structure

The `Group` class has the following attributes and methods:
- `name`: A name for the group.
- `groups`: A list to store subgroups.
- `users`: A list to store users.

### `__init__(self, _name)`

The constructor initializes a group with a name, an empty list for subgroups, and an empty list for users. This data structure was chosen to represent a group hierarchy where a group can contain subgroups and users.

### `add_group(self, group)`

This method allows you to add a subgroup to the group's list of subgroups.

### `add_user(self, user)`

This method allows you to add a user to the group's list of users.

### `get_groups(self)`

This method returns the list of subgroups for the group.

### `get_users(self)`

This method returns the list of users in the group.

### `get_name(self)`

This method returns the name of the group.

## Function `is_user_in_group(user, group)`

This function checks whether a given user is a member of the specified group or any of its subgroups. It follows a recursive approach to traverse the group hierarchy.

- It first checks if the user is in the current group's list of users.
- Then, it iterates through the subgroups of the current group and recursively calls itself on each subgroup to check if the user is in any of the subgroups.
- If the user is found in any subgroup, the function returns `True`. Otherwise, it returns `False`.

## Efficiency

### Time Efficiency

- The time efficiency of this code depends on the structure of the group hierarchy. In the worst case, where the user is not in any group, it may need to traverse all groups and subgroups. The time complexity can be considered O(n), where 'n' is the total number of groups and subgroups in the hierarchy.

### Space Efficiency

- The space efficiency is influenced by the use of lists to store subgroups and users. The space complexity can be considered O(n) for the space needed to store all the groups and users in the hierarchy. This can potentially be improved with more memory-efficient data structures if the hierarchy is very large.
