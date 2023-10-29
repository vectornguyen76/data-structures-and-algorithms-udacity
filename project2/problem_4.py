class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    users = group.get_users()
    if user in users:
        return True
    
    sub_groups = group.get_groups()
    for sub_group in sub_groups:
        exist_in_sub_group = is_user_in_group(user, sub_group)
        if exist_in_sub_group:
            return True
    
    return False

if __name__ == "__main__":
    # Testcase-1: Group with no Users test
    print("**** Testcase-1: Group with no Users test ****")
    empty_grp = Group("empty")
    user = "user"
    print(empty_grp.get_name(), "group has user?", is_user_in_group(user, empty_grp))  # Expecting False
    print("""*******************************""")

    # Testcase-2: Group with several users test
    print("**** Testcase-2: Group with several users test ****")
    grp = Group("test_grp")
    user1 = "user1"
    user2 = "user2"
    user3 = "user3"
    user4 = "user4"
    grp.add_user(user1)
    grp.add_user(user2)
    grp.add_user(user3)
    print(grp.get_name(), "group have user1?", is_user_in_group(user1, grp))  # Expecting True
    print(grp.get_name(), "group have user2?", is_user_in_group(user2, grp))  # Expecting True
    print(grp.get_name(), "group have user3?", is_user_in_group(user3, grp))  # Expecting True
    print(grp.get_name(), "group have user4?", is_user_in_group(user4, grp))  # Expecting False
    print("""*******************************""")

    # Testcase-3: Udacity Test Code
    print("**** Testcase-3: Udacity Test Code****")
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    sub_child_user_a = "sub_child_user_a"
    child.add_group(sub_child)
    parent.add_group(child)
    print(parent.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, parent))  # Expecting True
    print(child.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, child))  # Expecting True
    print(sub_child.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, sub_child))  # Expecting True
    print(parent.get_name(), "group has sub_child_user_a?", is_user_in_group(sub_child_user_a, parent))  # Expecting False
    print("""*******************************""")

    # Additional Testcase-4: Group not found test
    print("**** Additional Testcase-4: Group not found test ****")
    non_existent_group = Group("non_existent_group")
    user = "user"
    print(non_existent_group.get_name(), "group has user?", is_user_in_group(user, non_existent_group))  # Expecting False
    print("""*******************************""")

    # Additional Testcase-5: Group with no parent test
    print("**** Additional Testcase-5: Group with no parent test ****")
    isolated_group = Group("isolated_group")
    user = "user"
    isolated_group.add_user(user)
    print(isolated_group.get_name(), "group has user?", is_user_in_group(user, isolated_group))  # Expecting True
    print(isolated_group.get_name(), "group has sub_child_user?", is_user_in_group(sub_child_user, isolated_group))  # Expecting False
    print("""*******************************""")
