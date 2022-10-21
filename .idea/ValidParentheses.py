
def Check(open, close, s, i) : bool


    c = 0
    for x in range(i, len(s)):
        if s[x] = open:
            c = c++


def isValid(s: str) -> bool:


    counter = [0, 0, 0]
    symbol = {"(": ")", "[": "]", "{": "}"}
    symbolmap = {"(": 0, ")": 0, "[": 1, "]": 1, "{": 2, "}": 2}
    incsmap = {"(": +1, ")": -1, "[": +1, "]": -1, "{": +1, "}": -1}

    for i in range(0, len(s)):
        c = s[i]

        counterindex = symbolmap[c]
        increment = incsmap[c]
        counter[counterindex] = counter[counterindex] + increment

    

    for v in counter:
       if v != 0:


print(isValid(s))
s = "([)]"
return False

return True
