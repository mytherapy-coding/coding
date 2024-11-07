def flatten_list(nested_list):
    res = []

    def helper(current_list):
        for item in current_list:
            if isinstance(item, list):  # Check if item is a list
                helper(item)  # Recursively flatten the sublist
            else:
                res.append(item)  # Add the non-list item to the result

    helper(nested_list)
    return res

nested_list = [1, 3, 4, 5, [7, 3]]
print(flatten_list(nested_list))




def flatten(nested_list, res):
    for num in nested_list:
        if isinstance(num, list):
            flatten(num, res)  # Recursive call if num is a list
        else:
            res.append(num)

nested_list = [1, 3, 4, 5, [7, 3]]
res = []
flatten(nested_list, res)
print(res)



def flatten1(nested_list, res):
    for num in nested_list:
        if isinstance(num, list):
            flatten1(num, res)  # Recursive call if num is a list
        else:
            res.append(num)
    return res


nested_list = [1, 3, 4, 5, [7, 3]]
print(flatten1(nested_list, []))
