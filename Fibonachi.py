import time


def fibonachi(n):
     if n == 1 or n == 2:
         return 1
     return fibonachi(n-1) + fibonachi(n-2)


while 1==1:
    n = int(input('Please enter int: '))
    start = time.time()
    print(fibonachi(n))
    print(time.time() - start)
