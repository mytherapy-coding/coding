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

print()


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

print()

def flatten1(nested_list, res):
    for num in nested_list:
        if isinstance(num, list):
            flatten1(num, res)  # Recursive call if num is a list
        else:
            res.append(num)
    return res


nested_list = [1, 3, 4, 5, [7, 3]]
print(flatten1(nested_list, []))

print()

def flatten2(nested_list, res=None):
    if res is None:
        res = []  # Initialize res if it's not provided
    for num in nested_list:
        if isinstance(num, list):
            flatten2(num, res)  # Recursive call if num is a list
        else:
            res.append(num)
    return res

print()

nested_list = [1, 3, 4, 5, [7, 3]]
print(flatten2(nested_list))

nested_list = [1, 3, 4, 5, [7, 3]]
print(flatten2(nested_list))

print()

def flatten_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)  # Recursively yield items from sublist
        else:
            yield item  # Yield the individual element

# Test cases
nested_list1 = [1, 3, 4, 5, [7, 3]]
nested_list2 = [1, 3, 4, 5, [7, 3]]

flat1 = [item for item in flatten_generator(nested_list1)]
print(flat1)

flat2 = [item for item in flatten_generator(nested_list1)]
print(flat2)

print()

def flatten_list(nested_list):
    def helper(current_list):
        for item in current_list:
            if isinstance(item, list):
                yield from helper(item)  # Recursively yield items from sublist
            else:
                yield item  # Yield the individual element

    return list(helper(nested_list))  # Convert generator to a list for the final result

# Example usage
nested_list1 = [1, [2, [3, 4], 5], 6, [7, 8]]
nested_list2 = [[1, 2], [3, [4, 5]], 6]

# Collect the generator output into a list for printing
res1 = flatten_list(nested_list1)
res2 = flatten_list(nested_list2)

print(res1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(res2)  # Output: [1, 2, 3, 4, 5, 6]
