# Write a function to find the longest common prefix string amongst an array of strings.

def longestCommonPrefix( strs ):
    if len(strs) == 0:
        return ""
    res = ""
    flag = True
    count = 0
    while flag or count == len(min(strs,key=len)):
        temp = strs[0][count]
        for i in range(1,len(strs)):
            if strs[i][count] != temp:
                flag = False
                break
        if flag:
            res = temp
            count += 1
    return res