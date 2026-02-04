def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))   # "fl"
print(longestCommonPrefix(["dog","racecar","car"]))      # ""
print(longestCommonPrefix(["interspecies","interstellar","interstate"]))  # "inters"
print(longestCommonPrefix(["throne","throne"]))          # "throne"
print(longestCommonPrefix(["throne","dungeon"]))         # ""
print(longestCommonPrefix(["a"]))                        # "a"
print(longestCommonPrefix(["",""]))                      # ""
print(longestCommonPrefix(["","abc"]))                   # ""
print(longestCommonPrefix(["abc",""]))                   # ""
print(longestCommonPrefix(["cir","car"]))                # "c"
