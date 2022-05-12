def odd_count(lownum, highnum):

    num_list = []
    i = lownum
    n = 0
    odd_count = 0

# create list of num
    while i <= highnum:
        num_list.append(i)
        i = i+1

# count odd
    for n in num_list:
        if n % 2 != 0:
            odd_count = odd_count + 1
    return odd_count

while 1 == 1:
    lownum = int(input('Please enter low int: '))
    highnum = int(input('Please enter high int: '))
    print(odd_count(lownum, highnum))
