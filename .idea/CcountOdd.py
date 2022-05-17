def countOdds(lownum: int, highnum: int) -> int:

        if lownum % 2 == 0 and highnum % 2 == 0:
            return (highnum - lownum) // 2

        elif lownum % 2 != 0 and highnum % 2 != 0:
            return (highnum - lownum) // 2 + 1

        else:
            return (highnum - lownum + 1) // 2

while 1 == 1:
    lownum = int(input('Please enter low int: '))
    highnum = int(input('Please enter high int: '))
    print(countOdds(lownum, highnum))