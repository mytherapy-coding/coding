import numpy as np


def min_max(lst):
    res = []
    min_val = lst[0]
    for e in lst:
        if e < min_val:
            min_val = e
    res.append(min_val)
    max_val = lst[0]
    for e in lst:
        if e > max_val:
            max_val = e
    res.append(max_val)
    return res

def min_max0(lst):
    min_val = max_val = lst[0]
    for e in lst:
        if e < min_val:
            min_val = e
        if e > max_val:
            max_val = e
    return [min_val, max_val]


def min_max01(lst):
    min_val = max_val = lst[0]
    for e in lst:
        min_val = min(min_val,e)
        max_val = max(max_val,e)
    return [min_val, max_val]

def min_max1(lst):
    return [min(lst), max(lst)]


def min_max2(lst):
    lst = np.array(lst)
    res = np.min(lst)
    lst = np.array(lst)
    res1 = np.max(lst)
    return [res, res1]

def min_max3(lst):
    return [np.min(np.array(lst)), np.max(np.array(lst))]


def min_max4(lst):
    res = sorted(lst)
    return [res[0], res[-1]]

print(min_max4([30, 60, 9, 65, 8.5]))