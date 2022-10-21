

def longestCommonPrefix(strs) -> str:

    prefix = ""

    w = strs[0]
    for i in range(0, len(w)):

        c = w[i] #i elements of word with index 0
        for n in range(1, len(strs)):
            a = strs[n] # n element of strs = a
            if i >= len(a) or c != a[i]:
                return prefix

        prefix = prefix + c # add simbol to str


    return prefix

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))
