def compress0(chars: list[str]) -> int:
    '''
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    '''

    prev_char = chars[0]
    count = 1
    res = []
    for ch in chars[1:] + [None]:
        if ch == prev_char:
            count += 1
        else:
            res.append(prev_char)
            if count > 1:
                res.extend(str(count))
            prev_char = ch
            count = 1
    chars.clear()
    chars.extend(res)
    return len(res)


def compress1(chars: list[str]) -> int:
    prev_char = chars[0]
    count = 1
    res = []
    for ch in chars[1:] + [None]:
        if ch == prev_char:
            count += 1
        else:
            print((prev_char, str(count)))
            res.append(prev_char)
            if count > 1:
                res.extend(str(count))
            prev_char = ch
            count = 1
    chars[:] = res
    return len(res)


def compress2(chars: list[str]) -> int:
    prev_char = chars[0]
    count = 1
    j = 0
    for ch in chars[1:] + [None]:
        if ch == prev_char:
            count += 1
        else:
            chars[j] = prev_char
            j += 1
            if count > 1:
                chars[j:j + len(str(count))] = list(str(count))
                j += len(str(count))
            prev_char = ch
            count = 1
    return j


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(chars)
print(compress2(chars))
print(chars)
