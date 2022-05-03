dic = {1: 1, 2: 1}


def fibonachi(n):
    if n in dic:
        return dic[n]
    f = fibonachi(n - 1) + fibonachi(n - 2)
    dic[n] = f
    return f


while 1 == 1:
    i = int(input('Please enter int: '))
    print(fibonachi(i))
