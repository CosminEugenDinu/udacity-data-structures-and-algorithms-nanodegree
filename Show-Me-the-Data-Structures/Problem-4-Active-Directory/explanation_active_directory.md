Algorithm `is_user_in_group` iterates over `groups` array. For every group, search for existence of `user`; if not found, recursively iterates through next group.

Time complexity is O(m^n), where `m` is the number of groups and `n` is the number of users. This is the worst case, when the user is found at the last group.
