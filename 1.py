list1 = []
list2 = []

str1 = input("Enter numbers from 0 to 9 for L1 list: ")
for s in str1.split():
    i = int(s)
    list1.append(i)

str2 = input("Enter numbers from 0 to 9 for L2 list: ")
for s in str2.split():
    i = int(s)
    list2.append(i)

sum_list = []
n = 0
s = 0
for i in list1:
    s = s + list1[n] + list2[n]
    if s < 10:
        sum_list.append(s)
        n = n + 1
        s = 0
    else:
        r = s % 10
        c = s // 10
        sum_list.append(r)
        s = c
        n = n + 1

if s != 0:
    sum_list.append(s)

print(sum_list)
