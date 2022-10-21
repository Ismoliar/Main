

def isPalindrome(x: int) -> bool:
    if x < 0:
        return(False)
    else:
        z = str(x) # convert int to str
        y = z[::-1] # revers number step 1
        if z == y:
            return(True)
        else:
            return (False)

x = 21

result = isPalindrome(x)

print(result)
