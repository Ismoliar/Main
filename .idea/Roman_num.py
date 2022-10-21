

def romanToInt(s: str) -> int:
    numlist = []
    rmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # map of roman's nums

    for i in range(0, len(s)):
        c = s[i]
        v = rmap[c]
        numlist.append(v)
      
    num = 0
    i = len(numlist) - 1 # itarated from the end of nimlist
    while i >= 0:
        if i == 0: # if last element of list
            num = num + numlist[i]
            i = -1 # end of while
        elif numlist[i] <= numlist[i-1]: # if have previos value bigest
            num = num + numlist[i]
            i = i - 1
        else:
            count = 0
            count = numlist[i] - numlist[i-1] #if previos value less
            num = num + count
            i = i - 2

    print(num)
    return -1

s = "XIX"

print(romanToInt(s))

