def lengthLongestPath(input: str) -> int:
    words = input.split('\n')
    filepath = []
    maxlen = 0
    for word in words:
        quantity = word.count('\t')
        name = word.replace('\t', '')
        if '.' in name:
            filepath.append(name)
            fullpath = '/'.join(filepath)
            maxlen = max(len(fullpath), maxlen)
            filepath.pop()
        else:
            filepath = filepath[:quantity]
            filepath.append(name)

    return maxlen

def lengthLongestPath2(input: str) -> int:
    words = input.split('\n')
    filepath = []
    maxlen = 0
    for word in words:
        quantity = word.count('\t')
        name = word.replace('\t', '')
        if '.' in name:
            fullpath = '/'.join(filepath + [name])
            maxlen = max(len(fullpath), maxlen)
        else:
            filepath = filepath[:quantity]
            filepath.append(name)

    return maxlen

print(lengthLongestPath2("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
