def longestCommonPrefix(strs):
    word = strs[0]

    for i in range(1, len(strs)):
        while True:
            if strs[i].startswith(word) and word in strs[i]:
                break
            else:
                word = word[:-1]

    return word


strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = ["c", "acc", "ccac"]

print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))
print(longestCommonPrefix(strs3))