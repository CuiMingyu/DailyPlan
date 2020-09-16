s = "loveleetcode"


def firstUniqChar(s):
    dict = {}
    for i in s:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    for i in range(len(s)):
        if dict[s[i]] == 1:
            return i
    return -1


print(firstUniqChar(s))
